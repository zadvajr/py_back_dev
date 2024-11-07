#Pydantic - Properties as Pydantic Models
from pydantic import BaseModel
# from typing import List 

class Comment(BaseModel):
    text: str = None

class Blog(BaseModel):
    title: str
    comment: list[Comment] = None
    is_active: bool

blog = Blog(title="Our first blog", comment=[{"text": "My comment"}, {"text":"Your comment"},], is_active=True)
print(blog)

# title='Our first blog' comment=[Comment(text='My comment'), Comment(text='Your comment')] is_active=True