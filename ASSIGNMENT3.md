# Assignment 3 — Orchestrate one step, and prove it works

**Due before Monday's lecture. Submit on Moodle. Submission is anonymous: put no name in any file.**

## The question

A patient was monitored during exercise, one reading every 10 seconds:

```python
readings = [96, 104, 108, 112, 99, 101, 103, 107, 0, 110,
            115, 98, 102, 300, 105, 109, 111, 97]
interval_s = 10
```

**What was the longest unbroken stretch of readings above 100 bpm?** The answer is a count of readings, not a percentage.

As in the tutorial: a reading of 0 is a dropped sample, and anything above 250 bpm is an artefact. Neither is a measurement.

## What you have to decide

The tutorial decided everything for you. This time one decision is genuinely yours, and it changes the answer:

> **Does a dropped sample break the stretch, or is it simply skipped?**

A gap of 10 seconds in the middle of a hard effort is arguably nothing. A gap of ten minutes is arguably a different stretch. There is no right answer, there is only a decision — and a decision nobody wrote down is the thing this course exists to prevent.

Choose, say so in your prompt, and say why in your README.

## What to do

1. **SPECIFY the signature.** Something like `longest_run_above(readings: list, limit_bpm: float) -> int`. Units in the names, and the part after `->` says what comes back — here a count of readings, not a percentage.
2. **SPECIFY the prompt.** State every decision: dropped samples, artefacts, a reading exactly on the limit, a recording with no valid readings, and your answer to the question above. Ask for type hints and a docstring giving the units.
3. **Order the body** and put it in a module of your own — one `.py` file, definitions only, no `print` at the bottom.
4. **SPECIFY and order a generator** so that you can build a recording whose answer you already know. For example: *n_total valid readings, with exactly one stretch of run_length readings above the limit and no longer stretch anywhere*. 
5. **DIAGNOSE**, in `main.py`, in this order:
   - the **edges**: an empty recording, only dropped samples, everything exactly on the limit, nothing above the limit at all. Use `try` / `except` where you specified an error;
   - **data you built**: at least three `assert` lines using the generator, each with a tolerance, each with a comment saying what it is for;
   - **then**, last, the real recording above, printed with its units.
6. `main.py` must print `all checks passed` before it prints the answer.

## What to submit

1. `main.py` — the orchestrator: data, calls, checks, result. It must run.
2. your **module** — the step and the generator, exactly as the assistant wrote them.
3. `README.md` — use the template: both prompts exactly as you sent them; your answer to the decision above and why; what the assistant decided that you had not; one line per check.
4. the **transcript**, from the first prompt to the last.