import time
import random


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:
        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    d = 256
    q = 101

    h = pow(d, m - 1, q)

    pattern_hash = 0
    text_hash = 0

    matches = []
    comparisons = 0

    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        text_hash = (d * text_hash + ord(text[i])) % q

    for i in range(n - m + 1):

        if pattern_hash == text_hash:

            for j in range(m):
                comparisons += 1

                if text[i + j] != pattern[j]:
                    break
            else:
                matches.append(i)

        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) +
                         ord(text[i + m])) % q

            if text_hash < 0:
                text_hash += q

    return matches, comparisons


# Main Program

text = "AABAACAADAABAABA"
pattern = "AABA"

print("Text :", text)
print("Pattern :", pattern)

result1, comp1 = naive_search(text, pattern)
result2, comp2 = kmp_search(text, pattern)
result3, comp3 = rabin_karp(text, pattern)

print("\nNaive Search")
print("Matches :", result1)
print("Comparisons :", comp1)

print("\nKMP Search")
print("Matches :", result2)
print("Comparisons :", comp2)

print("\nRabin Karp")
print("Matches :", result3)
print("Comparisons :", comp3)


# Performance Comparison

text_large = "".join(random.choices("ABCD", k=10000))
patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

print("\nPerformance Comparison")
print("-------------------------------------------")
print("Pattern\t\tNaive\tKMP\tRK")

for p in patterns:
    _, c1 = naive_search(text_large, p)
    _, c2 = kmp_search(text_large, p)
    _, c3 = rabin_karp(text_large, p)

    print(f"{p}\t\t{c1}\t{c2}\t{c3}")
    