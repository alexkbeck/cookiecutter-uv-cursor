{% if cookiecutter.pydantic_models == 'y' -%}
"""Data models using Pydantic for validation and serialization."""

from pydantic import BaseModel


class FooModel(BaseModel):
    """Description of Pydantic model."""
    
    bar: str
    
    def __str__(self) -> str:
        """String representation of the model."""
        return f"FooModel(bar={self.bar})"
{%- endif %} 