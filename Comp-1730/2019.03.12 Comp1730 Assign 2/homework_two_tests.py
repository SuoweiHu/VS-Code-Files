import sys
import pytest
from sum_of_squares import sum_of_squares

suffixes = {0: "th", 1: "st", 2: "nd", 3: "th", 4: "th", 5: "th", 6: "th", 7: "th", 8: "th", 9: "th"}


def test_sum_of_squares_output_1():
    s1_tests = ((1, 1), (2, 5), (3, 14), (4, 30), (5, 55))
    message = "The {}{} square pyramidal number is {}. Your function returned {}."
    for n, correct in s1_tests:
        result = sum_of_squares(n)
        assert result == correct, message.format(n, suffixes[n % 10], correct, result)


def test_sum_of_squares_output_2():
    s2_tests = ((0, 0), (6, 91), (9, 285), (11, 506), (32, 11440), (51, 45526), (101, 348551))
    message = "The {}{} square pyramidal number is {}. Your function returned {}."
    for n, correct in s2_tests:
        result = sum_of_squares(n)
        assert result == correct, message.format(n, suffixes[n % 10], correct, result)


def test_sum_of_squares_return_type():
    s1_tests = ((1, 1), (2, 5), (3, 14), (4, 30), (5, 55))
    message = "The return value must be type <class 'int'>, your function returned a value of type {}."
    for n, correct in s1_tests:
        result = type(sum_of_squares(n))
        assert result == int, message.format(result)




if __name__ == '__main__':
    pytest.main(sys.argv)
