from typing import NewType
from typeguard import typechecked

UserId = NewType('UserId', int)
PostId = NewType('PostId', int)

@typechecked
def greeting(name: str, userId: UserId) -> str:
  return 'Hello ' + name + " UserId:{userId}".format(userId=userId)

msg = greeting('tae', 'number')
print(msg)