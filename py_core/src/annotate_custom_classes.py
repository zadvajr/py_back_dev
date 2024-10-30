"""Annotate custome classes"""
from typing import Optional, List

class Job:
    "Job class object"
    def __init__(self, title: str, description: Optional[str]) -> None:
        self.title = title
        self.description = description
    def __repr__(self):
        return self.title

job1 = Job("Software Engineer", "To build scalable software solutions")
job2 = Job("Junior Developer", "To Assist Software Engineer")

jobs: List[Job] = [job1, job2]
print(jobs)
print(type(jobs))
