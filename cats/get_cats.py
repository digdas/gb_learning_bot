import aiohttp

from config import UNSPLASH_ACCESS_KEY

# Функция для отправки запроса к Unsplash API и получения ссылки на изображение котика
async def get_cat_image() -> str:
    url = f"https://api.unsplash.com/photos/random/?query=cats&client_id={UNSPLASH_ACCESS_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            image_url = data["urls"]["regular"]
            return image_url
