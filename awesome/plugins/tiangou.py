import requests
from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
 
tiangou = on_startswith("舔狗日记", priority=3)
#love = on_keyword("土味情话",priority=3)

# 识别参数 并且给state 赋值


@tiangou.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    tiangoudiary = await get_soil_sentence()
    await tiangou.finish(tiangoudiary)

async def get_soil_sentence():
    res = requests.get('https://v1.alapi.cn/api/dog?format=text')
    sentence = res.text
    return sentence