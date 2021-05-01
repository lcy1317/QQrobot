# 补充说明

## 关于用户/群组

```python
event.user_id# 发消息人的id
event.group_id# 发消息群的id
event.sender.get("role")=="member/admin/owner"
event.sub_type == "friend/group/other"
event.__event__=="message.group/message.private"
#上面是消息类型，详情看F:\anaconda_\envs\bot\Lib\site-packages\nonebot\adapters\cqhttp里面的event.py
event.message#消息是啥
```

## nonebot包路径

F:\anaconda_\envs\bot\Lib\site-packages\nonebot

## API

### 彩虹屁

kuakua_url = "https://chp.shadiao.app/api.php?from=sunbelife"

### 骂人

maren_url = "https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn&from=sunbelife"

