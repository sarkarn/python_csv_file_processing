
import csv
import sys


class Loci:
    #Initialize the source loci file and output loci file location
    def __init__(self, loci_file_src_loc, loci_file_output_loc):
        self.__loci_file_src_loc = loci_file_src_loc
        self.__loci_file_output_loc = loci_file_output_loc

    # Read the loci.csv and load the position in the list
    def load_position(self):
        pos_list = []
        try:
            with open(self.__loci_file_src_loc, 'rt') as loci_file:
                loci_data = csv.reader(loci_file, delimiter=',')
                next(loci_data)
                for row in loci_data:
                    pos = int(row[0])
                    pos_list.append(pos)
        except IOError as e:
            print("I/O error while reading file {0} ({1}): {2}".format(self.__loci_file_src_loc, e.errno, e.strerror))
        return pos_list

    # Write to loci file with the coverage value
    #def loci_file_writer(self, posit_list, loci_coverage):
    def loci_file_writer(self, loci_coverage):
        print('output file directory ' + self.__loci_file_output_loc)
        try:
            with open(self.__loci_file_output_loc, 'w', newline='') as loci_file:
                writer = csv.writer(loci_file, delimiter=',')
                # write the header
                writer.writerow(['position', 'coverage'])
                #for pos in posit_list:
                    #coverage = loci_coverage.get(pos)
                    #writer.writerow([pos, coverage])
                for key, value in loci_coverage.items():
                    writer.writerow([key, value])
                loci_file.flush()
        except IOError as e:
            print("I/O error while writing file {0} ({1}): {2}".format(self.__loci_file_output_loc, e.errno, e.strerror))

