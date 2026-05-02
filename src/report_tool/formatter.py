import json

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
    base_report = build_report(stats)
    return f"{base_report}\n{_line('sorted', sorted(numbers))}"

def build_json_report(stats: dict) -> str:
    """Public: Builds a structured JSON report."""
    return json.dumps(stats, indent=4)


def _title(text: str) -> str:
    return text.strip().title()

def _line(name: str, value) -> str:
    return f"{name}: {value}"

if __name__ == "__main__":
    print("formatter.py — report formatting utilities")
