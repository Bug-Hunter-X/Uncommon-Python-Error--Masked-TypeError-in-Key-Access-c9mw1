# Uncommon Python Error: Masked TypeError in Key Access

This repository demonstrates a subtle bug in Python that can be easily missed. The function `function_with_uncommon_bug` attempts to access and multiply a dictionary's value, handling `KeyError` and `TypeError` exceptions.  However, the `TypeError` handling can mask a problem if the 'key' exists but its value cannot be multiplied (e.g., it's a string).

The bug is subtle because the code appears to handle all possible failures.  But a more robust solution would involve improved input validation to prevent the TypeError in the first place.

## How to run

1. Clone this repository.
2. Run `bug.py` to see the output of the function with different inputs.
3. Run `bugSolution.py` to see an improved version of the function.