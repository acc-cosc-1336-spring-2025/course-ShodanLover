def get_hamming_distance(dna1, dna2):
    """Calculates the Hamming distance between two equal-length DNA strings."""
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    """Computes the reverse complement of a DNA string without using slicing or built-in functions."""
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_complement = ""

    # Reverse the DNA string manually using a loop
    for i in range(len(dna) - 1, -1, -1):
        reversed_complement += complement_map[dna[i]]

    return reversed_complement

