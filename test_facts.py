import pytest  # new
import responses as _responses  # new (to use 'responses' identifier elsewhere)

from facts import get_math_fact, get_many_math_facts

single_fact_data = [(4, "4 is the first positive non-Fibonacci number.")]
many_facts_data = [
    (1, "1 is the multiplicative identity."),
    (2, "2 is a primorial, as well as its own factorial."),
    (3, "3 is the number of spatial dimensions we live in."),
]


@pytest.fixture
def responses(data):
    """Set up responses fixture."""
    with _responses.RequestsMock() as rsps:
        for number, fact in data:
            rsps.add(
                _responses.GET,
                "http://numbersapi.com/%s/math" % number,
                body=fact,
                status=200,
            )
        yield rsps


@pytest.mark.parametrize("data", [single_fact_data])
def test_get_math_fact(responses):
    """Test function returns a single math fact."""
    fact = get_math_fact(4)
    assert fact == "4 is the first positive non-Fibonacci number."
    assert len(responses.calls) == 1


@pytest.mark.parametrize("data", [many_facts_data])
def test_get_many_facts(responses):
    """Test function can get multiple math facts."""
    numbers = [1, 2, 3]
    facts = get_many_math_facts(numbers)
    assert facts == [
        "1 is the multiplicative identity.",
        "2 is a primorial, as well as its own factorial.",
        "3 is the number of spatial dimensions we live in.",
    ]
    assert len(responses.calls) == 3
