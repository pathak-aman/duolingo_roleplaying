from pydantic import BaseModel

class Sceanrio_Desc(BaseModel):
    description : str
    first_dialog : str
