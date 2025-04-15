# from app.configs import config
#
# pydantic의 기능
# 현재 폴더를 기준으로 .env가 있으면 읽고 없으면 기본값을 불러옴.
# .env에 ENV="invalid" 이렇게 변수가 선언되어 있는데.
# config에 미리 정의한 enum env의 값으로 'local', 'stage', 'prod' 이렇게 정해져있기 때문에
# ENV 값이 invalid이렇게 되어 있으면 에러가 난다.
#
# print(config.ENV)
