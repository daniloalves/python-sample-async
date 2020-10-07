from time import sleep
import logging
import aiohttp
import asyncio

logger = logging.getLogger(__name__)

## Example to call:
# python3 ./app.py

async def main():
    # await asyncio.sleep(0.1)
    print({'status_code': 200, 'message': 'Your request received and in proccess..'})
    return 'ok'
    
async  def mock_answer(time=5):
    await asyncio.sleep(0.1)
    sleep(time)
    print(f"Finished your process in {time} seconds!")
    return 'ok'

loop = asyncio.get_event_loop()

tasks = [loop.create_task(mock_answer()),loop.create_task(main())]
wait_tasks = asyncio.wait(tasks)

loop.run_until_complete(wait_tasks)
loop.close()