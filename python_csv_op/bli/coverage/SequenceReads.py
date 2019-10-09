
#This class load the sequence reads from the
#configurable location and compute the end position, then
# it loads start and end position of the reads in the nested list
import csv

class SequenceReads:
    #Initialize the sequence reads location
    def __init__(self, seq_reads_file):
        self.__seq_reads_file = seq_reads_file

    # read the sequence csv file, compute the end position by adding length with the
    # start position,and then  loads into nested list
    def get_sequence_reads(self):
        pos_list = []
        try:
           with open(self.__seq_reads_file, 'rt') as reads_file:
                reads_data = csv.reader(reads_file, delimiter=',')
                next(reads_data)
                for row in reads_data:
                    start_pos = int(row[0])
                    v_length = int(row[1])
                    pos = start_pos + v_length
                    pos_list.append([start_pos, pos])
        except IOError as e:
            print("I/O error while reading file {0}, ({1}) : {2}".format(self.__seq_reads_file, e.errno, e.strerror))
        return pos_list




