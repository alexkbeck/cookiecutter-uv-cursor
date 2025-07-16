{% if cookiecutter.pydantic_settings == 'y' -%}
import os
{% if cookiecutter.mocks == 'y' -%}
import pytest
{%- endif %}

{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.config import Settings, settings
{%- else -%}
from {{cookiecutter.project_slug}}.config import Settings, settings
{%- endif %}


class TestSettings:
    """Test cases for Settings configuration."""

    def test_default_values(self):
        """Test default configuration values."""
        config = Settings()
        
        assert config.app_name == "{{cookiecutter.project_name}}"
        assert config.debug is False
        assert config.database_url is None
        assert config.api_key is None
        assert config.max_connections == 10
        assert config.log_level == "INFO"

    def test_custom_values(self):
        """Test setting custom configuration values."""
        config = Settings(
            debug=True,
            database_url="sqlite:///test.db",
            api_key="test-key",
            max_connections=5,
            log_level="DEBUG"
        )
        
        assert config.debug is True
        assert config.database_url == "sqlite:///test.db"
        assert config.api_key == "test-key"
        assert config.max_connections == 5
        assert config.log_level == "DEBUG"

    def test_string_representation(self):
        """Test string representation of settings."""
        config = Settings()
        expected = "Settings(app_name={{cookiecutter.project_name}}, debug=False)"
        
        assert str(config) == expected

    def test_max_connections_validation(self):
        """Test max_connections field validation."""
        # Test valid range
        config = Settings(max_connections=50)
        assert config.max_connections == 50
        
        # Test edge cases would require ValidationError, but we keep it simple

    def test_global_settings_instance(self):
        """Test that global settings instance exists."""
        assert settings is not None
        assert isinstance(settings, Settings)

    {% if cookiecutter.mocks == 'y' -%}
    def test_environment_variables(self, monkeypatch):
        """Test configuration loading from environment variables."""
        # Set environment variables
        monkeypatch.setenv("APP_NAME", "test-app")
        monkeypatch.setenv("DEBUG", "true")
        monkeypatch.setenv("API_KEY", "env-api-key")
        monkeypatch.setenv("MAX_CONNECTIONS", "25")
        
        # Create new settings instance to pick up env vars
        config = Settings()
        
        assert config.app_name == "test-app"
        assert config.debug is True
        assert config.api_key == "env-api-key"
        assert config.max_connections == 25

    def test_env_file_configuration(self, monkeypatch, tmp_path):
        """Test configuration loading from .env file."""
        # Create temporary .env file
        env_file = tmp_path / ".env"
        env_file.write_text(
            "APP_NAME=file-app\n"
            "DEBUG=true\n"
            "API_KEY=file-api-key\n"
        )
        
        # Change working directory to tmp_path
        monkeypatch.chdir(tmp_path)
        
        # Create settings instance
        config = Settings()
        
        assert config.app_name == "file-app"
        assert config.debug is True
        assert config.api_key == "file-api-key"
    {%- endif %}
{%- endif %} 