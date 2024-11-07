#Pydantic - accepting only a subset of strings
from pydantic import BaseModel
from enum import Enum

class Languages(str, Enum):
    PY = "Python"
    JAVA = "Java"
    GO = "Go"

class Blog(BaseModel):
    title: str
    language: Languages = Languages.PY
    is_active: bool


blog = Blog(title="My first blog", language= "C++", is_active=True)
print(blog)

#Output: title='My first blog' Language=<Languages.PY: 'Python'> is_active=True
