import asyncio
import os
import sys


@command(pattern="^.restart", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    asyncio.get_event_loop().create_task(restart())
    os.execl(sys.executable, sys.executable, *sys.argv)


@command(pattern="^.shutdown", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    asyncio.get_event_loop().create_task(shutdown())


async def restart():
    await bot.disconnect()
    await event.edit("Restarting. `.ping` me or `.helpme` in a few minutes to check if I am online")

async def shutdown():
    await bot.disconnect()
    await event.edit("Turning off ...Manually turn me on later")
