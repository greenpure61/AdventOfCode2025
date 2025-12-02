# main.py

from pathlib import Path


from days.day01_solution import Day01
from days.day02_solution import Day02
# Når du laver day02.py, kan du tilføje:
# from days.day02 import Day02

PROJECT_ROOT = Path(__file__).parent
INPUT_DIR = PROJECT_ROOT / "inputs"
OUTPUT_FILE = PROJECT_ROOT / "results.txt"


def run_all_days():
    # Registrér de dage du har lavet her
    days = [
        (1, Day01),
        (2, Day02),
        # ...
    ]

    lines_out = []

    for day_number, day_class in days:
        input_path = INPUT_DIR / f"day{day_number:02}.txt"

        if not input_path.exists():
            lines_out.append(f"Day {day_number:02}: MANGLEDE INPUT-FIL ({input_path.name})")
            continue

        with input_path.open(encoding="utf-8") as f:
            lines = f.readlines()

        day = day_class(lines)  # <-- instansér klassen

        part1 = day.solve_part1()
        part2 = day.solve_part2()

        lines_out.append(f"Day {day_number:02} - Part 1: {part1}")
        lines_out.append(f"Day {day_number:02} - Part 2: {part2}")
        lines_out.append("")  # tom linje mellem dage

    OUTPUT_FILE.write_text("\n".join(lines_out), encoding="utf-8")
    print(f"Resultater skrevet til: {OUTPUT_FILE}")


if __name__ == "__main__":
    run_all_days()
