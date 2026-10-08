# import asyncio

# async def brew_chai():
#     print ("Brewing chai... ")
#     await asyncio.sleep(2) # here the await is not blocking the main thread it's a non blocking i/o operation
#     print("Chai is ready")

# asyncio.run(brew_chai())


# Another example ________________________________________________________________________________________________________



# import asyncio

# async def brew(name):
#     print(f"Brewing {name}")
#     await asyncio.sleep(2)
#     print(f"{name} is ready...")


# async def main():
#     await asyncio.gather(  # the gather function is used to run multiple async tasks concurrently and wait for all them to finish.
#         brew("Masala chai"),
#         brew("green chai"),
#         brew("Ginger chai")
#     )

# asyncio.run(main())


# Now ab iska result tujhe lg rha hoga total 6 seconds ke wait ke baad aayega 
# but actually it will come after 2 seconds because it is a non blocking operation on the main thread 



#Another  example _____________________________________________________________________________________________________________________


import asyncio
import aiohttp 


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"fetched{url} with status {response.status}")

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session: 
        # This creates an HTTP session.Think of the session as a connection manager for making HTTP requests.Instead of creating a completely new HTTP setup for every request:
        tasks = [fetch_url(session, url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())