from typing import Optional

from fastapi import FastAPI
from nba_api.stats.endpoints import boxscoreadvancedv2

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def items():
    return {"items": [f"item_{i: 02}" for i in range(20)]}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/boxscore")
async def get_boxscore():
    a = boxscoreadvancedv2.BoxScoreAdvancedV2(game_id="0042200311").get_normalized_dict()
    return {"boxscore": a}
    
