import responses

from facts import get_math_fact, get_many_math_facts


def test_get_math_fact():
    """Test function returns a single math fact."""
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "http://numbersapi.com/4/math",
            body="4 is the first positive non-Fibonacci number.",
            status=200,
        )
        fact = get_math_fact(4)
        assert fact == "4 is the first positive non-Fibonacci number."
        assert len(rsps.calls) == 1


def test_get_many_facts():
    """Test function can get multiple math facts."""
    with responses.RequestsMock() as rsps:
        rsps.add(
            responses.GET,
            "http://numbersapi.com/1/math",
            body="1 is the multiplicative identity.",
            status=200,
        )
        rsps.add(
            responses.GET,
            "http://numbersapi.com/2/math",
            body="2 is a primorial, as well as its own factorial.",
            status=200,
        )
        rsps.add(
            responses.GET,
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
        assert len(rsps.calls) == 3
