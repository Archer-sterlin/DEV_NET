from typing import List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestFormStrict
from .database import SessionLocal, engine
from .models import Base, Blog, User
from .schemas import Blog as blog_schema, ReturnUser, User as user_schema
from .schemas import ShowBlog



Base.metadata.create_all(bind=engine)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.post("/token")
async def token(form_data:OAuth2PasswordRequestFormStrict=Depends()):
    return {"auth_token":form_data.username + "token"}



@app.get("/")
async def root(token:str=Depends(oauth2_scheme)):
    return {"token":token}
 
@app.post('/blog', response_model=ShowBlog)
def create(request:blog_schema, db:Session=Depends(get_db)):
    blog = Blog(title=request.title, body=request.body)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


@app.post('/user', response_model=ReturnUser)
def create(request:user_schema, db:Session=Depends(get_db)):
    user = User(
        name=request.name, 
        email=request.email, 
        is_active=request.is_active,
        password=request.password,
        )
   
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.get('/blog', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def get_blogs( db:Session=Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@app.get('/blog/{blog_id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def get_blog( response:Response, blog_id:int,db:Session=Depends(get_db) ):
    blog = db.query(Blog).filter(Blog.id==blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id of {blog_id} not found")
    return blog 


@app.delete('/blog/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog( response:Response, blog_id:int, db:Session=Depends(get_db) ):
    blog = db.query(Blog).filter(Blog.id==blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"status":"success"}
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id of {blog_id} not found")


@app.put('/blog/{blog_id}', status_code=status.HTTP_202_ACCEPTED, response_model=ShowBlog)
def update_blog(request:blog_schema, blog_id:int, db:Session=Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id==blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {blog_id} not found")

    blog.update(dict(request), synchronize_session=False)
    db.commit()
    return blog
