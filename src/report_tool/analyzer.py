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
    if not numbers:
        raise ValueError("numbers must not be empty")

if __name__ == "__main__":
    print("analyzer.py — statistical analysis utilities")
