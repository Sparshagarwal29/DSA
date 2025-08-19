def sparseMatrix (matrix):
    if not matrix or not matrix[0]:
        return []
    row = len(matrix)
    col = len(matrix[0])
    non_zero_count = 0 
    
    sparse_Matrix = [[row,col,0]] # row,column,value
    for i in range(row):
        for j in range(col):
            if matrix[i][j] !=0:
                sparse_Matrix.append([i,j,matrix[i][j]])
                non_zero_count +=1
    sparse_Matrix[0][2] = non_zero_count

    return sparse_Matrix

def print_sparse(sparse_Matrix):
    if not sparse_Matrix:
        print("empty")
        return
    row, col, non_zero_count = sparse_Matrix[0]
    print(f"NO of rows: {row} ")
    print(f"NO of cols: {col} ")
    print(f"NO of non zero elements: {non_zero_count} ")
    
    for i in sparse_Matrix[1:]:
        print(f"{i[0]}\t{i[1]}\t{i[2]}")



original_matrix_1 = [
    [0, 0, 3, 0, 4],
    [0, 0, 5, 7, 0],
    [0, 0, 0, 0, 0],
    [0, 2, 6, 0, 0]
]

sparse_rep_1 = sparseMatrix(original_matrix_1)
print_sparse(sparse_rep_1)