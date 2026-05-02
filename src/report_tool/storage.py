from pathlib import Path

def save_report(text: str, filepath: str) -> Path:
    """Public: Saves text to the exact file path specified."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True) # Ensure directory exists
    path.write_text(text, encoding="utf-8")
    return path

def read_file(filepath: str | Path) -> str:
    """Public: Reads a file from disk."""
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Cannot read file: {path.absolute()}")
    return path.read_text(encoding="utf-8")

if __name__ == "__main__":
    print("storage.py — report persistence utilities")
