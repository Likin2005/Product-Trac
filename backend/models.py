from pydantic import BaseModel, Field

class Product(BaseModel):
    id : int
    name : str
    description : str
    price : float = Field(ge=1)
    quantity : int = Field(ge=1)