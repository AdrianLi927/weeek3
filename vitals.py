"""Vitals helpers for streak detection over threshold-based readings."""

from __future__ import annotations

import random

__all__ = ["generate_sample", "streak_over_threshold"]


def generate_sample(length: int, above_count: int, threshold: int) -> list[int]:
    """Create a deterministic sample with a long region above the threshold."""
    if length <= 0:
        raise ValueError("length must be positive")
    if above_count < 0 or above_count > length:
        raise ValueError("above_count must be between 0 and length")

    rng = random.Random(length * 37 + above_count * 17 + threshold * 13)
    values: list[int] = [0] * length

    high_start = max(0, (length - above_count) // 2)
    high_end = high_start + above_count

    for idx in range(length):
        if high_start <= idx < high_end:
            values[idx] = threshold + rng.randint(1, 25)
        else:
            values[idx] = rng.randint(max(0, threshold - 40), threshold - 1)

    artifact_positions = {
        max(0, high_start - 1),
        min(length - 1, high_end),
        max(0, high_start // 2),
        min(length - 1, (high_end + length) // 2),
    }
    for pos in artifact_positions:
        if pos < length:
            values[pos] = 300 if rng.random() < 0.5 else -5

    return values


def _repair_artifacts(readings_bpm: list[int]) -> list[float]:
    """Replace out-of-range samples by linear interpolation using valid neighbors."""
    if not readings_bpm:
        raise ValueError("readings_bpm cannot be empty")

    repaired = [float(value) for value in readings_bpm]
    valid_indices = [idx for idx, value in enumerate(repaired) if 0 <= value <= 250]

    if not valid_indices:
        raise ValueError("readings_bpm must contain at least one valid value")

    for idx, value in enumerate(repaired):
        if 0 <= value <= 250:
            continue

        previous_valid = max((pos for pos in valid_indices if pos < idx), default=None)
        next_valid = min((pos for pos in valid_indices if pos > idx), default=None)

        if previous_valid is not None and next_valid is not None:
            start_value = repaired[previous_valid]
            end_value = repaired[next_valid]
            span = next_valid - previous_valid
            if span == 0:
                repaired[idx] = float(start_value)
            else:
                fraction = (idx - previous_valid) / span
                repaired[idx] = start_value + (end_value - start_value) * fraction
        elif previous_valid is not None:
            start_value = repaired[previous_valid]
            end_value = 0.0
            span = idx - previous_valid + 1
            if span == 0:
                repaired[idx] = 0.0
            else:
                fraction = (idx - previous_valid) / span
                repaired[idx] = start_value + (end_value - start_value) * fraction
        elif next_valid is not None:
            start_value = 0.0
            end_value = repaired[next_valid]
            span = next_valid - (-1)
            if span == 0:
                repaired[idx] = 0.0
            else:
                fraction = (idx - (-1)) / span
                repaired[idx] = start_value + (end_value - start_value) * fraction
        else:
            repaired[idx] = 0.0

    return repaired


def streak_over_threshold(
    readings_bpm: list[int],
    threshold_bpm: int = 100,
    reading_interval_s: int = 0,
) -> int:
    """Return the longest consecutive run of readings at or above threshold.

    Values outside the clinically valid range [0, 250] are treated as artifacts and are
    repaired by linear interpolation between the nearest valid samples. If only one side
    has valid data, the missing side is treated as zero during interpolation.
    """
    del reading_interval_s

    cleaned = _repair_artifacts(readings_bpm)
    longest_streak = 0
    current_streak = 0

    for value in cleaned:
        if value >= threshold_bpm:
            current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        else:
            current_streak = 0

    return longest_streak
