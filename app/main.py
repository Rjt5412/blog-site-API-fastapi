from fastapi import FastAPI
from .routers import post, user, auth, vote

from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

# Commented since Alembic is now being used
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# * for now but ideally this would depend on use cases.
# Eg. if frontend is on a different domain then allow request only from that domain
# by mentioning it here.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World"}

