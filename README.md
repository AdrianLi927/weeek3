# Assignment 3

## 1. The step

<!-- The signature you specified, and one or two sentences on what it computes. -->

```
```

## 2. The prompt

<!-- Exactly as you sent it. If the first attempt came back wrong, paste both and
     say what was wrong with the first. -->

```
```

## 3. The decision

<!-- Does a dropped sample break the stretch, or is it skipped? What did you
     choose, and why? What would change in the answer if you had chosen the
     other way? -->

A dropped sample is linearly interpolated between its closest undropped neighbours, since a human heartrate doesnt usually suddenly dramatically jump very far over the span of 10 seconds it would probably safe to assume that for a real data set the dropped data's actual value would be somewhere in between the 2 neighbour undropped data points.


## 4. The generator

<!-- Its signature, the prompt you used, and what it has to guarantee for your
     checks to mean anything. -->
The signiture was not explicitly mentioned but the agent correctly infered that `length`, `above_count` and `threshold` should be integers and return should be `list[int]` based on the context of the first function.
```
```

## 5. The checks

| check | what it is for | passed? |
|---|---|---|
|  |  |  |

## 6. What the assistant decided that you had not

<!-- Read the "Decisions not in the spec" list if your assistant provides one,
     and look at the code for anything you did not ask for: rounding, ordering,
     what it does with an input you never mentioned. -->

It had decided to check other files despite telling it not to for 3 times, I should just move the files out the project folder next time..


## 7. The result

<!-- The number, with its units, and one sentence on whether it is plausible for
     a patient during exercise. -->
