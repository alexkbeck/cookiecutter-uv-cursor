{% if cookiecutter.pydantic_models == 'y' -%}
{% if cookiecutter.layout == "src" -%}
from src.{{cookiecutter.project_slug}}.models import FooModel
{%- else -%}
from {{cookiecutter.project_slug}}.models import FooModel
{%- endif %}


class TestFooModel:
    """Test cases for FooModel."""

    def test_valid_model_creation(self):
        """Test creating a valid FooModel."""
        model = FooModel(bar="test")
        
        assert model.bar == "test"

    def test_string_representation(self):
        """Test string representation of the model."""
        model = FooModel(bar="test")
        expected = "FooModel(bar=test)"
        
        assert str(model) == expected

    {% if cookiecutter.mocks == 'y' -%}
    def test_model_with_mock(self, mocker):
        """Test FooModel with mocking."""
        # Example of mocking datetime if needed
        mock_str = mocker.patch.object(FooModel, '__str__')
        mock_str.return_value = "Mocked FooModel"
        
        model = FooModel(bar="test")
        result = str(model)
        
        assert result == "Mocked FooModel"
        mock_str.assert_called_once()
    {%- endif %}
{%- endif %} 