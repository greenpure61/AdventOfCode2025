# 🎄 Advent of Code 2025 – Python Solutions

Dette repository indeholder mine løsninger til *Advent of Code 2025*, organiseret dag-for-dag i et struktureret Python-projekt.  
Alle opgaver køres samlet via én `main.py`, som samtidig skriver resultaterne til en `results.txt`-fil.

Projektet er sat op med fokus på:
- klar struktur  
- nem udvidelse med nye dage  
- genkørsel af hele kalenderen på én gang  
- separat inputfil pr. dag  

---

## 📁 Projektstruktur

advent_of_code_2025/
│
├─ main.py
├─ README.md
│
├─ days/
│ ├─ init.py
│ ├─ day01_solution.py
│ ├─ day02_solution.py
│ └─ ... (én fil pr. dag)
│
└─ inputs/
├─ day01.txt
├─ day02.txt
└─ ... (én inputfil pr. dag)


- **`days/`** indeholder én klasse per dag (`Day01`, `Day02`, …).  
- **`inputs/`** indeholder puzzle-inputtet for hver dag.  
- **`main.py`** loader alle `DayXX`-klasser, kører `solve_part1()` og `solve_part2()`, og gemmer resultaterne i `results.txt`.

---

## ▶️ Kør løsningerne

Projektet kører med Python 3.10+.

1. Installér dependencies (ingen nødvendige, men et virtual environment anbefales):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate


2. Kør alle dage:
python main.py


3. Resultaterne gemmes automatisk i:
results.txt


Format i filen:
Day 01 - Part 1: xxxx
Day 01 - Part 2: xxxx

Day 02 - Part 1: xxxx
Day 02 - Part 2: xxxx

...

➕ Tilføj en ny dag

Opret en ny fil i days/, fx:

days/day03_solution.py


Lav en klasse med følgende struktur:

class Day03:
    def __init__(self, lines):
        self.lines = [l.strip() for l in lines]

    def solve_part1(self):
        return 0

    def solve_part2(self):
        return 0


Tilføj den i main.py:

from days.day03_solution import Day03

days = [
    (1, Day01),
    (2, Day02),
    (3, Day03),
]


Tilføj puzzle-input:

inputs/day03.txt


Run again — done.

🧠 Designfilosofi

Klasse-baseret struktur:
Hver dag er indkapslet i én klasse, hvilket gør det nemt at holde parsing, del 1 og del 2 samlet.

Modulær opsætning:
main.py er ansvarlig for orchestration, logging og output.

Performance-venlig:
Selv opgaver med store ranges (Day 2) genereres effektivt ved at beregne strukturerede tal i stedet for brute-force loops.

⭐ Advent of Code

Opgaverne kommer fra:
https://adventofcode.com/2025

(support the creator!)

God kodejagt og glædelig jul! 🎅✨