import requests

URL = "http://numbersapi.com/%s/math"


def get_math_fact(number):
    """Get one math fact."""
    response = requests.get(URL % number)
    return response.content.decode()


def get_many_math_facts(numbers):
    """Get multiple math facts."""
    facts = []
    for number in numbers:
        response = requests.get(URL % number)
        facts.append(response.content.decode())
    return facts
