from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import models 


def get_challenge_quota(db: Session, user_id: str):
    return (db.query(models.ChallengeQuota)
            .filter(models.ChallengeQuota.user_id == user_id)
            .first())

def create_challenge_quota(db: Session, user_id: str):
    quota = models.ChallengeQuota(user_id=user_id, quota_remaining=50, last_reset_date=datetime.now())
    db.add(quota)
    db.commit()
    db.refresh(quota)
    return quota

def reset_quota_if_needed(db: Session, user_id: str):
    quota = get_challenge_quota(db, user_id)
    if not quota:
        return create_challenge_quota(db, user_id)

    # Reset the quota if the last reset date is more than 24 hours ago
    if datetime.now() - quota.last_reset_date > timedelta(days=1):
        quota.quota_remaining = 10
        quota.last_reset_date = datetime.now()
        db.commit()
        db.refresh(quota)
    return quota

def create_challenge(
        db: Session, 
        challenge: models.Challenge
        ):
    db.add(challenge)
    db.commit()
    db.refresh(challenge)
    return challenge