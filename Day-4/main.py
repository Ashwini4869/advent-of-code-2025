def parse_grid_file(filename: str):
    grid = []
    lines = None
    with open(filename, "r") as file:
        lines = file.readlines()

    for line in lines:
        grid.append(list(line.strip("\n")))

    return grid


def is_accessible(paper_roll_position, total_rows, total_cols, grid):
    current_i, current_j = paper_roll_position
    # print(f"Current element position: ({current_i},{current_j})")
    min_i = current_i if current_i == 0 else current_i - 1
    max_i = current_i if current_i >= (total_rows - 1) else current_i + 1
    i_range = [x for x in range(min_i, max_i + 1)]

    min_j = current_j if current_j == 0 else current_j - 1
    max_j = current_j if current_j >= (total_cols - 1) else current_j + 1
    j_range = [x for x in range(min_j, max_j + 1)]

    # print("i range", i_range)
    # print("j range", j_range)
    adjacent_elements_string = ""

    for i in i_range:
        for j in j_range:
            if (i, j) != (current_i, current_j):
                # print(f"Element at pos({i},{j}) is : {grid[i][j]}")
                adjacent_elements_string += grid[i][j]

    # print("Adjacent Elements String:", adjacent_elements_string)

    adjacent_paper_roll_count = adjacent_elements_string.count("@")

    if adjacent_paper_roll_count < 4:
        return True
    else:
        return False


def get_accessible_rolls(grid):
    total_columns = len(grid[0])
    total_rows = len(grid)
    accessible_rolls = []

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                if is_accessible((i, j), total_rows, total_columns, grid):
                    accessible_rolls.append((i, j))

    return accessible_rolls


def remove_accessible_rolls(grid, accessible_rolls):
    for roll in accessible_rolls:
        i, j = roll
        grid[i][j] = "x"
    return grid


def remove_accessible_rolls_recursively(grid):
    total_removed_rolls_count = 0

    while True:
        accessible_rolls = get_accessible_rolls(grid)
        if len(accessible_rolls) != 0:
            total_removed_rolls_count += len(accessible_rolls)
            grid = remove_accessible_rolls(grid, accessible_rolls)

        else:
            break

    return total_removed_rolls_count


if __name__ == "__main__":
    grid = parse_grid_file("input.txt")
    total_removed_rolls_count = remove_accessible_rolls_recursively(grid)
    print(f"Total removed rolls : {total_removed_rolls_count}")
