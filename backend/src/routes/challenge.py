from fastapi import APIRouter, Request, HTTPException, Response, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .. database.database import (
    create_challenge,
    get_challenge_quota,
    create_challenge_quota, 
    get_user_challenges,
    reset_quota_if_needed
)
from ..ai_generator import generate_challenge_ai
from ..utils import authenticate_and_get_user_details
from ..database.models import get_db
import json
from datetime import datetime

router = APIRouter()

class ChallengeRequest(BaseModel):
    difficulty: str
    class Config:
        json_schema_extra = {
            "example": {
                "difficulty": "easy"
            }
        }

@router.post("/generate-challenge")
async def generate_challenge( request_obj: Request, request: ChallengeRequest, db:Session= Depends(get_db)):
    try:
        user_details = authenticate_and_get_user_details(request_obj)
        user_id = user_details.get("user_id")
        quota = get_challenge_quota(db, user_id)
        if not quota:
            quota = create_challenge_quota(db, user_id)
            if not quota:
                create_challenge_quota(db, user_id)
            quota = get_challenge_quota(db, user_id)
        if quota.quota_remaining <= 0:
            raise HTTPException(status_code=403, detail="Quota exhausted.")
        challenges_data = generate_challenge_ai(request.difficulty)
        print(challenges_data)
        new_challenge = create_challenge(
            db=db,
            difficulty= request.difficulty,
            created_by=user_id,
            title= challenges_data['title'],
            options=json.dumps(challenges_data['options']),
            correct_anwser_id=challenges_data['correct_answer_id'],
            explanation=challenges_data['explanation']

        )
        
        quota.quota_remaining -= 1
        db.commit()
        return {
            "id": new_challenge.id,
            "difficulty":request.difficulty,
            "title":new_challenge.title,
            "options":json.loads(new_challenge.options),
            "correct_answer_id": new_challenge.correct_answer_id,
            "explanation":new_challenge.explanation,
            "timestamp":new_challenge.date_created.isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/my-history")
async def myhistory(resquest:Request, db: Session = Depends(get_db)):
    user_details = authenticate_and_get_user_details(resquest)
    user_id =user_details.get("user_id")
    challenges = get_user_challenges(db, user_id)
    return  challenges 

@router.get("/quota")
async def get_quota(request:Request, db: Session = Depends(get_db)):
    print(request)
    user_details = authenticate_and_get_user_details(request)
    user_id = user_details.get("user_id")
    
    quota = get_challenge_quota(db, user_id)
    if not quota:
        return "Khoong lay duoc du lieu",{
            "user_id": user_id,
            "quota_remaining": 0,
            "last_reset_date": datetime.now()
            }
    quota = reset_quota_if_needed(db, user_id)
    
    return quota