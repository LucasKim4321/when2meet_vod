from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.apis.v1.meeting_router import edgedb_router as meeting_edgedb_router
from app.apis.v1.meeting_router import mysql_router as meeting_mysql_router

app = FastAPI(
    default_response_class=ORJSONResponse,
)

app.include_router(meeting_edgedb_router)
app.include_router(meeting_mysql_router)

# print("나는 app/__init__ 이야", __name__)
# if __name__ == "__main__":
#     import asgi
