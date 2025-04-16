import httpx
from starlette.status import HTTP_200_OK
from tortoise.contrib.test import TestCase

from app import app
from app.tortoise_models.meeting import MeetingModel


class TestMeetingRouter(TestCase):
    async def test_api_create_meeting_mysql(self) -> None:  # 모든 테스트는 None을 반환하는게 정석
        # Given When Then 구조에서 Given은 자동생성되기 때문에 Given 생략

        # When
        # AsyncClient는 async연산이 필요해서 async를 사용
        # async로 열면 async로 닫아야함.
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=app),
            base_url="http://test",
        ) as client:
            response = await client.post("/v1/mysql/meetings")

        response.raise_for_status()  #  응답 코드가 에러일 경우 예외(Exception)를 발생시키는 함수

        # Then: 테스트 결과를 검증
        # API 테스트에서 응답이 성공했는지(200 OK)를 확인하는 코드
        assert response.status_code == HTTP_200_OK  # 여기까지만 하면 실제로 데이터가 생성됬는지 검증이 안됨.
        # API 테스트 성공 후 데이터 변환을 시도함. API 테스트 전에 시도하면 잘못된 오류코드로 혼란을 유도함.
        url_code = response.json()["url_code"]
        assert (await MeetingModel.filter(url_code=url_code).exists()) is True


# FastAPI는 ASGI인터페이스를 구현함.
# ASGI 규칙대로 호출하면 실제로 http요청을 하지 않아도 마치 http요청을 한것처럼 처리
# ASGITransport() : ASGI 규칙대로 호출
#
# SGI란?
# ASGI (Asynchronous Server Gateway Interface)
# Python에서 비동기 웹 애플리케이션을 위한 표준 인터페이스입니다.
#
# WSGI의 업그레이드 버전입니다.
# FastAPI, Django Channels, Starlette, uvicorn 등에서 사용됩니다.

# 구분        WSGI                              ASGI
# 대상        동기 웹 앱 (Flask, Django 기본)      비동기 웹 앱 (FastAPI, Django Channels 등)
# 처리 방식    하나의 요청 처리 후 다음 요청           여러 요청을 비동기로 동시에 처리 가능
# 예         Flask, Django (기본)               FastAPI, Django Channels, Starlette
# 병렬성      제한적                              ✅ 웹소켓/HTTP/백그라운드 작업 가능

# 사용 상황                                     ASGI가 필요한가?
# 일반 웹사이트 (블로그, 쇼핑몰 등)                  ❌ 보통 WSGI로 충분
# 웹소켓, 실시간 채팅, 알림                        ✅ ASGI 필요
# FastAPI 사용 시                              ✅ ASGI 필요
# Django에서 Django Channels로 WebSocket 쓸 때  ✅ ASGI 필요

# await란?
# await는 비동기 함수 (async def) 안에서만 사용할 수 있는 키워드로,
# 다른 비동기 함수의 실행이 끝날 때까지 기다리는 역할을 합니다.

# HTTP는 다양한 응답을 주고 받을 수 있다.

# with (Context Manager)(컨텍스트 관리자)
# 리소스를 열고 닫는 과정을 자동으로 관리해주는 매우 강력한 문법입니다.
# 작업이 끝났을 때 자동으로 작업을 종료 close()를 시켜줌.
# 작업이 끝났을 때 작업을 종료 close()를 하지 않으면 다른 프로그램이 접근 할 수 없음.
#
# 대표적인 리소스 예시
# 리소스 종류           예시                                                 설명
# 파일                open("file.txt")                                     파일 핸들 (읽기/쓰기 후 닫아야 함)
# 네트워크 연결         requests.Session(), socket, FTP                      연결 후 종료해야 함
# 데이터베이스          connection.cursor()                                  커서 열고 닫기 필요
# 스레드 락            threading.Lock()                                     락 획득 후 해제 필요
# 입출력 장치           serial.Serial(), camera.open()                      장치 연결/해제
# 로그                logging에서 FileHandler, StreamHandler
# 가상 환경 / 세션      Django request, Flask context, transaction.atomic()
# 임시 파일/디렉터리     tempfile.NamedTemporaryFile()
# WebDriver          selenium.webdriver.Chrome()                          브라우저 열고 닫기
