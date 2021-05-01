import requests
from nonebot import on_command,on_startswith,on_keyword
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
 
#wyy = on_startswith("网抑", priority=3)
wyy = on_keyword("网抑", priority=3)

# 识别参数 并且给state 赋值


@wyy.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    tiangoudiary = await get_soil_sentence()
    await wyy.finish(tiangoudiary)

async def get_soil_sentence():
    url = 'https://v1.hitokoto.cn/'
    par = {"c":"j"}
    res = requests.get(url,params=par)
    result= res.json()
    content_s = result['hitokoto']
    return content_s