from typing import Annotated

from pydantic import BaseModel, Field

from app.dtos.frozen_config import FROZEN_CONFIG


# DTO : data 를 “전달”하기 위한 목적으로 생성한 객체
class CreateMeetingResponse(BaseModel):

    # 클래스를 한번 생성하고 나면 클래스가 더 이상 변경되지 않음.
    model_config = FROZEN_CONFIG

    # json형태로 응답해줄 key값 추가
    # 필드에 examples 추가시 examples=["example01"])]  # Swagger UI에서 이 필드를 볼 때, 아래처럼 입력 예시로 "example01"이 표시
    url_code: Annotated[
        str,
        Field(
            description="미팅 url 코드. unique 합니다.",
        ),
    ]  # description 설명 작성
