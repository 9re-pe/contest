n = int(input())
d = []
for _ in range(n-1):
    d += list(map(int, input().split()))

# Convert D to a 2D matrix for easier indexing
matrix = [[0] * n for _ in range(n)]
idx = 0
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j] = d[idx]
        matrix[j][i] = d[idx]
        idx += 1

# Initialize dp array with 2^N elements set to 0
dp = [0] * (1 << n)

# Iterate through all possible masks
for mask in range(1 << n):
    # Update the dp array using the edges
    for i in range(n):
        for j in range(i+1, n):
            # If neither i nor j is used in the current mask
            if not (mask & (1 << i)) and not (mask & (1 << j)):
                new_mask = mask | (1 << i) | (1 << j)
                dp[new_mask] = max(dp[new_mask], dp[mask] + matrix[i][j])

print(dp[(1 << n) - 1])
