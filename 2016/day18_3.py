# http://adventofcode.com/2016/day/18
# Faster version of Part 2

ROW1 = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
ROWS = 400000

def main():

    grid = [c for c in ROW1]
    next_grid = [0 for c in range(len(ROW1))]

    count = 0
    count += sum(map(lambda t: 1 if t == '.' else 0, grid))

    for row in range(1, ROWS):
        for col in range(len(ROW1)):

            parent_left_trap = col > 0 and grid[col - 1] == '^'
            parent_center_trap = grid[col] == '^'
            parent_right_trap = col < (len(ROW1) - 1) and grid[col + 1] == '^'

            if parent_left_trap and parent_center_trap and not parent_right_trap:
                next_grid[col] = '^'
            elif parent_center_trap and parent_right_trap and not parent_left_trap:
                next_grid[col] = '^'
            elif parent_left_trap and not parent_center_trap and not parent_right_trap:
                next_grid[col] = '^'
            elif parent_right_trap and not parent_left_trap and not parent_center_trap:
                next_grid[col] = '^'
            else:
                next_grid[col] = '.'
                count += 1


        # Swap the ptrs
        temp = grid
        grid = next_grid
        next_grid = temp

    print count

main()