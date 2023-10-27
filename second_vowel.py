def second_vowel(s: str) -> int:
    # Returns the INDEX of the second vowel in 's', if none return -1
    # A vowel is defined as 'aeiou' and a 'y' that isn't the first character
    # Examples:
    #   second_vowel('test') -> -1
    #   second_vowel('aeiou') -> 1
    #   second_vowel('slowly') -> 5
    #   second_vowel('yip') -> -1
    vowels = 'aAeEiIoOuUyY'
    pos = 0
    num_vowels = 0
    exit_cond = False

    # Reduce the num_vowels by 1 if string starts with y/Y
    if s[0] in 'yY':
        num_vowels -= 1

    # For each character in input string
    if not exit_cond:
        for ch in s:
            # If character contains a vowel:
            if ch in vowels:
                # Increment number of vowels
                num_vowels += 1
                if num_vowels == 2:
                    # We only care about the second vowel
                    break
            # Finally update position
            pos += 1

    # If number of vowels is less than 2, this means we can't find a second vowel
    if num_vowels < 2:
        exit_cond = True

    if exit_cond:
        pos = -1

    return pos
