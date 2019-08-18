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
- `python-graph-master`
> which is...
- `asm_vote_counter.py`
> which is...

#### Missing:
- UI
> which is...
- Processing from Excel to csv
> which is...

##### Cautionary Note (Roiman, M19, 2019)
Honestly, I don't know all of the ins and outs of this code. It works. It worked when we needed it to work. But it's one of those "sold as-is" things. Schultze is definitely an awesome method. But maybe get some CS majors torebuild it.

## Dependencies:
The code used by the ASM has several dependencies. These include `python-vote-core` and `python-graph-master`. These cant be found with pip, as far as I could tell, and we definitely should re-work them ASAP.