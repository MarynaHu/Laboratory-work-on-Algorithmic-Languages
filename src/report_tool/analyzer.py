def analyze(numbers: list[float]) -> dict[str, float]:
    
    _validate(numbers)
    total = sum(numbers)
    count = len(numbers)
    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": total / count,
    }


def _validate(numbers: list[float]) -> None:
    """Raise ValueError if the list is empty."""
    if not numbers:
        raise ValueError("numbers must not be empty")


if __name__ == "__main__":
    print("analyzer.py — statistical analysis utilities")
    print("-" * 44)
    print("Public functions:")
    print("  analyze(numbers) — compute count, sum, min, max, mean")
    print()
    print("Example:")
    sample = [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]
    result = analyze(sample)
    print(f"  analyze({sample})")
    print(f"  => {result}")
