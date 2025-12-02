# days/day02_solution.py

from bisect import bisect_left, bisect_right


class Day02:
    def __init__(self, lines: list[str]):
        # Input kan være wrapped over flere linjer, så vi samler dem
        joined = "".join(line.strip() for line in lines if line.strip())
        parts = [p for p in joined.split(",") if p]  # fjern evt. tomme entries

        ranges: list[tuple[int, int]] = []
        for part in parts:
            start_str, end_str = part.split("-")
            ranges.append((int(start_str), int(end_str)))

        self.ranges = ranges

    # ---------- Generator til DEL 1: præcis to gentagelser ----------

    def _generate_invalid_ids_exactly_twice(self) -> list[int]:
        """
        Generér alle tal op til max_r, der er på formen:
        n = a * 10^k + a
        hvor a har k cifre (ingen leading zeros).
        """
        max_r = max(r[1] for r in self.ranges)
        max_digits = len(str(max_r))

        invalid_ids: list[int] = []

        # total længde = 2k, så 2k <= max_digits  => k <= max_digits // 2
        for k in range(1, max_digits // 2 + 1):
            start = 10 ** (k - 1)      # første a med k cifre
            end = 10 ** k              # eksklusiv
            mul = 10 ** k

            for a in range(start, end):
                n = a * mul + a
                if n > max_r:
                    break
                invalid_ids.append(n)

        invalid_ids.sort()
        return invalid_ids

    # ---------- Generator til DEL 2: mindst to gentagelser ----------

    def _generate_invalid_ids_at_least_twice(self) -> list[int]:
        """
        Generér alle tal op til max_r, der er på formen:
        n = int(str(a) * m)
        hvor:
          - a har k cifre (ingen leading zeros)
          - m >= 2
          - k * m <= max_digits
        Duplicates fjernes via set (fx '1111' kan være 1×4 eller 11×2).
        """
        max_r = max(r[1] for r in self.ranges)
        max_digits = len(str(max_r))

        ids_set: set[int] = set()

        # k = længde af blok (antal cifre)
        # mindst 2 gentagelser => 2*k <= max_digits  ⇒ k <= max_digits // 2
        for k in range(1, max_digits // 2 + 1):
            base_start = 10 ** (k - 1)   # første a med k cifre (ingen leading zero)
            base_end = 10 ** k           # eksklusiv

            for a in range(base_start, base_end):
                s = str(a)

                # m = antal gentagelser (mindst 2)
                # max_m så k * m <= max_digits
                max_m = max_digits // k

                for m in range(2, max_m + 1):
                    n_str = s * m
                    n = int(n_str)

                    if n > max_r:
                        break  # større m giver kun større n, så break

                    ids_set.add(n)

        invalid_ids = sorted(ids_set)
        return invalid_ids


    # ---------- Part 1 ----------

    def solve_part1(self) -> int:
        invalid_ids = self._generate_invalid_ids_exactly_twice()

        total = 0
        for L, R in self.ranges:
            i = bisect_left(invalid_ids, L)
            j = bisect_right(invalid_ids, R)
            total += sum(invalid_ids[i:j])

        return total

    # ---------- Part 2 ----------

    def solve_part2(self) -> int:
        invalid_ids = self._generate_invalid_ids_at_least_twice()

        total = 0
        for L, R in self.ranges:
            i = bisect_left(invalid_ids, L)
            j = bisect_right(invalid_ids, R)
            total += sum(invalid_ids[i:j])

        return total
