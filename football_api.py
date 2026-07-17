import os
import aiohttp


API_KEY = os.getenv("FOOTBALL_API_KEY")

BASE_URL = "https://v3.football.api-sports.io"


async def get_fixtures():
    headers = {
        "x-apisports-key": API_KEY
    }

    url = f"{BASE_URL}/fixtures"

    params = {
        "date": "2026-07-17"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            headers=headers,
            params=params
        ) as response:

            data = await response.json()

            return data
