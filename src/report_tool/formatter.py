def build_report(stats: dict) -> str:

    lines = [
        _title("Number Report"),
        "-" * 20,
        _line("count", stats["count"]),
        _line("sum", stats["sum"]),
        _line("min", stats["min"]),
        _line("max", stats["max"]),
        _line("mean", round(stats["mean"], 2)),
    ]
    return "\n".join(lines)


def build_sorted_report(numbers: list[float], stats: dict) -> str:
    lines = [
        _title("Number Report"),
        "-" * 20,
        _line("count", stats["count"]),
        _line("sum", stats["sum"]),
        _line("min", stats["min"]),
        _line("max", stats["max"]),
        _line("mean", round(stats["mean"], 2)),
        _line("sorted", sorted(numbers)),
    ]
    return "\n".join(lines)


def _title(text: str) -> str:
    return text.strip().title()


def _line(name: str, value) -> str:
    return f"{name}: {value}"


if __name__ == "__main__":
    print("formatter.py — report formatting utilities")
    print("-" * 42)
    print("Public functions:")
    print("  build_report(stats)                  — plain-text statistics report")
    print("  build_sorted_report(numbers, stats)  — report with sorted numbers")
    print()
    print("Example:")
    sample_stats = {"count": 3, "sum": 6.0, "min": 1.0, "max": 3.0, "mean": 2.0}
    print(build_report(sample_stats))
