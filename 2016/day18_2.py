# http://adventofcode.com/2016/day/18

ROW1 = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
#ROW1 = ".^^.^.^^^^"
ROWS = 400000
#ROWS = 10

def main():

    grid = [None for x in range(ROWS)]
    for y in range(len(grid)):
        grid[y] = ['.' for i in range(len(ROW1))]

    grid[0] = [c for c in ROW1]

    count = 0
    count += sum(map(lambda t: 1 if t == '.' else 0, grid[0]))

    for row in range(1, len(grid)):
        for col in range(len(ROW1)):

            parent_left_trap = col > 0 and grid[row - 1][col - 1] == '^'
            parent_center_trap = grid[row - 1][col] == '^'
            parent_right_trap = col < (len(ROW1) - 1) and grid[row - 1][col + 1] == '^'

            if parent_left_trap and parent_center_trap and not parent_right_trap:
                grid[row][col] = '^'
            elif parent_center_trap and parent_right_trap and not parent_left_trap:
                grid[row][col] = '^'
            elif parent_left_trap and not parent_center_trap and not parent_right_trap:
                grid[row][col] = '^'
            elif parent_right_trap and not parent_left_trap and not parent_center_trap:
                grid[row][col] = '^'

        count += sum(map(lambda t: 1 if t == '.' else 0, grid[row]))

    print count

main()