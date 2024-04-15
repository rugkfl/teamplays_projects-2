from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class QnA(Document):
    ques_title: Optional[str] = None
    ques_writer: Optional[str] = None
    ques_content: Optional[str] = None
    ques_time: Optional[datetime] = None
    ques_answer: Optional[str] = None
    
  
    class Settings:
        name = "QnA"