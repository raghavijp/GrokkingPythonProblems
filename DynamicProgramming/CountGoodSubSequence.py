MOD = 1000000007

# read through explanation in educative
def quick_modular_inverse(base, exponent, modulus):
    result = 1

    while exponent != 0:
        if (exponent & 1) == 1:
            result = result * base % modulus

        exponent >>= 1
        base = base * base % modulus

    return result


def combination(n, k, factorials, inverses):
    return (factorials[n] * inverses[k] % MOD) * inverses[n-k] % MOD


def count_good_subsequences(s):

    N = len(s) + 1
    factorials = [1] * N
    inverses = [1] * N

    for i in range(1, N):
        factorials[i] = factorials[i-1] * i % MOD
        inverses[i] = quick_modular_inverse(factorials[i], MOD - 2, MOD)

    frequency_count = [0] * 26

    max_count = 1

    for char in s:
        max_count = max(max_count, frequency_count[ord(char) - ord('a')] + 1)
        frequency_count[ord(char) - ord('a')] += 1

    final_count = 0

    for i in range(1, max_count + 1):
        count = 1

        for j in range(26):
            if frequency_count[j] >= i:
                count = count * (combination(frequency_count[j], i,  factorials, inverses) + 1) % MOD

        final_count = (final_count + count - 1) % MOD

        # Returning the final count after casting it to integer
    return int(final_count)

def main():
    input_list = ["aqw", "aabbcc", "aaa", "abbc", "abbb"]

    for i, s in enumerate(input_list):
        print(f"\t given value: ", s)
        print(f"\t combinations: ", count_good_subsequences(s))
        print("-"*100)


if __name__ == "__main__":
    main()