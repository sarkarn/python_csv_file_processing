import unittest
from unittest import mock

from bli.coverage.CoverageCalculator import CoverageCalculator
from bli.coverage.Loci import Loci
from bli.coverage.SequenceReads import SequenceReads


class CoverageCalculatorTest(unittest.TestCase):

    #Mock the sequence data
    def mock_get_seq_reads(self):
        reads_pos = [[10000, 10010], [20000, 20020], [30000, 30030]]
        return reads_pos
    #Mock the loci position
    def mock_load_loci_position(self):
        pos = [10001, 10002, 200000]
        return pos

    #Test Initializer
    def test_init(self):
        cov_calc = CoverageCalculator('/test/reads/loc', '/test/loci/src/loc', '/test/loci/output/loc')
        self.assertIsNotNone(cov_calc, 'Instance of CoverageCalculator is not null')

    def test_sorted_nested_list(self):
        cov_calc = CoverageCalculator('/test/reads/loc', '/test/loci/src/loc', '/test/loci/output/loc')
        reads_pos = [[10001, 10005], [30000, 30020], [20000, 20025], [15000, 15020]]
        sorted_reads_pos = cov_calc.sort_nested_list(reads_pos)
        self.assertEqual(15000, sorted_reads_pos[1][0])

    # Mock the Sequencereads and Loci class in order to avoid the reading files
    # and test the get coverage method.
    def test_get_coverage(self):
        reads_pos = [[]]
        pos = []
        with mock.patch.object(SequenceReads, 'get_sequence_reads', new=self.mock_get_seq_reads):
            seq_reads = SequenceReads('/mock_path')
            reads_pos = seq_reads.get_sequence_reads()  # This will call mock method
        with mock.patch.object(Loci, 'load_position', new=self.mock_load_loci_position):
            lc = Loci('/mock_path', '/mock_path')
            pos = lc.load_position()  # This will call mock method
        cov_calc = CoverageCalculator('/test/reads/loc', '/test/loci/src/loc', '/test/loci/output/loc')
        v_coverage = cov_calc.calculate_coverage(reads_pos, pos)
        self.assertEqual(1, v_coverage[10001])
        self.assertEqual(1, v_coverage[10002])
        self.assertEqual(0, v_coverage[200000])
        self.assertEqual(3, len(v_coverage))

    #Test calculate coverage method
    def test_calculate_coverage(self):
        cov_calc = CoverageCalculator('/test/reads/loc', '/test/loci/src/loc', '/test/loci/output/loc')
        v_coverage = cov_calc.calculate_coverage(self.mock_get_seq_reads(), self.mock_load_loci_position())
        self.assertEqual(1, v_coverage[10001])
        self.assertEqual(1, v_coverage[10002])
        self.assertEqual(0, v_coverage[200000])
        self.assertEqual(3, len(v_coverage))

if __name__ == '__main__':
    unittest.main()


