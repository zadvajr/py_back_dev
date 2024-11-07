#Pydantic - getting dynamic values at runtime
from pydantic import BaseModel, Field
from datetime import datetime
import time

class Blog(BaseModel):
    title: str
    created_at: datetime = Field(default_factory=datetime.now)
    is_active: bool


print(Blog(title="My first blog", is_active=True))
time.sleep(3)

print(Blog(title="My second blog", is_active=True))

#Outputs:
# title='My first blog' created_at=datetime.datetime(2024, 11, 7, 22, 56, 55, 376246) is_active=True
# title='My second blog' created_at=datetime.datetime(2024, 11, 7, 22, 56, 58, 376645) is_active=True