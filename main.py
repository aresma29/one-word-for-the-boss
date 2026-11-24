from pathlib import Path
print((Path(__file__).parent / "entry.txt").read_text().strip())
