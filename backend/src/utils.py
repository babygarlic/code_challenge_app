from fastapi import HTTPException
from clerlk_backend_api import Clerk, AuthenticateRequestOptions
import os 
from dotenv import load_dotenv

load_dotenv()

clerk_sdk = Clerk( bearer_auth=os.getenv("CLERK_API_KEY") )

def authenticate_and_get_user(request):
    """
    Authenticate the user using Clerk and return the user object.
    """
    try:
        reques_state = clerk_sdk.authenticate_request(
            request,
            AuthenticateRequestOptions(
                authorized_parties=["http://localhost:5173","localhost:5173"],
                  jwt_key=os.getenv("JWT_KEY")  # Adjust this to your authorized parties
                )
            )
        if not request_state.is_signed_in:
            raise HTTPException(status_code=401, detail="Invalid token")
        user_id = request_state.payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="User ID not found in token")
        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    