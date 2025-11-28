from typing import Optional, Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field(default="BizBot")
    app_env: str = Field(default="dev")
    app_host: str = Field(default="0.0.0.0")
    app_port: int = Field(default=80)

    premium_api_key: str = Field(default="change-me-very-secret")

    public_rate_limit_per_min: int = Field(default=60)
    premium_rate_limit_per_min: int = Field(default=300)

    cache_backend: Literal["memory", "redis"] = Field(default="memory")
    cache_ttl_seconds: int = Field(default=600)
    cache_max_items: int = Field(default=256)
    redis_url: str = Field(default="redis://localhost:6379/0")

    llm_provider: Literal["OPENAI", "HF"] = Field(default="OPENAI")
    openai_api_key: Optional[str] = None
    openai_model: str = Field(default="gpt-4o-mini")
    hf_api_token: Optional[str] = None
    hf_model: str = Field(default="mistralai/Mistral-7B-Instruct-v0.3")

    stripe_api_key: Optional[str] = None
    stripe_webhook_secret: Optional[str] = None
    stripe_price_id: Optional[str] = None
    stripe_success_url: Optional[str] = None
    stripe_cancel_url: Optional[str] = None
    stripe_portal_return_url: Optional[str] = None

    admin_token: str = Field(default="change-admin-token")

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()

def stripe_enabled() -> bool:
    return bool(settings.stripe_api_key and settings.stripe_price_id and settings.stripe_webhook_secret)
