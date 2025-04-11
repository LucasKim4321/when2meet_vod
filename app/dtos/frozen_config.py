from pydantic import ConfigDict

FROZEN_CONFIG = ConfigDict(frozen=True)

# frozen -> 얼어 있다.
# 얼어있는 객체 -> 생성 이후에는 변경할 수 없는 객체
# immutable

# my_set = frozenset()  # add() 불가능
# my_set = set()  # add() 가능
# my_set.add(1)
