import re
from typing import Annotated

from fastapi import APIRouter, Path, Query, HTTPException

from app.api.v1.endpoints.image_search import search_images


router = APIRouter()
data = {}

TAGS = [
  ["유직", "무직"],
  ["활동", "휴식"],
  ["바쁨", "여유"],
  ["심심", "유흥", "지침", "귀가"],
  ["흥미", "화남", "행복", "속상", "신남", "허탈", "냉소", "지루", "사랑"],
  ["부자", "거지"]
]


@router.get("/{query}")
async def get_images(
        query: Annotated[str, Path(title="Decimal tags for image query")]
):
    validate_query(query)
    tags = convert_query(query)
    images = search_images(tags, data['df'])
    return {"imageNames": images}


def validate_query(query: str):
    if query is None:
        raise HTTPException(status_code=400, detail="Missing Parameters")
    if len(query) != 6:
        raise HTTPException(status_code=400, detail="Invalid Parameters")

    regex = re.findall('^[0-9]+$', query)

    if len(regex[0]) != 6:
        raise HTTPException(status_code=400, detail="Invalid Parameters")
    for idx, item in enumerate(regex[0]):
        if int(item) >= len(TAGS[idx]):
            raise HTTPException(status_code=400, detail="Invalid Parameters")


def convert_query(query: str):
    tags = []

    for idx, item in enumerate(query):
        tags.append(TAGS[idx][int(item)])

    return tags
