# coding: utf-8
from run_schulze import run_schulz
import csv
import sys
import os
from Tkinter import Tk # used for UI
from tkFileDialog import askopenfilename # used to pick a file



# MOST IMPORTANT THING: how your data looks!

Mvotes = [] # a list for temporary storage of vote data by class
class_IDs = [] # a list for all class IDs
votes = [] # a list for all voter data
m22 = ["[Karina Gencheva]","[Chris Wilkinson]","[Amulya Pilla]","[Muhammad Abdurrehman Asif]", "[Fju Mewes]", "[Yael (Maya) Cohen]", "[Sarah Poisner]", "[Aspen Pflughoeft]"]
m21 = ["[Tessa Owens]","[Stella Odiwuor]","[Sho Hihara]","[Nebraska Grayson]","[Johannes M. Halkenhaeusser]","[Audrey Warters]"]


# TODO: ask user to specify first column with candidate names
print ("What is the first column that has a candidate name? (first column == 0)")
try:
    candidates_start_column = int(raw_input())
except ValueError:
    print("ERROR! This is not a number!")

headers =[] # list for headers

r = Tk() # we don't want a full GUI, so keep the root window from appearing
r.withdraw()
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# these two lines cloase the filepicker after selection
r.update()
Tk().destroy()

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
            headers[candidate_indexes[0]:candidate_indexes[-1]], full_data=False)

else:
    print "File not in CSV format!"