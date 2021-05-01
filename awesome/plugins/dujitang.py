from nonebot import on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event
import requests
import json

weather = on_startswith("毒鸡汤", priority=2)


@weather.handle()
async def handle_first_receive(bot: Bot, event: Event, state: dict):
    se = await get_dujitang()
    await weather.finish(se)

async def get_dujitang():
    default_sentence="我没见过一个煤矿工人靠挖煤又快又多当上了煤老板。"
    url = "http://rainbow.ilibrary.me/api/rainbow/random"
    headers = {
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control" : "max-age=0",
        "Cookie" : "__gads=ID=2259474e6918a12c-223a528558c500b4:T=1608995008:RT=1608995008:S=ALNI_MYh2OIippuk5f3eJPNegsv62cABAg; UM_distinctid=1769f937360bc4-05f0488b1c204b-5a301e44-1fa400-1769f937361b5c",
        "Host" : "rainbow.ilibrary.me",
        "Proxy-Connection" : "keep-alive",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    sentence = "!"
    for i in range(0,10):
        res = requests.get(url,headers = headers)
        shit = json.loads(res.text)
        # print(type(shit))
#         print(shit.keys())
#         print(shit.values())
#         print(shit['sentence'])
        if "毒鸡汤" in res.text: 
            sentence = shit['sentence']
            break
    if sentence =="!":
        sentence = default_sentence
    return sentence