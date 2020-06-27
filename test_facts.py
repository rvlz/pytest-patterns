import pytest  # new
import responses as _responses  # new (to use 'responses' identifier elsewhere)

from facts import get_math_fact, get_many_math_facts


@pytest.fixture
def responses():
    """Set up responses fixture."""
    with _responses.RequestsMock() as rsps:
        yield rsps


def test_get_math_fact(responses):
    """Test function returns a single math fact."""
    responses.add(
        _responses.GET,
        "http://numbersapi.com/4/math",
        body="4 is the first positive non-Fibonacci number.",
        status=200,
    )
    fact = get_math_fact(4)
    assert fact == "4 is the first positive non-Fibonacci number."
    assert len(responses.calls) == 1


def test_get_many_facts(responses):
    """Test function can get multiple math facts."""
    responses.add(
        _responses.GET,
        "http://numbersapi.com/1/math",
        body="1 is the multiplicative identity.",
        status=200,
    )
    responses.add(
        _responses.GET,
        "http://numbersapi.com/2/math",
        body="2 is a primorial, as well as its own factorial.",
        status=200,
    )
    responses.add(
        _responses.GET,
        "http://numbersapi.com/3/math",
        body="3 is the number of spatial dimensions we live in.",
        status=200,
    )
    numbers = [1, 2, 3]
    facts = get_many_math_facts(numbers)
    assert facts == [
        "1 is the multiplicative identity.",
        "2 is a primorial, as well as its own factorial.",
        "3 is the number of spatial dimensions we live in.",
    ]
    assert len(responses.calls) == 3
