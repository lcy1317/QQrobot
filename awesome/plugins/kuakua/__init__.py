from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
from . import data
love = on_startswith(msg="夸", priority=2)
import requests


# 识别参数 并且给state 赋值


@love.handle()
async def love_rev(bot: Bot, event: Event, state: dict):
    res = requests.get("https://chp.shadiao.app/api.php?from=sunbelife")
    await love.finish(message = res.text, at_sender = True)
#    seed = random.randint(0,len(data.kuakua)-1)
#    await love.finish(message=data.kuakua[seed], at_sender=True)