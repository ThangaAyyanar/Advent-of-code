
highest_seat_number = 0
seat_location = [ [0]*8 for i in range(128)]

def parse_seat(order):
    global highest_seat_number
    row_start = 0
    row_end = 127
    col_start = 0
    col_end = 7
    for letter in order:
        if letter == 'F':
            row_end = int((row_start+row_end)/2)
        elif letter == 'B':
            row_start = int((row_start+row_end)/2) + 1
        if letter == 'L':
            col_end = int((col_start+col_end)/2)
        elif letter == 'R':
            col_start = int((col_start+col_end)/2) + 1
    # print(f"Row {row_start} {row_end} and columns {col_start} {col_end}")
    # print(f"Seat number {row_start*8+col_start}")
    seat_location[row_start][col_start] = 1
    current_seat_number = row_start*8+col_start
    if highest_seat_number < current_seat_number:
        highest_seat_number = current_seat_number


def main():
    with open("input.txt") as inputFile:
        for line in inputFile:
            parse_seat(line)
        #part2
        for seat in seat_location:
            print(seat)
        #part1
        print(f"Highest seat number {highest_seat_number}")

if __name__ == "__main__":
    main()

