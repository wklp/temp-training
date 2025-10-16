import asyncio
import random

async def fetch_image(image_name):
    print(f"Fetching {image_name}...")
    await asyncio.sleep(random.randint(1,3))
    print(f"✅ {image_name} downloded!")

async def main():
    
    await asyncio.gather(
        fetch_image("cat.jpg"),
        fetch_image("dog.png"),
        fetch_image("sunset.jpeg"),
        fetch_image("mountains.webp"),
        fetch_image("robot.svg")
        )
        
asyncio.run(main())