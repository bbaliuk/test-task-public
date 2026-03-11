from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class Category(BaseModel):
    id: int
    name: str


class Tag(BaseModel):
    id: int
    name: str


class PetPayload(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    id: int
    category: Category
    name: str
    photo_urls: List[str] = Field(alias="photoUrls")
    tags: List[Tag]
    status: str


class PetPostPayload(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )

    pet_id: Optional[int] = Field(alias="petId")
    name: Optional[str]
    status: Optional[str]
