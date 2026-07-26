def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    number_of_rows = len(a)
    number_of_columns = len(a[0])
    transposed_result = []
    for col in range(number_of_columns):
        subset_list = []
        for row in range(number_of_rows):
            subset_list.append(a[row][col])
        transposed_result.append(subset_list)
    return transposed_result



