from typing import Optional
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict
from pydantic import BaseModel



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


class Blog(BaseModel):
    title:str
    body:str
    is_published:Optional[bool]

app = FastAPI()


@app.post("/token")
async def token(form_data:OAuth2PasswordRequestFormStrict=Depends()):
    return {"auth_token":form_data.username + "token"}



@app.get("/")
async def root(token:str=Depends(oauth2_scheme)):
    return {"token":token}


@app.post("/blog")
async def create_blog(blog:Blog):
    return {"blog":{
        "title":blog.title,
        "body":blog.body,
    }}

