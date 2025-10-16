import asyncio

async def download_file(file_name):
    print(f"Downloading {file_name}...")
    await asyncio.sleep(1.5)
    print(f"Done downloading {file_name}!")

async def main():
    await asyncio.gather(
        download_file("file1.pdf"),
        download_file("file2.pdf"),
        download_file("file3.mp3")
        
        )
        
asyncio.run(main())