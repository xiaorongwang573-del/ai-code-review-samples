from __future__ import annotations


def moving_average(values: list[float], window: int) -> list[float]:
    if window <= 0:
        raise ValueError("window must be a positive integer")
    if window > len(values):
        return []

    averages: list[float] = []
    for start in range(0, len(values) - window + 1):
        subset = values[start:start + window]
        averages.append(sum(subset) / window)

    return averages


def test_moving_average() -> None:
    assert moving_average([10, 20, 30, 40], 2) == [15, 25, 35]
    assert moving_average([10, 20, 30], 3) == [20]
    assert moving_average([10, 20], 3) == []

    try:
        moving_average([10, 20], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for window=0")


if __name__ == "__main__":
    test_moving_average()
    print(moving_average([10, 20, 30, 40], 2))
