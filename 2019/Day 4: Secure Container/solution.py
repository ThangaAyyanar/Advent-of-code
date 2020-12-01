
# i/p: 367479-893698


def occurances(index,password_string):

    count = 1
    new_index = index
    current_word = password_string[index]
    while new_index < len(password_string):
        if current_word == password_string[new_index]:
            count += 1
        new_index += 1
    return count



def check_valid_password(password_string):
    has_double=False
    index = 1
    previous_char=int(password_string[0])

    while index < len(password_string):

        # print(f"{index} {previous_char} {password_string[index]}")
        int_char = int(password_string[index])
        if int_char < previous_char:
            return False
        elif int_char == previous_char:
            count = occurances(index,password_string)
            # print(f"Number of occurances {count}")
            if count % 2 == 0:
                has_double = True
            index += count - 1

            if index < len(password_string):
                    previous_char=int_char
            continue

        previous_char=int_char
        index += 1

    if has_double:
        return True
    else:
        return False


# password_string = str(111111)
# password_string = str(223450)
# password_string = str(123789)
# password_string = str(123444)
# print(check_valid_password(password_string))

number_of_valid_passwords = 0

for password in range(367479,893698):

    if check_valid_password(str(password)):
        print(password)
        number_of_valid_passwords += 1

print(f"Number of valid password {number_of_valid_passwords}")
