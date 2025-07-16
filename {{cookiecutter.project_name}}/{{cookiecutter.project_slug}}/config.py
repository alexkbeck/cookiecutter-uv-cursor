{% if cookiecutter.pydantic_settings == 'y' -%}
"""Configuration management using Pydantic Settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings with environment variable support."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Application settings
    app_name: str = Field(default="{{cookiecutter.project_name}}", description="Application name")
    debug: bool = Field(default=False, description="Enable debug mode")
    
    # Logging settings
    log_level: str = Field(default="INFO", description="Logging level")
    
    def __str__(self) -> str:
        """String representation of settings."""
        return f"Settings(app_name={self.app_name}, debug={self.debug})"

# Global settings instance
settings = Settings()
{%- endif %} 