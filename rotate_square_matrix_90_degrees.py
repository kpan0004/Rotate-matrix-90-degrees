"""
New column index is current row index
New row index is dimension - 1 - (current column index)
"""
def rotate_square_matrix_90(a_matrix):
    assert len(a_matrix) == len(a_matrix[0]), "Input must be a square matrix"
    dim = len(a_matrix)
    for i in range (dim // 2): #Number of 'loops'
        for j in range(i, dim - i - 1): #Start and end indices of the loop
            i_2,j_2 = get_point_90_away(i,j, dim)
            i_3,j_3 = get_point_90_away(i_2,j_2, dim)
            i_4,j_4 = get_point_90_away(i_3,j_3, dim)
            swap_elements_pythonic(a_matrix, i, j, i_2, j_2, i_3, j_3, i_4, j_4)
    return a_matrix

"""
Points 1,2,3,4 are defined in clockwise order. For the algo to worth they must
90 degrees apart in the same 'loop' in the matrix
"""
def swap_elements(a_matrix, i_1, j_1, i_2, j_2, i_3, j_3, i_4, j_4):
    temp1 = a_matrix[i_1][j_1]
    temp2 = a_matrix[i_2][j_2]
    temp3 = a_matrix[i_3][j_3]
    a_matrix[i_3][j_3] = a_matrix[i_4][j_4]
    a_matrix[i_2][j_2] = temp3
    a_matrix[i_1][j_1] = temp2
    a_matrix[i_4][j_4] = temp1

def swap_elements_pythonic(a_matrix, i_1, j_1, i_2, j_2, i_3, j_3, i_4, j_4):
    a_matrix[i_1][j_1], a_matrix[i_2][j_2], a_matrix[i_3][j_3], a_matrix[i_4][j_4] = \
    a_matrix[i_2][j_2], a_matrix[i_3][j_3], a_matrix[i_4][j_4], a_matrix[i_1][j_1]                    

def get_point_90_away(i,j, dim):
    new_j = dim - 1 - i
    new_i = j
    return new_i, new_j

def pretty_print(a_matrix):
    for row in a_matrix:
        for item in row:
            item = str(item)
            while len(item) < 2:
                item += " "
            print(item, end = " ")
        print("")

if __name__ == "__main__":
    my_matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    my_matrix2 = [[1,2,3],[4,5,6],[7,8,9]]
    matrices = [my_matrix, my_matrix2]
    for matrix in matrices:
        print("----------")
        print("Original matrix:")
        pretty_print(matrix)
        print("")
        print("Matrix rotated 90 degrees:")
        pretty_print(rotate_square_matrix_90(matrix))
        print("----------")

