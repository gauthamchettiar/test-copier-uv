from test_uv.hello import hello


def test_hello_default() -> None:
    """Test the hello function with default parameter."""
    result = hello()
    assert "Hello, World" in result
    assert "test_uv" in result


def test_hello_with_name() -> None:
    """Sample test for hello function with a custom name."""
    result = hello("Alice")
    assert result == "Hello, Alice from test_uv!"
