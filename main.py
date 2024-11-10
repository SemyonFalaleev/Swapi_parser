import asyncio
import aiohttp
from models import init_orm, close_orm 
from functions import get_people, insert_db, get_count_people
from more_itertools import chunked

async def main():
    await init_orm()
    async with aiohttp.ClientSession() as session:
        count = await get_count_people(session)
        for chunk_i in chunked(range(1, count+1), n = 25):
            coros = [get_people(session, i) for i in chunk_i]
            result = await asyncio.gather(*coros)
            asyncio.create_task(insert_db(result))
    main_coro = asyncio.current_task()
    tasks = asyncio.all_tasks()
    tasks.remove(main_coro)
    await asyncio.gather(*tasks)
    await close_orm()

if __name__ == "__main__":
    asyncio.run(main())








