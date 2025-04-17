from datetime import date, timedelta

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

MEETING_DATE_MAX_RANGE = timedelta(days=62)  # 62일을 초과하는지 비교할 때 사용

# 클라이언트가 보낸 요청(Request Body)의 데이터를 받고 검증하는 역할
class UpdateMeetingDateRangeRequest(BaseModel):
    model_config = FROZEN_CONFIG  # 한번 생성하면 재할당 되지 않도록 FROZEN_CONFIG 설정
    start_date: date
    end_date: date

    def exceeds_max_range(self) -> bool:
        return self.end_date - self.start_date > MEETING_DATE_MAX_RANGE  # 기간을 초과하는지 검증


class UpdateMeetingTitleRequest(BaseModel):
    model_config = FROZEN_CONFIG  # 한번 생성하면 재할당 되지 않도록 FROZEN_CONFIG 설정
    title: str


class UpdateMeetingLocationRequest(BaseModel):
    model_config = FROZEN_CONFIG  # 한번 생성하면 재할당 되지 않도록 FROZEN_CONFIG 설정
    location: str
