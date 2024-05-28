import numpy as np

def pairwise_comparison_matrix(criteria, comparisons):
    n = len(criteria)
    matrix = np.ones((n, n))
    for (i, j), value in comparisons.items():
        matrix[i, j] = value
        matrix[j, i] = 1 / value
    return matrix

def normalize_matrix(matrix):
    column_sums = np.sum(matrix, axis=0)
    normalized_matrix = matrix / column_sums
    return normalized_matrix

def calculate_priority_vector(normalized_matrix):
    priority_vector = np.mean(normalized_matrix, axis=1)
    return priority_vector

def calculate_consistency_ratio(matrix, priority_vector):
    n = matrix.shape[0]
    weighted_sum_vector = np.dot(matrix, priority_vector)
    lambda_max = np.mean(weighted_sum_vector / priority_vector)
    ci = (lambda_max - n) / (n - 1)
    
    # Consistency Index (CI) table
    ri_values = {
        1: 0.0, 2: 0.0, 3: 0.58, 4: 0.90, 5: 1.12,
        6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49
    }
    ri = ri_values[n]
    cr = ci / ri if ri != 0 else 0
    return cr

def ahp(criteria, comparisons):
    matrix = pairwise_comparison_matrix(criteria, comparisons)
    normalized_matrix = normalize_matrix(matrix)
    priority_vector = calculate_priority_vector(normalized_matrix)
    consistency_ratio = calculate_consistency_ratio(matrix, priority_vector)
    
    return priority_vector, consistency_ratio
