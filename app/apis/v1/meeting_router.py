from fastapi import APIRouter

from app.dtos.create_meeting_response import CreateMeetingResponse

edgedb_router = APIRouter(prefix="/v1/edgedb/meetings", tags=["Meeting"])
mysql_router = APIRouter(prefix="/v1/mysql/meetings", tags=["Meeting"])
# 원래는 어떤 db를 쓰는지 url에 적을 필요 없음.
# 실전에서는 db이름을 url에 넣지마세요!


@edgedb_router.post(
    path="",
    description="meeting을 생성합니다."
)
async def api_create_meeting_edgedb() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")

# controller =  view = path operation function
# 타입힌트로 리턴값을 정해주면 자동으로 swagger에도 표시됨.
@mysql_router.post(
    "",
    description="meeting을 생성합니다."
)
async def api_create_meeting_mysql() -> CreateMeetingResponse:
    return CreateMeetingResponse(url_code="abc")


