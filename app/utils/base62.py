import string
from typing import ClassVar, Final

# from typing import Final은 변경되지 않아야 할 "상수" 값을 선언할 때 사용하는 타입 힌트입니다.
# 즉, "이 변수는 값을 바꾸지 않을 거야!"라고 코드 상에서 명확히 의도를 표현할 수 있게 해줍니다.

# ClassVar는 클래스 변수임을 명시적으로 표현하는 타입 힌트입


class Base62:
    BASE: Final[ClassVar[str]] = string.ascii_letters + string.digits
    BASE_LEN: Final[ClassVar[int]] = len(BASE)

    # mypy 1.13.0 버전에서 이렇게 함.
    # BASE: Final[str] = string.ascii_letters + string.digits
    # BASE_LEN: Final[int] = len(BASE)
    # print(BASE_LEN)  # BASE의 길이는 62

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode() needs positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result: list[str] = []
        # result = ""  # 문자열은 '+' 사용해도 실제로는 지우고 새로 다시 만드는 작업을 하기 때문에 반복횠수가 많을 수록 손해

        # 0이면 False 나머지 숫자는 True
        while num:
            # divmod(a,b) a/b의 몪과 나머지를 동시에 구함.
            num, remainder = divmod(num, cls.BASE_LEN)
            # result.append(cls.BASE[remainder])
            result += cls.BASE[remainder]

        return "".join(result)


# print(Base62.encode(62))  # ab
# print(Base62.encode(124))  # ac
# print(Base62.encode(2))  # c

# print(uuid.uuid4().int)
# print(Base62.encode(uuid.uuid4().int))


# 디버그 하기
# 디버그 모드 클릭

# 디버깅할 라인에 좌측 줄번호 클릭하면 빨간색 원이 생김

# Step Over (n)	함수 안으로 들어가지 않고 다음 줄로 이동
# Step Into (s)	함수 안으로 들어감
# Step Out (r)	지금 함수 빠져나와서 호출한 쪽으로 감

# Evaluate expression
# 커맨드 엔터 / 실행됨
#
