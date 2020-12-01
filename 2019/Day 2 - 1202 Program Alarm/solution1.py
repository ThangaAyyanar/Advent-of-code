
program_code = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0]

# program_code = [1,9,10,3,2,3,11,0,99,30,40,50]

output = 19690720

print(f"Length of program_code {len(program_code)}")
length_of_program_code = len(program_code)

def valid_index(index):
    index+3 < length_of_program_code 

def perform_operation(index,length):
    
    if length > 3 and valid_index(index):

        opcode = program_code[index]
        input1 = program_code[index+1]
        input2 = program_code[index+2]
        output_index = program_code[index+3]
        
        # print(f"index:{index} {program_code[index]} {program_code[index+1]} {program_code[index+2]} {program_code[index+3]}")

        if opcode == 1:
            result = program_code[input1] + program_code[input2]
            program_code[output_index] = result
            return True
        elif opcode == 2:
            result = program_code[input1] * program_code[input2]
            program_code[output_index] = result
            return True
        else:
            return False

    else:
        return False


for index in range(0,length_of_program_code,4):
    if index + 1 > length_of_program_code:

        print(f"index:{index}")
        break

    if index + 2 > length_of_program_code:

        print(f"index:{index} {program_code[index]}")
        break

    if index + 3 > length_of_program_code:

        print(f"index:{index} {program_code[index]} {program_code[index+1]}")
        break

    if perform_operation(index,4):
        print("==============================================================")
        print(f"{program_code}")
        # print(f"index:{index} {program_code[index]} {program_code[index+1]} {program_code[index+2]} {program_code[index+3]}")

# print(f"The final result {program_code}")
