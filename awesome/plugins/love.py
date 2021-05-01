from nonebot import on_command,on_startswith
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, Event, MessageSegment, Message

love = on_startswith(msg="love you", priority=4)


# 识别参数 并且给state 赋值


@love.handle()
async def love_rev(bot: Bot, event: Event, state: dict):
    await love.finish(message="love you too~", at_sender=True)

loves = on_startswith(msg="我爱你", priority=4)


# 识别参数 并且给state 赋值


@loves.handle()
async def loves_rev(bot: Bot, event: Event, state: dict):
    await loves.finish(message="我也爱你!mua~", at_sender=True)
