from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import requests
import json

weather = on_command("查天气", priority=5)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    args = str(event.message).strip()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if args:
        state["city"] = args  # 如果用户发送了参数则直接赋值


@weather.got("city", prompt="你想查询哪个城市的天气呢？")
async def handle_city(bot: Bot, event: Event, state: dict):
    city = state["city"]
    # if city not in ["上海", "北京"]:
    #     await weather.reject("你想查询的城市暂不支持，请重新输入！")
    city_weather = await get_weather(city)
    await weather.finish(city_weather)


async def get_weather(city: str):
    url = 'https://api.seniverse.com/v3/weather/now.json'
    r= requests.get(url, params={
        'key': 'SUnODibZ4s-9IQy-P',
        'location': city,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=1)
    res = r.json()
    tot=""
    res=r.json()
    content_s = res['results']
    a=content_s[0]
    tot=tot+"地点："+a['location']['name']+"\n"
    tot=tot+"时区："+a['location']['timezone']+"\n"
    tot=tot+"天气："+a['now']['text']+"\n"
    tot=tot+"温度："+a['now']['temperature']+"摄氏度\n"
    tot=tot+"最近更新时间："+a['last_update']   
    return tot