# from typing import Final은 변경되지 않아야 할 "상수" 값을 선언할 때 사용하는 타입 힌트입니다.
# 즉, "이 변수는 값을 바꾸지 않을 거야!"라고 코드 상에서 명확히 의도를 표현할 수 있게 해줍니다.

# abc = "hihi"
# abc = "hello"
# print(abc)

# mypy로 테스트시 재할당 되지 말아야할 값이 재할당 되서 오류남.
# abc2: Final[str] = "hihi"
# abc2 = "hello"
# print(abc2)


# 리스트는 재할당 되는 것이 아니라 내부 상태가 달라지는 것이라 괜찮음.
# abc3: Final[list[str]] = ["a", "b"]
# abc3.append("c")
# print(abc3)
