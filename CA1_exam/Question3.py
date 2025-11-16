def min_window_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    min_len = float('inf')
    start = -1

    i = 0
    while i < m:
        j = 0
        # Move i until we find a match sequence for s2
        while i < m:
            if s1[i] == s2[j]:
                j += 1
                if j == n:
                    break
            i += 1


        if j < n:
            break

        # Move backward to find the smallest window
        end = i
        j -= 1
        while j >= 0:
            if s1[i] == s2[j]:
                j -= 1
            i -= 1

        i += 1  

        # Check window length
        if end - i + 1 < min_len:
            min_len = end - i + 1
            start = i

        # Move i to the next chara to find next possible window
        i = i + 1

    # return "" if start == -1 else s1[start:start + min_len]
    if start == -1:
        return ""
    else:
        return s1[start : start + min_len]



s1 = "abcdebdde"
s2 = "bde"
print(min_window_subsequence(s1, s2))
