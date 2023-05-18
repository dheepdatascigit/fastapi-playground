from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from msal import ConfidentialClientApplication
from jose import jwt, JWTError
import requests

app = FastAPI()

# Azure AD B2B configurations
CLIENT_ID = "<your-client-id>"
CLIENT_SECRET = "<your-client-secret>"
TENANT_ID = "<your-tenant-id>"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_token_header(token):
    return {"Authorization": f"Bearer {token}"}

def decode_token(token):
    header = jwt.get_unverified_header(token)
    jwk_url = f"{AUTHORITY}/v2.0/.well-known/openid-configuration"
    jwk_response = requests.get(jwk_url)
    jwks = jwk_response.json()["jwks_uri"]
    jwk_response = requests.get(jwks)
    key = next(
        iter(
            [k for k in jwk_response.json()["keys"] if k["kid"] == header["kid"]]
        )
    )
    rsa_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(key))
    payload = jwt.decode(
        token,
        rsa_key,
        algorithms=["RS256"],
        audience=CLIENT_ID,
        issuer=AUTHORITY,
    )
    return payload

# Initialize MSAL client application
msal_app = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=AUTHORITY,
)

def validate_access_token(token: str):
    try:
        # Verify the token signature and decode the payload
        payload = decode_token(token)
        
        # Perform additional validation checks based on your requirements
        # Example checks:
        
        # Check if the token is expired
        now = datetime.utcnow()
        if now > datetime.fromtimestamp(payload["exp"]):
            raise HTTPException(status_code=401, detail="Token expired")
        
        # Check if the token was issued in the future (clock skew)
        if now < datetime.fromtimestamp(payload["iat"]):
            raise HTTPException(status_code=401, detail="Invalid token")
        
        # Check if the token is intended for this application
        if payload["aud"] != CLIENT_ID:
            raise HTTPException(status_code=401, detail="Invalid audience")
        
        # Add additional checks as per your requirements
        
        return payload
        
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token")

# Route to validate access token
@app.get("/validate-token")
def validate_token(token: str = Depends(oauth2_scheme)):
    payload = validate_access_token(token)
    return {"valid": True, "username": payload["sub"]}

# Example protected route
@app.get("/protected")
def protected_route(token: str = Depends(oauth2_scheme)):
    payload = validate_access_token(token)
    return {"message": "Access granted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
