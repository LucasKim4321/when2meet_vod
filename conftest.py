import asyncio
from typing import Any, Generator
from unittest.mock import Mock, patch

import pytest
from _pytest.fixtures import FixtureRequest
from tortoise import generate_config
from tortoise.contrib.test import finalizer, initializer

from app.configs import config
from app.configs.tortoise_config import TORTOISE_APP_MODELS

TEST_BASE_URL = "http://test"
TEST_DB_LABEL = "models"  # 테스트할 DB model
TEST_DB_TZ = "Asia/Seoul"  # 타임존 설정


def get_test_db_config() -> dict[str, Any]:
    tortoise_config = generate_config(
        db_url=f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/test",
        app_modules={TEST_DB_LABEL: TORTOISE_APP_MODELS},
        connection_label=TEST_DB_LABEL,
        testing=True,  # testDB 자동 생성해줌
    )
    tortoise_config["timezone"] = TEST_DB_TZ

    return tortoise_config


# autouse가 활성화 되어 있으면 테스트 함수를 사용하지 않고도 fixture가 생성됨.
@pytest.fixture(scope="session", autouse=True)
def initialize(request: FixtureRequest) -> Generator[None, None]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # Mocking은 실제 의존성을 대체할 가짜 객체를 만들어서 테스트를 수행하는 것
    with patch("tortoise.contrib.test.getDBConfig", Mock(return_value=get_test_db_config())):
        initializer(modules=TORTOISE_APP_MODELS)  # 커맨드 p 눌러보면 인자가 보임
    yield  # 종료될 때 호출됨.
    finalizer()  # yield가 없는 일반 fixture는 테스트가 처음 시작할 때 한번호출되고 종료될 때 호출안됨.
    loop.close()

    pass


# 테스트 함수에서 fixture 이름을 인자로 받으면 initialize를 가동시킴
# def test_func(initialize):
#     pass
