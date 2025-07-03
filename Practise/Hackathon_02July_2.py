def min_subset_diff(arr):
    total = sum(arr)
    n = len(arr)
    target = total // 2

    # dp[i] = True if subset sum i is possible
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    for i in range(target, -1, -1):
        if dp[i]:
            s1 = i
            break

    s2 = total - s1
    return abs(s2 - s1)

# Example
arr = [1, 6, 11, 5]
print("Minimum difference:", min_subset_diff(arr))  # Output: 1
