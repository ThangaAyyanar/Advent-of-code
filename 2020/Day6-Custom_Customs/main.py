overall = []

#part 1
def get_group_data(group):
        unique_answers = set()
        group_split = group.split("\n")
        for line in group_split:
            unique_answers.update(list(line))
        overall.append(unique_answers)

#part2
def get_group_data_part2(group):
        unique_answers = set()
        group_split = group.split("\n")
        if group_split[0] is None:
            print("None")
        unique_answers.update(list(group_split[0]))
        for index in range(1,len(group_split)):
            unique_answers = unique_answers & set(list(group_split[index])) # set intersection
        overall.append(unique_answers)


def main():
    global overall
    with open("input.txt") as inputFile:
        all_input = inputFile.read()
        group_sum = 0
        seperate_groups = all_input.split("\n\n") # Ensure last line has extra new line or last group is not taken into account
        for group in seperate_groups:
            # get_group_data(group)
            get_group_data_part2(group)
        # print(overall)
        for group in overall:
            group_sum += len(group)
        print(group_sum)

if __name__ == "__main__":
    main()


