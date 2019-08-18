# coding: utf-8
from pyvotecore.stv import STV
from pyvotecore.schulze_stv import SchulzeSTV
from pyvotecore.condorcet import CondorcetHelper
import csv
from pprint import pprint

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


#import data 
M2020_votes = []
M2019_votes = []
M2021_votes = []
votes = []

headers =[]

with open('/Users/Roiman/Downloads/Spring 2019 Ballot (Responses) - Data Procseeing M22 (22_40 Jan 27 PST).csv',
          'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        votes.append(row)
    # for row in csvreader:
    #     if row[0] == 'M2019':
    #         M2019_votes.append(row)
    #     elif row[0] == 'M2020':
    #         M2020_votes.append(row)
    #     elif row[0] == 'M2021':
    #         M2021_votes.append(row) 
    #     else:
    #         headers.append(row)




# m19
# print 'm19'
# run_schulz([v[1:7] for v in M2019_votes], headers[0][1:7])
# m20
print 'm22'
run_schulz([v[2:10] for v in votes[1:]],
    votes[0][2:10], full_data=False)
# m21
# print 'm21'
# run_schulz([v[14:] for v in M2021_votes], headers[0][14:])

