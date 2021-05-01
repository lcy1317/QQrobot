from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
import os

weather = on_command("打卡", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="请输入一卡通+密码格式如：213181111 xxxxxxxx")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    if (len(city)>10):
        city = 'python report.py '+city
        os.system(city)
    else:
        await weather.finish("你的输入好像有些问题哦~")
        return
    await weather.finish("我有努力帮你打卡去哦，只要你的账号密码是对滴！")
