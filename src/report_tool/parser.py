def parse_numbers(text: str) -> list[float]:
    pieces = text.replace(";", ",").split(",")
    pieces = _clean_pieces(pieces)
    return [float(p) for p in pieces]


def _clean_pieces(parts: list[str]) -> list[str]:
    return [item.strip() for item in parts if item.strip() != ""]


if __name__ == "__main__":
    print("parser.py — number parsing utilities")
    print("-" * 36)
    print("Public functions:")
    print("  parse_numbers(text) — parse comma/semicolon-separated numbers")
    print()
    print("Example:")
    sample = "10, 20.5; 30, 40"
    result = parse_numbers(sample)
    print(f'  parse_numbers("{sample}")')
    print(f"  => {result}")
