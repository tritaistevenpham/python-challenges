from in_celsius import in_celsius
from min_four import min_four
from second_vowel import second_vowel


def test_in_celsius():
    print(in_celsius(32.0))
    print(in_celsius(212.0))
    print(in_celsius(-40.0))


def test_min_four():
    print(min_four(1, 2, 3, 4))
    print(min_four(3, 2, 4, 6))
    print(min_four(0, 0, -5, 0))


def test_second_vowel():
    print(second_vowel('test'))
    print(second_vowel('aeiou'))
    print(second_vowel('slowly'))
    print(second_vowel('yip'))
    print(second_vowel('yoghurt'))


# Main Function:
if __name__ == '__main__':
    # Unit Testing:
    print(f"Running Unit Tests:")
    test_in_celsius()
    print(f"~> End in_celsius\n")
    test_min_four()
    print(f"~> End min_four\n")
    test_second_vowel()
    print(f"~> End second_vowel\n")
