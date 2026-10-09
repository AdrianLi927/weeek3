Create a test python program to count high heartrate streaks:

You will fill in 2 files - `vitals.py` and `main.py`

`vitals.py` will contain 2 importable functions - `streak_over_threshold` and `generate_sample`
- `streak_over_threshold(readings_bpm: list[int], threshold_bpm: int, reading_interval_s: int) -> int`: `readings_bpm` will take in the heartrate readings, these readings were measured once every `reading_interval_s`. The function will return the time of the longest streak (`highest_streak * reading_interval_s`). If a reading from `readings_bpm` is `<0` or `>250` then it is considered an artifact and will be normalised by linear interpolation between the nearest neighbours (and if none then the neighbour will be treated as 0). An empty list of `readings_bpm` or a `threshold_bpm` that would be treated as an artifact will raise a `ValueError`
- `generate_sample(length: int, longest_streak: int, threshold: int, num_above_threshold: int) -> list[int]` will generate a fake pseudo random sample readings_bpm with the specified inputs and will also have a variety of readings that are artifacts, on the edge of artifacts and contain other values above the threshold but making sure that the longest streak is still as specified. It should `ValueError` if `num_above_threshold` is less than `longest_streak` or than `length`.

`main.py` will contain a test with `generate_sample` first, print "all checks passed", and print the result of `streak_over_threshold` on a predetermined sample.
The tests will contain in this order (use try except where errors are expected):
- An empty recording
- Only artifacts
- Everything exactly on the threshold
- Nothing above the threshold
- 3 tests using `generate_samples` with assert statements, these can pass with a 5% tolerance on the expected result, they will test for the expected longest streak time by first a generic one, one with all values above the threshold or invalid, and one with all values below the threshold or invalid
Then finally it will print the longest streak of high heartrate with
```python
readings = [96, 104, 108, 112, 99, 101, 103, 107, 0, 110,
            115, 98, 102, 300, 105, 109, 111, 97]
interval_s = 10
```
along with units.

There is no extra information in the other files in the folder. Do not check or edit them.

Make no mistakes.

