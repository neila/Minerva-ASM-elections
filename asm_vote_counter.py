# coding: utf-8
from vote_core.pyvotecore.stv import STV
from vote_core.pyvotecore.schulze_stv import SchulzeSTV
from vote_core.pyvotecore.condorcet import CondorcetHelper
import csv
import sys
import os
from pprint import pprint
from Tkinter import Tk # used for UI
from tkFileDialog import askopenfilename # used to pick a file



# MOST IMPORTANT THING: how your data looks!
# TODO: write requirements.

def run_schulz(votes, header, full_data=False):
    """
    votes: a list of lists containing each voter, append
            the ranked preferences of each voter.
            The preferences are numbers (1 through n)
            and they are ordered by the same order as the headers
    header: a list of names, in the order that they were collected.
    full_data: presents all the information, not just winner names.
    """

    ballots = []

    for vote in votes:

        ballots.append(
            filter(
                lambda candidate: candidate != 'DROP',
                map(lambda (rank, candidate): 'DROP' if rank == '' else candidate,
                    sorted(zip(vote, header)))))


    ballots = list(filter(lambda candidate: candidate != [], ballots))


    ballot_count = {}
    for ballot in ballots:
        ballot = tuple(ballot)
        if ballot in ballot_count:
            ballot_count[ballot] += 1
        else:
            ballot_count[ballot] = 1


    input = [{
        "count": v,
        "ballot": list(k)
    } for k, v in ballot_count.items()]

    for line in input:
        dict_ballot = {}
        for rank, candidate in enumerate(line['ballot']):
            dict_ballot[candidate] = -rank

        line['ballot'] = dict_ballot

    if full_data:
        pprint(SchulzeSTV(input, required_winners=3).as_dict())
    else:
        pprint(SchulzeSTV(input, required_winners=3).as_dict()['winners'])


Mvotes = [] # a list for temporary storage of vote data by class
class_IDs = [] # a list for all class IDs
votes = [] # a list for all voter data
m22 = ["[Karina Gencheva]","[Chris Wilkinson]","[Amulya Pilla]","[Muhammad Abdurrehman Asif]", "[Fju Mewes]", "[Yael (Maya) Cohen]", "[Sarah Poisner]", "[Aspen Pflughoeft]"]
m21 = ["[Tessa Owens]","[Stella Odiwuor]","[Sho Hihara]","[Nebraska Grayson]","[Johannes M. Halkenhaeusser]","[Audrey Warters]"]


# TODO: ask user to specify first column with candidate names
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
        # TODO: each class should be auto-found by a first column indicator
        """ e.g. 
        class_IDs = list
        for row[0] in votes:
            if row[0] not in class_IDs:
                class_IDs.append(row[0])
        """

        for row in csvreader:
            votes.append(row)

    headers = votes[0] # get headers
    for row in votes[1:]:
        if row[0] not in class_IDs:
            class_IDs.append(row[0])
    
    for ID in class_IDs:
        # temporary store votes by class
        for row in votes:
            if row[0] == ID:
                Mvotes.append(row)

        # TODO: find indexes of headers of this Mclass
        # TODO: only select vote and header segments of this Mclass

        print ID
        run_schulz([v[2:] for v in Mvotes],
            headers[2:], full_data=False)

    # m19
    # print 'm19'
    # run_schulz([v[1:7] for v in M2019_votes], headers[0][1:7])
    # m20
    # print 'm22'
    # run_schulz([v[2:10] for v in votes[1:]],
    #     votes[0][2:10], full_data=False)
    # m21
    # print 'm21'
    # run_schulz([v[14:] for v in M2021_votes], headers[0][14:])

else:
    print "File not in CSV format!"