grid = []

def part1():
    number_of_trees = 0
    x = 0
    y = 0
    while y < len(grid)-1: #y is 0 indexed
        x += 3
        y += 1
        # print(f"Indexes {y},{x%len(grid[0])}")
        if grid[y][x%len(grid[0])] == '#':
            number_of_trees += 1

    print(f"Number of trees {number_of_trees}")

def part2():

    answer = 1
    given_slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for gx,gy in given_slopes:
        x = 0
        y = 0
        number_of_trees = 0
        while y < len(grid)-1:
            x += gx
            y += gy
            if grid[y][x%len(grid[0])] == '#':
                number_of_trees += 1
        answer *= number_of_trees
    print(f"Answer {answer}")

def main():
    with open("input.txt") as inputFile:
        for line in inputFile:
            grid.append(line.strip())
        part1()
        part2()

if __name__ == "__main__":
    main()
