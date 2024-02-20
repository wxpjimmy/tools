# AAD Token provider for local test

## install dependencies
pip install fastapi   
pip install "uvicorn[standard]"

## start local token bridger
uvicorn token_provider:app --reload

## environment variables to set
IDENTITY_ENDPOINT=http://host.docker.internal:8000/token   
IDENTITY_HEADER=test