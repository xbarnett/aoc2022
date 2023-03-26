def freqs(s):
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    return result
