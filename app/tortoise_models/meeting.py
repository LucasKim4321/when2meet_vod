# from __future__ import annotations  # 임시로 import 에러 무효화

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meeting"

    @classmethod
    # async def create_meeting(cls, url_code: str) -> MeetingModel:  # MeetingModel정의가 아직 끝나지 않았기 때문에 에러남.
    async def create_meeting(cls, url_code: str) -> "MeetingModel":  # 쌍따옴표를 사용해 임시로 에러 해결.
        return await cls.create(url_code=url_code)


# Text : 길이가 길다. 인덱스 안됨.
# Varchar : 길이 제한, 인덱스 가능.
# mysql의 varcher는 255이하는 사용되는 크기가 같다.
# ch33 Tortoise-orm 설치 및 모델 생성
