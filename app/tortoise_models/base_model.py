from tortoise import fields


class BaseModel:
    id = fields.BigIntField(primary_key=True)
    created_at = fields.DatetimeField(auto_now_add=True)


# MySQL : primary key를 정할 때 주의해야 되는 점
# MySQL version 8 이상 부터라면 (5.7 부터도 쓰긴함)
# innodb가 default engine (옛날 MyISAM)

# innodb의 특징 중 하나 ->  clustering index
# primary key를 기준으로
# primary key값이 비슷한 row들끼리 disk에서도 실제로 모여있음.

# HDD
# 랜덤 IO가 느리고, 순차 IO가 빠르다.

# SSD
# 순차 IO가 좀 더 빠르지만 랜덤 IO도 빠름.

# 그냥 int가 아니라, 비즈니스 작 의미가 있고
# 계속해서 증가하는 어떤 갑으로 설정하면
# 굉장히 빠르게 읽을 수 있습니다.

# int의 최대값 21억이지만 이걸 넘어서 사용하게 될 수도 있어서 bigint사용
