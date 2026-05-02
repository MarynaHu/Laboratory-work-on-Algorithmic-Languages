def parse_numbers(text: str) -> list[float]:
    normalized_text = text.replace(";", " ").replace(",", " ")
    pieces = normalized_text.split()
    return [float(p) for p in pieces]

if __name__ == "__main__":
    print("parser.py — number parsing utilities")