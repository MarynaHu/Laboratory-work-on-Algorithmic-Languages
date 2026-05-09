def parse_numbers(text: str) -> list[float]:
    """Parse a comma-, semicolon-, or whitespace-separated string into a list of floats."""
    normalised = text.replace(",", " ").replace(";", " ")
    pieces = _clean_pieces(normalised.split())
    return [float(p) for p in pieces]
 
 
def _clean_pieces(parts: list[str]) -> list[str]:
    """Return stripped, non-empty tokens."""
    return [item.strip() for item in parts if item.strip() != ""]
 
 
if __name__ == "__main__":
    print("parser.py — number parsing utilities")
    print("-" * 36)
    print("Public functions:")
    print("  parse_numbers(text) — parse comma/semicolon/space-separated numbers")
    print()
    print("Example:")
    sample = "10, 20.5; 30 40"
    result = parse_numbers(sample)
    print(f'  parse_numbers("{sample}")')
    print(f"  => {result}")