# coding: utf-8
# runs the shculz STV

from vote_core.pyvotecore.stv import STV
from vote_core.pyvotecore.schulze_stv import SchulzeSTV
from vote_core.pyvotecore.condorcet import CondorcetHelper
from pprint import pprint
def run_schulz(votes, header, full_data=False, required_winners=3):
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
        pprint(SchulzeSTV(input, required_winners=required_winners).as_dict())
    else:
        pprint(SchulzeSTV(input, required_winners=required_winners).as_dict()['winners'])


