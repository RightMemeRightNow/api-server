import re
from typing import Annotated

import pandas as pd
from fastapi import FastAPI, Path, Query, HTTPException

app = FastAPI()
data = {}
TAGS = [
  ["유직", "무직"],
  ["활동", "휴식"],
  ["바쁨", "여유"],
  ["심심", "유흥", "지침", "귀가"],
  ["흥미", "화남", "행복", "사랑", "신남" ,"허탈", "냉소", "지루", "속상"],
  ["거지", "부자"]
]


@app.on_event('startup')
def init_data():
    df = pd.read_csv('images.csv')
    data["df"] = df


@app.get("/api/images/{query}")
async def root(
        query: Annotated[str, Path(title="Decimal tags for image query")],
        q: Annotated[str | None, Query(alias="item-query")] = None,
):
    validate_query(query)
    return {"imageNames": convert_query(query)}


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
