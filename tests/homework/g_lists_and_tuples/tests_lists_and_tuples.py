import unittest
from src.homework.g_lists_and_tuples.dictionary import get_p_distance, get_p_distance_matrix

class Test_Config(unittest.TestCase):

    def test_p_distance(self):
        seq1 = ['T','T','T','C','C','A','T','T','T','A']
        seq2 = ['G','A','T','T','C','A','T','T','T','C']
        result = get_p_distance(seq1, seq2)
        self.assertAlmostEqual(result, 0.4, places=3)

    def test_get_p_distance_matrix(self):
        sequences = [
            ['T','T','T','C','C','A','T','T','T','A'],
            ['G','A','T','T','C','A','T','T','T','C'],
            ['T','T','T','C','C','A','T','T','T','T'],
            ['G','T','T','C','C','A','T','T','T','A']
        ]
        expected = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result = get_p_distance_matrix(sequences)
        for i in range(len(expected)):
            for j in range(len(expected[i])):
                self.assertAlmostEqual(result[i][j], expected[i][j], places=3)
