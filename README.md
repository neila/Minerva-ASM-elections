# ASM_Elections_Code

## IMPORTANT
Before using this to actually run an election, read the segment on preparing the data for processing. Results will be incorrect otherwise.
> p.s. this code and instructions were written on/for Mac OS (Sierra, 10.12.6).

## How the CSV file needs to be structured?
### First Column: Class ID
> in theory, if ASM representatives are per-cohort this ID should be unique for class+cohort. eg. M23A, M23B, M24, M25, M26A, M26B, etc.

### First Row: Headers
> Question headers and Candidate Names

### Candidate Columns
> - the candidate of each class (or cohort) should be sequential.
> > ie all candidates for M22 should span columns 1-10, not columns 1, 4, 10-15, 21-23.

- all candidate columns should be sequential.
> ie. no columns contatining other information should exist between two candidate names, EVEN if those are candidates of different classes/cohorts.

- The code can be run multiple times on multiple files, but as long as the above is true, it will identify the candidates and voters of each class and spew-out the winners.

### Voters Don't Have to be Sequential
rows represent a ballot/vote. Voters can be in any order, as long as column 0 is class IDs.

### Voters Not Spoiling Their Ballots Must Rank *_ALL_* Candidates
it's how our voting works. If it ever changes, changes have to be made to the code.
> these changes include, but may not be limited to:
> - the way `run_schulze.py` counts votes
> - the way `asm_vote_counter.py` recognizes candidate columns



## What's In Here?
#### Exists:

- `vote-core`
> This is the core of the code – an implementation of the election method.
> - originally from: https://github.com/bradbeattie/python-vote-core
> - there's a Py3 version: https://pypi.org/project/python3-vote-core/
> - the authors say it isn't "clean" though, but works.


- `pygraph`
> This is required for `vote-core`. Why? IDK. Uses the algorithms in it.

> - originally from https://github.com/pmatiello/python-graph
> - updated version exist in: https://github.com/Shoobx/python-graph
> honestly, I haven't tested the new version. May break everything.

- `asm_vote_counter.py`
> - asks for the first column in the CSV that has candidate names
> - asks for number of desired winners
> - calls `run_shulze.py` on each class ballot
> > ie. it recognizes in a larger CSV which lines belond to each class
> >	as well as the corrosponding cadidates.

- `run_schulze.py`
> counts the ballots and runs the schulz method on the data

- `UI_elements.py`
> Containes code for the buttons and pop-ups
> uses Tk and Tkinter, which will require updating in Python 3

#### Missing:
- Processing from Excel to csv


##### Cautionary Note (Roiman, M19, 2019)
Honestly, I don't know all of the ins and outs of this code. It works. It worked when we needed it to work. But it's one of those "sold as-is" things. Schultze is definitely an awesome method. But maybe get some CS majors to rebuild it.

## Dependencies:
The code used by the ASM has several dependencies. These include `python-vote-core` and `python-graph-master`. These cant be found with pip, as far as I could tell, and we definitely should re-work them ASAP.