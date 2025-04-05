def get_p_distance(list1, list2):
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return round(differences / len(list1), 5)

def get_p_distance_matrix(sequences):
    matrix = []
    for i in range(len(sequences)):
        row = []
        for j in range(len(sequences)):
            row.append(get_p_distance(sequences[i], sequences[j]))
        matrix.append(row)
    return matrix
