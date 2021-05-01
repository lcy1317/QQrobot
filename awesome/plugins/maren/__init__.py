from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
from . import data
from . import namelist
love = on_startswith(msg="骂人", priority=2)
zuan = on_startswith(msg="祖安", priority=2)
import requests

# 识别参数 并且给state 赋值


@love.handle()
async def love_rev(bot: Bot, event: Event, state: dict):
    #print(event.__event__,type(event))
    if (event.__event__=="message.group"):
        if (event.group_id in namelist.black_list_group): return
        if (namelist.white_list_group_on and event.group_id not in namelist.white_list_group): return
    elif (event.__event__=="message.private"):
        if (event.user_id in namelist.black_list_private): return
        if (namelist.white_list_private_on and event.user_id not in namelist.white_list_private): return
    else:
        pass
    res = requests.get("https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn&from=sunbelife")
    await love.finish(message = res.text)
#    seed = random.randint(0,len(data.kuakua)-1)
#    await love.finish(message=data.kuakua[seed], at_sender=True)

@zuan.handle()
async def zuan_rev(bot: Bot, event: Event, state: dict):
    if (event.__event__=="message.group"):
        if (event.group_id in namelist.black_list_group): return
        if (namelist.white_list_group_on and event.group_id not in namelist.white_list_group): return
    elif (event.__event__=="message.private"):
        if (event.user_id in namelist.black_list_private): return
        if (namelist.white_list_private_on and event.user_id not in namelist.white_list_private): return
    else:
        pass
    res = requests.get("https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn&from=sunbelife")
    await love.finish(message = res.text)
    # seed = random.randint(0,len(data.kuakua)-1)
    # await zuan.finish(message=data.kuakua[seed], at_sender=True)