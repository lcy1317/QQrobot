from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message
import random
 
love = on_startswith(msg="功能", priority=1)


# 识别参数 并且给state 赋值


@love.handle()
async def love_rev(bot: Bot, event: Event, state: dict):
        await love.finish(message="\n1.每日一句\n2.祖安/骂人\n3.夸夸\n4.人品\n5.舔狗日记\n6.土味情话\n7.网抑\n8.毒鸡汤\n9.查天气\n10.盛乐恒语录\n11.每日健康申报打卡，请私聊机器人发送健康申报查看详情", at_sender=True)