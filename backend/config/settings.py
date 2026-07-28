from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------
    app_name: str = "Sage AI Interview Agent"
    app_version: str = "1.0.0"

    environment: str = "development"
    debug: bool = True

    host: str = "127.0.0.1"
    port: int = 8000

    api_v1_prefix: str = "/api/v1"

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------
    database_url: str

    # ------------------------------------------------------------------
    # AWS
    # ------------------------------------------------------------------
    aws_region: str = "ap-south-1"

    # ------------------------------------------------------------------
    # LiveKit
    # ------------------------------------------------------------------
    livekit_url: str = ""
    livekit_api_key: str = ""
    livekit_api_secret: str = ""

    # ------------------------------------------------------------------
    # File Upload
    # ------------------------------------------------------------------
    upload_directory: str = "storage/resumes"
    max_resume_size_mb: int = 5

    # ------------------------------------------------------------------
    # Pydantic Settings Configuration
    # ------------------------------------------------------------------
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()