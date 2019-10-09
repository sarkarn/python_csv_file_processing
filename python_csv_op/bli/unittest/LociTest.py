import unittest
from unittest import mock

from bli.coverage import SequenceReads
from bli.coverage.Loci import Loci


class LociTest(unittest.TestCase):


    #Mock the built in open method for reading loci  CSV,
    #, and then make a call to load_position function on Loci object.
    @mock.patch("builtins.open", create=True)
    def test_load_position(self, mock_open):
        example_file = """position,coverage
        10001,
        20005,
        30007,"""
        mock_open.side_effect = [
            mock.mock_open(read_data=example_file).return_value
        ]
        loci = Loci('/dummy/src', '/dummy/output')
        pos = loci.load_position()
        self.assertEqual(3, len(pos))
        self.assertEqual(10001, pos[0])
        self.assertEqual(20005, pos[1])
        self.assertEqual(30007, pos[2])



    #Mock the built in open method for opening loci  CSV,
    #, and then make a call to loci_file_writer function on Loci object.
    @mock.patch("builtins.open", create=True)
    def test_loci_file_writer(self, mock_open):
        example_file = """position,coverage
        ,"""
        mock_open.side_effect = [
            mock.mock_open(read_data=example_file).return_value
        ]
        loci = Loci('/dummy/src', '/dummy/output')
        pos_list = [10001, 10005, 20008]
        coverage_data = {10001: 1, 10005: 2, 20008: 4}
        #loci.loci_file_writer(pos_list, coverage_data)
        loci.loci_file_writer(coverage_data)
        self.assertLogs("Test Case Passes")


if __name__ == '__main__':
    unittest.main()