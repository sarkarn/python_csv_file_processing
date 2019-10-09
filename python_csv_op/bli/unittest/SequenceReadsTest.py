import unittest
from unittest import mock

from bli.coverage.SequenceReads import SequenceReads


class SequenceReadsTest(unittest.TestCase):

    #Mock the built in open method for reading the sequence reads CSV,
    #, and then make a call to sequence reads function on SequenceReads object.
    @mock.patch("builtins.open", create=True)
    def test_get_sequence_reads(self, mock_open):
        example_file = """startposition,length
        10000,10
        20000,20
        30000,30"""
        mock_open.side_effect = [
            mock.mock_open(read_data=example_file).return_value
        ]
        seq_reads = SequenceReads('/dummy')
        pos_list = seq_reads.get_sequence_reads()
        self.assertEqual(3, len(pos_list))
        self.assertEqual(10000, pos_list[0][0])
        self.assertEqual(10010, pos_list[0][1])
        self.assertEqual(20000, pos_list[1][0])
        self.assertEqual(20020, pos_list[1][1])

if __name__ == '__main__':
    unittest.main()
