#Pydantic is useful for data validation and type hints
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    is_active: bool


blog = Blog(title="My first blog", is_active=True)
print(blog)