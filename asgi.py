from app import app

# print("나는 asgi.py야", __name__)

# main하고 자동완성 기능을 사용하면 만들어줌.
# 파이참의 라이브 템플릿 기능
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

# poetry add orjson

# 파일메뉴 클릭 런 으로 해당 파일을 실행
# 혹은 컨트롤 시프트 r로 해당 파일을 실행

# 커맨드 시프트 n  스크래치 파일 생성

# Swagger UI   http://localhost:8000/docs    대화형 API 문서 (기본 제공)
# ReDoc        http://localhost:8000/redoc   깔끔한 스타일의 API 문서
