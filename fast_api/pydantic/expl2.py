#Accepting optional values
from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    # description: str = None will also work
    is_active: bool

blog = Blog(title="My first blog", is_active=True)
print(blog)

#Output: title='My first blog' description=None is_active=True