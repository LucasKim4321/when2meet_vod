from fastapi import FastAPI

app = FastAPI()

# int, str, bool
# dict, set, list, tuple -> collection

@app.get("/")
async def root() -> dict[str,str]:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str,str]:
    return {"message": f"Hello {name}"}


# uvicorn main:app --reload 명령으로 서버 실행

# main: 파일 main.py (파이썬 "모듈").
# app: main.py 내부의 app = FastAPI() 줄에서 생성한 오브젝트.
# --reload: 코드 변경 시 자동으로 서버 재시작. 개발 시에만 사용.