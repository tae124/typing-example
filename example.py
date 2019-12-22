from typing import NewType

UserId = NewType('UserId', int)
PostId = NewType('PostId', int)

def greeting(name: str, userId: UserId) -> str:
    return 'Hello ' + name + " UserId:{userId}".format(userId=userId)

msg = greeting('tae', PostId(10))
print(msg)