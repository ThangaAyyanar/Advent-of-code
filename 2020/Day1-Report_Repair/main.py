
total_sum = 2020

## Part 1
def main():

    with open("input.txt") as inputFile:

        input_data = inputFile.readlines()
        limit = range(len(input_data))
        for index_i in limit:
            i_value = int(input_data[index_i])
            for index_j in limit:
                j_value = int(input_data[index_j])
                if (i_value + j_value) == total_sum:
                    print(f'ith iteration value {i_value},{j_value}')
                    print(i_value*j_value)
                    return

## Part 2
def part2():

    with open("input.txt") as inputFile:

        input_data = inputFile.readlines()
        limit = range(len(input_data))
        for index_i in limit:
            i_value = int(input_data[index_i])
            for index_j in limit:
                j_value = int(input_data[index_j])
                for index_k in limit:
                    k_value = int(input_data[index_k])
                    if (i_value + j_value + k_value) == total_sum:
                        print(f'ith iteration value {i_value},{j_value},{k_value}')
                        print(i_value*j_value*k_value)
                        return


if __name__ == "__main__":
    part2()
