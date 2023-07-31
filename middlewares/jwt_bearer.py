from fastapi.security import HTTPBearer
from utils.jwt_manger import create_token, verify_token
from fastapi import FastAPI, HTTPException, Body, Path, Query, Request

class JWTBarer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = verify_token(auth.credentials)
        if data is None:
            raise HTTPException(status_code=401, detail="Invalid token")