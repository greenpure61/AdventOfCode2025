# days/day01.py

class Day01:
    def __init__(self, lines: list[str]):
        # Fjern tomme linjer og whitespace
        self.lines = [line.strip() for line in lines if line.strip()]

    def solve_part1(self) -> int:
        pos = 50
        zeros = 0

        for line in self.lines:
            direction = line[0]
            distance = int(line[1:])

            if direction == "L":
                pos = (pos - distance) % 100
            elif direction == "R":
                pos = (pos + distance) % 100
            else:
                raise ValueError(f"Ukendt retning: {direction}")

            if pos == 0:
                zeros += 1

        return zeros

    def solve_part2(self) -> int:
        pos = 50
        zeros = 0

        for line in self.lines:
            direction = line[0]
            distance = int(line[1:])

            # Beregn hvor mange gange vi rammer 0 under denne rotation
            if direction == "R":
                # pos(k) = pos + k  (mod 100)  ⇒  k ≡ -pos (mod 100)
                k0 = (-pos) % 100
            elif direction == "L":
                # pos(k) = pos - k  (mod 100)  ⇒  k ≡ pos (mod 100)
                k0 = pos % 100
            else:
                raise ValueError(f"Ukendt retning: {direction}")

            # Første klik må ikke være k=0, så hvis k0==0, jump til 100
            if k0 == 0:
                k_first = 100
            else:
                k_first = k0

            if k_first <= distance:
                zeros_this_rotation = 1 + (distance - k_first) // 100
            else:
                zeros_this_rotation = 0

            zeros += zeros_this_rotation

            # Opdater endelig position efter hele rotationen
            if direction == "R":
                pos = (pos + distance) % 100
            else:  # "L"
                pos = (pos - distance) % 100

        return zeros
