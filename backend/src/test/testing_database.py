from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.database.database import get_challenge_quota
from src.database.database import Session

if __name__ == "__main__":
    import uvicorn
    from src.database.database import Session

    # Kiểm tra get_challenge_quota
    def test_get_challenge_quota():
        db = Session
        try:
            user_id = "user_30li2vYuZAl8hcCbtapLoMfhKKz"  
            challenge_quotas = get_challenge_quota(db, user_id)
            print(f"Challenge quota của {user_id}: {challenge_quotas}")
        finally:
            db.close()

    test_get_challenge_quota()
    # Chạy server
    uvicorn.run("app", host="0.0.0.0", port=5000)