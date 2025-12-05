import random
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = 0


my_posts = [
    {
        "title": "I like pizza!!!!",
        "content": "I really love pizza, especially pepperoni, it's the best!",
        "published": True,
        "rating": 5,
        "id": 1,
    },
    {
        "title": "look at my new car",
        "content": "I just bought a new car, it's a red convertible!",
        "published": False,
        "id": 2,
    },
    {
        "title": "testing this social media app",
        "content": "",
        "published": True,
        "rating": 3,
        "id": 3,
    }
]


@app.get("/")
async def root():
    return {"message": "landing page"}


@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_post(post: Post):
    id : int = random.randint(1, 10000000000)
    post_dict = post.model_dump()
    post_dict["id"] = id
    my_posts.append(post_dict)
    return {"data": post}


@app.get("/posts/{id}")
async def get_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return {"post_detail": post}
    return {"message": "post not found"}