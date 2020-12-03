counter=0

def validate_password(condition,character,password):

    character_count = 0
    for pass_char in password:
        if pass_char == character:
            character_count += 1

    return character_count >= int(condition[0]) and character_count <= int(condition[1])

def validate_password2(condition,character,password):

    startIndex = int(condition[0]) - 1
    endIndex = int(condition[1]) - 1

    if password[startIndex] == character and password[endIndex] == character:
        return False
    elif password[startIndex] == character or password[endIndex] == character:
        return True
    else:
        return False


def get_data(input_data):
    space_seperated_string = input_data.split()

    limit = space_seperated_string[0].split("-")
    character = space_seperated_string[1].split(":")[0]
    input_string = space_seperated_string[2]

    # print(f"limit {limit}\ncharacter {character}\nString {input_string}")
    return (limit,character,input_string)


def main():
    global counter
    with open("input.txt") as inputFile:
        for line in inputFile:
            limit,character,input_string = get_data(line)
            if validate_password2(limit,character,input_string):
                counter += 1

        print(f"counter {counter}")


if __name__ == "__main__":
    main()
