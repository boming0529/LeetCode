def solution(S):
    occurrences = [0] * 26
    # cluc frequently times
    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = occurrences[0]

    for i in range(1, 26):
    # for i in range(-1, -27, -1):
        if occurrences[i] > best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char

S = 'zzzaaa'
ans = solution(S)
print(ans)

S = 'aabbccaadcc'
ans = solution(S)
print(ans)

S = 'hello'
ans = solution(S)
print(ans)