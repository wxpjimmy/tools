from fastapi import FastAPI, Request
from azure.identity import AzureCliCredential


app = FastAPI()
credential: AzureCliCredential = None

@app.on_event("startup")
async def startup_event():
    global credential
    credential = AzureCliCredential()
    print("Token Provider is starting up")


@app.get("/token")
async def get_token(request: Request):
    resource = request.query_params.get("resource")
    if not resource:
        resource = "https://management.azure.com/"
    identity_header = request.headers.get("X-IDENTITY-HEADER")
    if identity_header != "test":
        print(f"Wrong identity header: {identity_header}, expected: test")
    global credential
    token = credential.get_token(resource)
    return {"access_token": token.token, "expires_on": token.expires_on, "resource": resource}
