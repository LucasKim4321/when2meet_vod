import random
import timeit
import uuid
from datetime import datetime
from typing import Sequence

from sqids import sqids

from app.utils.base62 import Base62

squid = sqids.Sqids()

class Squids:

    @classmethod
    # def encode(cls, nums: list[int]) -> str:
    def encode(cls, nums: Sequence[int]) -> str:  # 시퀸스 자료형으로 하면 리스트, 튜플 둘 다 받아진다.
        return squid.encode(nums)

def do_squids():
    now = datetime.now()
    return Squids.encode(
        [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1,9)]
    )

def  do_base62():
    uu = uuid.uuid4()
    return Base62.encode(uu.int)

if __name__ == "__main__":
    # print(do_squids())
    # print(do_base62())

    # sqids가 base62에 비해 많이 느리지만 기능은 좀 더 있을 수 있음.
    print(timeit.timeit(lambda: do_squids(), number=10000))
    print(timeit.timeit(lambda: do_base62(), number=10000))


# print(Squids.encode([1,2]))
# print(Squids.encode((1,2)))

# uuid.uuid4().int는 128비트 정수
# 하지만 sqids.encode()는 64비트까지만 지원
# print(Squids.encode([uuid.uuid4().int]))

