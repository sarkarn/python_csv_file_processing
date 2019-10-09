import configparser

from bli.coverage.Loci import Loci
from bli.coverage.SequenceReads import SequenceReads


class CoverageCalculator:
    # Inialize the source sequence reads, loci and the output location of the loci csv files
    def __init__(self, seq_reads_file_loc, loci_file_src_loc, loci_file_output_loc):
        self.__seq_reads_file_loc = seq_reads_file_loc
        self.__loci_file_src_loc = loci_file_src_loc
        self.__loci_file_output_loc = loci_file_output_loc

    def sort_nested_list(self, nested_list):
        # sort in the ascending order based on the 1st element
        nested_list.sort(key=lambda x: x[0])
        return nested_list

        # This function gets the sequence reads from the SequenceReads class and position from the Loci class,

    # then it passes sequence reads and position to calculate_coverage function which calculate the coverage for the
    # each position.
    def get_coverage(self):
        reads = SequenceReads(seq_reads_file=self.__seq_reads_file_loc)
        # Read the Sequence reads from the reads.csv
        reads_pos_list = reads.get_sequence_reads()

        # sort the data based on the start index so that search algorithm can be efficient.
        sorted_reads = self.sort_nested_list(reads_pos_list)

        loci = Loci(loci_file_src_loc=self.__loci_file_src_loc, loci_file_output_loc=self.__loci_file_output_loc)
        # Get all the position
        pos_list = loci.load_position()

        # calculate coverage for each position
        p_coverage = self.calculate_coverage(sorted_reads, pos_list)

        # Write the coverage value in the loci file
        #loci.loci_file_writer(posit_list, p_coverage)
        loci.loci_file_writer(p_coverage)

        # for key, value in p_coverage.items():
        # print(str(key) + '  ' + str(value))

    # This function takes the sequence reads which contains start and end position list, and position list
    # as arguments. Then this function compute the coverage for each position.
    def calculate_coverage(self, sorted_reads_pos_list, pos_list):
        pos_coverage = dict()

        # For each position compute the coverage by iterating over all the position.
        for pos in pos_list:
            cov_count = 0
            # don't search if the position coverage is already calculated.
            if pos in pos_coverage:
                continue
            # Iterate over the reads and check whether position is in between start and end position of the sequence reads.
            for reads in sorted_reads_pos_list:
                # stop searching for the position if the start position is greater than the position
                if reads[0] > pos:
                    break
                if reads[0] <= pos < reads[1]:
                    cov_count = cov_count + 1
            pos_coverage[pos] = cov_count
        return pos_coverage





if __name__ == "__main__":
    config = configparser.ConfigParser()
    # Read the sequence reads and loci input file and the loci outfile location from the
    # configuration file
    config.read('config.ini')
    reads_csv_loc = config.get('DEFAULT', 'reads_file_loc')
    loci_csv_src_loc = config.get('DEFAULT', 'loci_file_src_loc')
    loci_csv_output_loc = config.get('DEFAULT', 'loci_file_output_loc')
    ccalc = CoverageCalculator(reads_csv_loc, loci_csv_src_loc, loci_csv_output_loc)
    ccalc.get_coverage()
