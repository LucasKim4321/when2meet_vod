from app.configs.base_config import Config


def get_config() -> Config:
    # 보통은 노란줄이나 빨간줄 생기면 무시하면 안됨.
    # 하지만 이건 테스트도 잘 되고 실제로도 동작하기 때문에 괜찮음.
    return Config(_env_file=".env", _env_file_encoding="utf-8")


config = get_config()

print(config.ENV)
