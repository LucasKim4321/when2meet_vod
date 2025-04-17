from datetime import datetime

from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from app.dtos.create_meeting_response import CreateMeetingResponse
from app.dtos.get_meeting_response import GetMeetingResponse
from app.dtos.update_meeting_request import UpdateMeetingDateRangeRequest
from app.services.meeting_service_mysql import (
    service_create_meeting_mysql,
    service_get_meeting_mysql,
)

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 db를 쓰는지 url에 적을 필요 없음.
# 실전에서는 db이름을 url에 넣지마세요!


# @edgedb_router.post(path="", description="meeting을 생성합니다.")
# async def api_create_meeting_edgedb() -> CreateMeetingResponse:
#     return CreateMeetingResponse(url_code="abc")


# controller =  view = path operation function
# 타입힌트로 리턴값을 정해주면 자동으로 swagger에도 표시됨.
@mysql_router.post("", description="meeting을 생성합니다.")
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code=(await service_create_meeting_mysql()).url_code)


# @edgedb_router.get(
#     "/{meeting_url_code}",  # path variable
#     description="meeting 을 조회합니다.",
# )
# async def api_get_meeting_edgedb(meeting_url_code: str) -> GetMeetingResponse:
#     return GetMeetingResponse(url_code="abc")

# @mysql_router.get(
#     "/{meeting_url_code}",  # path variable
#     description="meeting 을 조회합니다.",
# )
# async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
#     return GetMeetingResponse(url_code="abc")


@mysql_router.get(
    "/{meeting_url_code}",  # path variable
    description="meeting 을 조회합니다.",
)
async def api_get_meeting_mysql(meeting_url_code: str) -> GetMeetingResponse:
    meeting = await service_get_meeting_mysql(meeting_url_code)
    if meeting is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail=f"meeting with url_code: {meeting_url_code} not found"
        )
    return GetMeetingResponse(
        url_code=meeting.url_code,
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )


# @edgedb_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
# async def api_update_meeting_date_range_edgedb(
#     meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
# ) -> GetMeetingResponse:
#     return GetMeetingResponse(
#         url_code="abc",
#         start_date=datetime.now().date(),
#         end_date=datetime.now().date(),
#         title="test",
#         location="test",
#     )


@mysql_router.patch("/{meeting_url_code}/date_range", description="meeting 의 날짜 range 를 설정합니다.")
async def api_update_meeting_date_range_mysql(
    meeting_url_code: str, update_meeting_date_range_request: UpdateMeetingDateRangeRequest
) -> GetMeetingResponse:

    # mypy를 디버깅할 때 reveal_type 사용가능. import x
    # reveal_type(GetMeetingResponse().start_date)
    # mypy .  테스트시
    # Revealed type is "Union[datetime.date, None]" 이런식으로 결과가 나옴

    return GetMeetingResponse(
        url_code="abc",
        start_date=datetime.now().date(),
        end_date=datetime.now().date(),
        title="test",
        location="test",
    )
