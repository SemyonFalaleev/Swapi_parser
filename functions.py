import asyncio
import aiohttp
from models import init_orm, close_orm, DbSession, SwapiPeople
import json
from serializer import serializer

async def get_count_people(http_session):
    response = await http_session.get(f"https://swapi.dev/api/people/")
    json_data = await response.json()
    count = json_data.get("count")
    return count

async def get_people(http_session, people_id):
    response = await http_session.get(f"https://swapi.dev/api/people/{people_id}/")
    json_data = await response.json()
    return json_data

async def insert_db(json_data):
    async with DbSession() as db:
        orm_obj = [serializer(data) for data in json_data]
        db.add_all(orm_obj)
        await db.commit()

