import asyncio 
import logging

logging.basicConfig(level=logging.INFO)

async def fetch_user(user_id: int) -> dict:
    try:
        if user_id == 0:
            raise ValueError("User not found!")
        await asyncio.sleep(1)  # Simulate network delay
        logging.info({"user_id": user_id, "name": "abdullah"})
    except Exception as e:
        logging.error(f"❌ Error: {e} , user_id: {user_id}")
        return {"user_id": user_id, "error": str(e)}
async def main():
    tasks = [
        fetch_user(1),
        fetch_user(2),  
        fetch_user(0)  # This will raise an error
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())