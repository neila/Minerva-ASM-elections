# ASM_Elections_Code

## IMPORTANT
Before using this to actually run an election, read the segment on preparing the data for processing. Results will be incorrect otherwise.

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
> counts the vallot and runs the schulz method on the data

- `UI_elements.py`
> Containes code for the buttons and pop-ups
> uses Tk and Tkinter, which will require updating in Python 3

#### Missing:
- Processing from Excel to csv
> which is...

##### Cautionary Note (Roiman, M19, 2019)
Honestly, I don't know all of the ins and outs of this code. It works. It worked when we needed it to work. But it's one of those "sold as-is" things. Schultze is definitely an awesome method. But maybe get some CS majors torebuild it.

## Dependencies:
The code used by the ASM has several dependencies. These include `python-vote-core` and `python-graph-master`. These cant be found with pip, as far as I could tell, and we definitely should re-work them ASAP.