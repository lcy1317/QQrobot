from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
love = on_startswith(msg="人品", priority=2)


# 识别参数 并且给state 赋值


@love.handle()
async def love_rev(bot: Bot, event: Event, state: dict):
    seed = random.randint(0,100)
    if (event.user_id==1157340882): seed = random.randint(90,100)
    if (event.user_id==1710314742): seed = random.randint(90,100)
    await love.finish(message="你的人品值是"+str(seed), at_sender=True)