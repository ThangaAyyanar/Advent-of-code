import re
# @dataclass
# class PassportModel:
    # byr:int     # (Birth Year)
    # iyr:int     # (Issue Year)
    # eyr:int     # (Expiration Year)
    # hgt:str     # (Height)
    # hcl:str     # (Hair Color)
    # ecl:str     # (Eye Color)
    # pid:str     # (Passport ID)
    # cid:int     # (Country ID)

MandatoryFields = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
valid_passports = 0

class PassportModel:
    pass

def validate_passport(model):
    for field in MandatoryFields:
        if field in model.__dict__:
            continue
        else:
            return False
    return True

def validate_passport_part2(model):

    valid_count = 0

    if int(model.byr) >= 1920 and int(model.byr) <=2002:
        valid_count += 1
    if int(model.iyr) >= 2010 and int(model.iyr) <=2020:
        valid_count += 1
    if int(model.eyr) >= 2020 and int(model.eyr) <=2030:
        valid_count += 1

    measurement = model.hgt[-2:]
    if measurement == "cm":
        height = model.hgt[:-2]
        if int(height) >= 150 and int(height) <= 193:
            valid_count += 1
    elif measurement == "in":
        height = model.hgt[:-2]
        if int(height) >= 59 and int(height) <= 76:
            valid_count += 1

    if re.search(r'^#[0-9a-f]{6}',model.hcl):
        valid_count += 1

    valid_eye_color = ["amb","blu","brn","gry","grn","hzl","oth"]
    if model.ecl in valid_eye_color:
        valid_count += 1

    if len(model.pid) == 9:
        valid_count += 1

    return (valid_count == 7)

def parse_block(block):
    # print(block)
    block_split = block.split()
    model = PassportModel()
    for param in block_split:
        param_split = param.split(":")

        if param_split[0] == "byr":
            model.byr = int(param_split[1])
        elif param_split[0] == "iyr":
            model.iyr = int(param_split[1])
        elif param_split[0] == "eyr":
            model.eyr = int(param_split[1])
        elif param_split[0] == "hgt":
            model.hgt = param_split[1]
        elif param_split[0] == "hcl":
            model.hcl = param_split[1]
        elif param_split[0] == "ecl":
            model.ecl = param_split[1]
        elif param_split[0] == "pid":
            model.pid = param_split[1]
        elif param_split[0] == "cid":
            model.cid = int(param_split[1])

    return model

def main():
    global valid_passports
    valid_passports_part2 = 0
    with open("input.txt") as inputFile:

        block = ""

        for line in inputFile:
            if line == "\n":
                model = parse_block(block)
                if validate_passport(model):
                    valid_passports += 1
                if validate_passport(model) and validate_passport_part2(model):
                    valid_passports_part2 += 1
                block = ""
            elif block == "":
                block = line.strip()
            else:
                block = f'{block} {line.strip()}'

        # parse last line
        if block != "":
            model = parse_block(block)
            if validate_passport(model):
                valid_passports += 1
            if validate_passport(model) and validate_passport_part2(model):
                valid_passports_part2 += 1

        print(f"valid passports {valid_passports}")
        print(f"valid passports part2 {valid_passports_part2}")

if __name__ == "__main__":
    main()
