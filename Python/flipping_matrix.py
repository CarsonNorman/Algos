# Sean invented a game involving a 2Nx2N matrix where each cell of the matrix contains an integer. 
# He can reverse any of its rows or columns any number of times. 
# The goal of the game is to maximize the sum of the elements in the N x N submatrix located in the upper-left quadrant of the matrix.

# Given the initial configurations for q matrices, help Sean reverse the rows and columns of each matrix in the best possible way so that the sum of the elements in the matrix's upper-left quadrant is maximal.

def flippingMatrix(matrix):
    #horizontal comparison
    for i in matrix:
        for j in range(int(len(i)/2)):
            if i[j] < i[len(i) - j - 1]:
                i[j], i[len(i) -j - 1] = i[len(i) -j - 1], i[j]
                             
    #vertical comparison (Needs to be optimized)
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        for j in range(int(len(row)/2)):
            if(row[j] < row[len(row) - j - 1]):
                matrix[j][i], matrix[len(row) - j - 1][i] = matrix[len(row) - j - 1][i], matrix[j][i]
        
    #final answer calculation
    sum = 0
    for i in range(int(len(matrix)/2)):
        for j in range(int(len(matrix)/2)):
            sum += matrix[i][j]
    return sum