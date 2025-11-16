def palindrome_pairs(words):
    pairs = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # distinct indices
                combined = words[i] + words[j]
                if combined == combined[::-1]:  # check palindrome
                    pairs.append([i, j])
    return pairs


# Example 1
words1 = ['bat', 'tab', 'cat']
print(palindrome_pairs(words1))

# Example 2
words2 = ['a', 'abc', 'cba', '']
print(palindrome_pairs(words2))
