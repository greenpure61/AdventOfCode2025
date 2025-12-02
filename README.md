# 🎄 Advent of Code 2025 – Python Solutions

Dette repository indeholder mine løsninger til **Advent of Code 2025**, organiseret dag-for-dag i et struktureret Python-projekt.  
Alle opgaver kan køres samlet via `main.py`, som samtidig skriver resultaterne til `results.txt`.

Projektet er sat op med fokus på:

- klar og skalerbar struktur  
- nem udvidelse med nye dage  
- genkørsel af hele kalenderen på én gang  
- én inputfil og én beskrivelsesfil pr. dag  

---

## 📁 Projektstruktur

```text
advent_of_code_2025/
│
├─ main.py
├─ README.md
│
├─ days/
│   ├─ __init__.py
│   ├─ day01_solution.py
│   ├─ day02_solution.py
│   └─ ... (én fil pr. dag)
│
├─ inputs/
│   ├─ day01.txt
│   ├─ day02.txt
│   └─ ... (én puzzle input pr. dag)
│
└─ descriptions/
    ├─ day01.txt
    ├─ day02.txt
    └─ ... (én opgavebeskrivelse pr. dag)

```

- **`days/`** indeholder én klasse pr. dag (`Day01`, `Day02`, …)  
- **`inputs/`** indeholder puzzle input for hver dag  
- **`main.py`** loader alle dag-klasser, kører dem og skriver resultater til `results.txt`  

---

## ▶️ Kør løsningerne

Projektet kræver **Python 3.10+**.

### 1. Opret virtual environment (valgfrit, men anbefales)

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```

### 2. Kør alle dage

```bash
python main.py
```

### 3. Resultater

Output skrives til:

```
results.txt
```

Formatet:

```
Day 01 - Part 1: xxxx
Day 01 - Part 2: xxxx

Day 02 - Part 1: xxxx
Day 02 - Part 2: xxxx

...
```

---

## ➕ Tilføj en ny dag

### 1. Opret en ny fil i `days/`

```
days/day03_solution.py
```

### 2. Tilføj en klasse

```python
class Day03:
    def __init__(self, lines):
        self.lines = [line.strip() for line in lines]

    def solve_part1(self):
        return 0  # TODO

    def solve_part2(self):
        return 0  # TODO
```

### 3. Registrér dagen i `main.py`

```python
from days.day03_solution import Day03

days = [
    (1, Day01),
    (2, Day02),
    (3, Day03),
]
```

### 4. Opret inputfil

```
inputs/day03.txt
```

Kør `python main.py` igen — done.

---

## 🧠 Designfilosofi

### Klasse-baseret struktur
Hver dag har sin egen klasse, så parsing, part 1 og part 2 holdes samlet og overskueligt.

### Modulær og udvidbar opsætning
`main.py` fungerer som entry point og håndterer:

- loading af inputs  
- instansiering af dag-klasser  
- kørsel af part 1 & 2  
- output til `results.txt`

### Performance-venlig
Selv dage med store ranges (fx Day 2) er optimeret via matematisk generering frem for brute force iteration.

---

## ⭐ Advent of Code

Opgaverne kommer fra:  
https://adventofcode.com/2025  
*(support the creator!)*

---

**Glædelig jul — og god kodejagt 🎅✨**
