from typing import List, Tuple


def rotate(polyomino: List[str]) -> List[List[str]]:
    """
    Generate all possible rotations of the given polyomino.
    """
    rotations = [polyomino]
    for _ in range(3):
        polyomino = [''.join(x[::-1]) for x in zip(*polyomino)]
        rotations.append(polyomino)
    return rotations


def trim(polyomino: List[str]) -> List[str]:
    """
    Trim the empty rows and columns around the polyomino to get the minimal representation.
    """
    rows = [row for row in polyomino if '#' in row]
    if not rows:
        return []
    min_col = min(row.index('#') for row in rows)
    max_col = max(max(i for i, c in enumerate(row) if c == '#') for row in rows)
    return [row[min_col:max_col + 1] for row in rows]


def can_place(grid: List[List[str]], polyomino: List[str], row: int, col: int) -> bool:
    """
    Check if the polyomino can be placed on the grid at the given position without overlapping and going out of bounds.
    """
    if row + len(polyomino) > 4 or col + len(polyomino[0]) > 4:
        return False

    for r, prow in enumerate(polyomino):
        for c, cell in enumerate(prow):
            if cell == '#' and grid[row + r][col + c] == '#':
                return False
    return True


def place(grid: List[List[str]], polyomino: List[str], row: int, col: int):
    """
    Place the polyomino on the grid at the given position. Assumes can_place() is already checked and is True.
    """
    for r, prow in enumerate(polyomino):
        for c, cell in enumerate(prow):
            if cell == '#':
                grid[row + r][col + c] = '#'


def is_grid_full(grid: List[List[str]]) -> bool:
    """
    Check if the grid is fully covered by polyominos.
    """
    return all(cell == '#' for row in grid for cell in row)


def solve(polyominos: List[List[str]]) -> str:
    # Generate all possible rotations of the polyominos and trim them to minimal representation
    polyominos_rotations = [rotate(trim(polyomino)) for polyomino in polyominos]

    # Try all combinations of rotations and positions for the three polyominos
    for poly1 in polyominos_rotations[0]:
        for r1 in range(4):
            for c1 in range(4):
                grid = [['.' for _ in range(4)] for _ in range(4)]
                if not can_place(grid, poly1, r1, c1):
                    continue
                place(grid, poly1, r1, c1)

                for poly2 in polyominos_rotations[1]:
                    for r2 in range(4):
                        for c2 in range(4):
                            grid2 = [row[:] for row in grid]
                            if not can_place(grid2, poly2, r2, c2):
                                continue
                            place(grid2, poly2, r2, c2)

                            for poly3 in polyominos_rotations[2]:
                                for r3 in range(4):
                                    for c3 in range(4):
                                        grid3 = [row[:] for row in grid2]
                                        if not can_place(grid3, poly3, r3, c3):
                                            continue
                                        place(grid3, poly3, r3, c3)

                                        if is_grid_full(grid3):
                                            return "Yes"
    return "No"


polyominos = []
for i in range(3):
    polyomino = [input() for _ in range(4)]
    polyominos.append(polyomino)

print(solve(polyominos))
