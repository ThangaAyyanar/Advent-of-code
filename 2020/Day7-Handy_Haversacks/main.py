from collections import defaultdict,deque

filename = "input.txt"
# filename = "test.txt"

target = "shinygoldbag"
parent = defaultdict(list)
content = defaultdict(list)

def size(bag):
    count = 1
    for (n,another_bag) in content.get(bag,[]):
        count += n*size(another_bag)
    return count

def main():
    with open(filename) as inputFile:
        all_data = inputFile.readlines()
        for data in all_data:
            data = data.strip()
            space_split = data.split()
            container = space_split[0] +space_split[1]+space_split[2]
            idx = 4
            while idx < len(space_split):

                if space_split[idx] == 'no':
                    break

                n = int(space_split[idx])
                bag = space_split[idx+1]+space_split[idx+2]+space_split[idx+3]
                if bag[-1] == '.' or bag[-1] == ',':
                    bag = bag[:-1]
                if bag[-1]=='s':
                    bag = bag[:-1]
                if container[-1]=='s':
                    container = container[:-1]
                parent[bag].append(container)
                content[container].append([n,bag])
                idx += 4
        # print(parent)
    SEEN = set()
    visit = deque([target])

    while len(visit) > 0:
        current = visit.popleft()
        if current in SEEN:
            continue
        SEEN.add(current)
        visit += parent[current]

    # print(SEEN)
    print(len(SEEN)-1)
    print(size(target)-1)



if __name__ == "__main__":
    main()
