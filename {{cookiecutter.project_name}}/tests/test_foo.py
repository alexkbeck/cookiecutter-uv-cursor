{% if cookiecutter.async_support == 'y' or cookiecutter.mocks == 'y' -%}
import pytest
{%- endif %}

{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.foo import foo{% if cookiecutter.async_support == 'y' %}, async_foo{% endif %}
{%- else -%}
from {{cookiecutter.project_slug}}.foo import foo{% if cookiecutter.async_support == 'y' %}, async_foo{% endif %}
{%- endif %}


def test_foo():
    assert foo("foo") == "foo"


{% if cookiecutter.mocks == 'y' -%}
def test_foo_with_mock(mocker):
    """Test foo function with mocking."""
    # Example of mocking print function
    mock_print = mocker.patch("builtins.print")
    
    result = foo("test")
    assert result == "test"
    
    # In a real scenario, you might verify that print was called
    # This is just an example of how to use the mocker fixture

{% if cookiecutter.logging == 'y' -%}
def test_foo_with_logger_mock(mocker):
    """Test foo function with logger mocking."""
    mock_logger = mocker.patch("{{cookiecutter.project_slug}}.foo.logger")
    
    result = foo("test")
    assert result == "test"
    
    # Verify logger was called with expected message
    mock_logger.info.assert_called_once_with("Processing: test")
{%- endif %}
{%- endif %}


{% if cookiecutter.async_support == 'y' -%}
@pytest.mark.asyncio
async def test_async_foo():
    result = await async_foo("foo")
    assert result == "async_foo"

{% if cookiecutter.mocks == 'y' -%}
@pytest.mark.asyncio
async def test_async_foo_with_mock(mocker):
    """Test async_foo function with mocking."""
    # Mock asyncio.sleep to speed up test
    mock_sleep = mocker.patch("asyncio.sleep")
    
    result = await async_foo("test")
    assert result == "async_test"
    
    # Verify asyncio.sleep was called
    mock_sleep.assert_called_once_with(0.1)
{%- endif %}
{%- endif %}
