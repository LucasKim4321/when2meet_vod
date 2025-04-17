from datetime import date

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

# 클라이언트에게 응답할 때의 데이터 구조를 정의
class GetMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG  # 한번 생성하면 재할당 되지 않도록 FROZEN_CONFIG 설정

    url_code: str
    start_date: date | None = None
    end_date: date | None = None
    title: str
    location: str
