def letter_combinations(digits):
    if not digits:
        return []

    # Digit to letters mapping
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    # Start with an initial empty combination
    result = ['']

    # For each digit in input, build new combinations
    for digit in digits:
        letters = mapping[digit]
        new_result = []
        for prefix in result:
            for letter in letters:
                new_result.append(prefix + letter)
        result = new_result

    return result


# Example
print(letter_combinations("23"))
