from pydantic import BaseModel, Field, ConfigDict
from typing import List


class CategoryResponse(BaseModel):
    id: int
    name: str


class TagResponse(BaseModel):
    id: int
    name: str


class PetResponse(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    category: CategoryResponse
    name: str
    photo_urls: List[str] = Field(alias="photoUrls")
    tags: List[TagResponse]
    status: str


class UpdatePetResponse(BaseModel):
    code: int
    type: str
    message: str
