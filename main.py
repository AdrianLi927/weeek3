"""Validation checks for the vitals streak logic."""

from __future__ import annotations

from vitals import generate_sample, streak_over_threshold


def run_edge_checks() -> None:
    """Exercise the expected edge conditions and their error handling."""
    try:
        streak_over_threshold([])
        raise AssertionError("Empty input should raise ValueError")
    except ValueError:
        pass

    try:
        streak_over_threshold([300, -1, 275, 400, 999])
        raise AssertionError("All-artifact input should raise ValueError")
    except ValueError:
        pass

    limit_readings = [100, 100, 100, 100, 100]
    assert streak_over_threshold(limit_readings, threshold_bpm=100) == 5

    below_threshold = [99, 98, 97, 96, 95]
    assert streak_over_threshold(below_threshold, threshold_bpm=100) == 0


def run_generated_assertions() -> None:
    """Check three independent generated samples with a 5% tolerance."""
    samples = [
        (generate_sample(320, 110, 100), 110, 100),
        (generate_sample(480, 160, 120), 160, 120),
        (generate_sample(600, 200, 90), 200, 90),
    ]

    for readings, expected_count, threshold in samples:
        actual = streak_over_threshold(readings, threshold_bpm=threshold)
        tolerance = 0.05 * expected_count
        assert abs(actual - expected_count) <= tolerance, (
            f"Expected {expected_count} with tolerance {tolerance}, got {actual}"
        )


def main() -> None:
    """Run the checks and print the final sample result."""
    run_edge_checks()
    run_generated_assertions()
    print("\033[92mall checks passed\033[0m")

    readings_bpm = [96, 104, 108, 112, 99, 101, 103, 107, 0, 110, 115, 98, 102, 300, 105, 109, 111, 97]
    result = streak_over_threshold(readings_bpm)
    print(f"Longest streak with readings_bpm = {readings_bpm}: {result}")


if __name__ == "__main__":
    main()
