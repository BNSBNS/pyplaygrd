grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', 'x']]

# rotate 90 degree, technically, get each index 1 at row, and print it, so [0][0] print first then, next row first col [1][0], and etc etc

for row in range(len(grid[0])):

    for column in range(len(grid)):
        print(grid[column][row], end='')
    print()