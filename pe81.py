with open('matrix.txt', 'r') as f:
    matrix = [map(int, line.strip('\n').split(',')) for line in f]

dp = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

for j in range(len(matrix[0])):
    dp[0][j] = sum(matrix[0][:j+1])

for i in range(1, len(matrix)):
    dp[i][0] = sum([matrix[k][0] for k in range(i+1)])

for i in range(1, len(matrix)):
    for j in range(1, len(matrix[0])):
        topval = matrix[i][j] + dp[i-1][j]
        leftval = matrix[i][j] + dp[i][j-1]
        
        if topval <= leftval:
            dp[i][j] = topval
        else:
            dp[i][j] = leftval

print dp[len(matrix)-1][len(matrix[0])-1]