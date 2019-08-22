# coding: utf-8
from run_schulze import run_schulz
from UI_elements import get_file_path, get_number_of_winners, get_first_candidate_column
import csv
import sys
import os

# MOST IMPORTANT THING: how your data looks!

Mvotes = [] # a list for temporary storage of vote data by class
class_IDs = [] # a list for all class IDs
votes = [] # a list for all voter data

# TODO: ask user to specify first column with candidate names
try:
    candidates_start_column = int(get_first_candidate_column())
    required_winners = int(get_number_of_winners())
except ValueError:
    print("ERROR! This is not a number!")


# TODO: ask for number of winners (verify 3)

headers =[] # list for headers

filename = get_file_path()


# verify the file is a .csv
if filename.endswith('.csv'):
    # TODO: move following sections to sub-functions
    with open(filename,
              'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            votes.append(row)

    headers = votes[0] # get headers
    votes = votes[1:] # discard headers from votes
    
    # find all classes these votes are for
    for row in votes:
        if row[0] not in class_IDs:
            class_IDs.append(row[0])
    
    for ID in class_IDs:
        """
        # set to 1 after we get this class's candidates
        # this allows us to stop searching in the rows
        # once we get one non-empty row
        # WARNING: implicit assumption is that each voter
        #           ranks *every* candidate in their class.
        
        # There is an "obvious" assumption that the indexes will
        # end up sequential within the same class.
        # The code must be tweaked otherwise
        """
        candidate_ticker = 0
        candidate_indexes = []

        # temporary store votes by class
        for row in votes:
            if row[0] == ID:
                Mvotes.append(row)
                # find indexes of headers of this Mclass
                if candidate_ticker == 0:
                    for column in row[candidates_start_column:]:
                        if len(column)>0:
                            candidate_indexes.append(row.index(column))
                    if len(candidate_indexes)>0:
                        candidate_ticker = 1

        # Print which class's results these are
        print ID
        # using first and last indexes
        run_schulz([v[candidate_indexes[0]:candidate_indexes[-1]] for v in Mvotes],
            headers[candidate_indexes[0]:candidate_indexes[-1]], full_data=False,
            required_winners=required_winners)

else:
    print "File not in CSV format!"