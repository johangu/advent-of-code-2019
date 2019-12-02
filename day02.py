def part01(ints, one, two):
    i = 0
    ints[1] = one
    ints[2] = two
    while i < len(ints):
        if ints[i] not in [1, 2, 99]:
            raise Exception("Something went wrong")
            break
        elif ints[i] == 99:
            break
        elif ints[i] == 1:
            ints[ints[i+3]] = ints[ints[i+1]] + ints[ints[i+2]]
        elif ints[i] == 2:
            ints[ints[i+3]] = ints[ints[i+1]] * ints[ints[i+2]]

        i += 4
    return ints


def part02(ints, needle):
    for noun in range(100):
        for verb in range(100):
            output = part01(list(ints), noun, verb)
            if output[0] == needle:
                return 100 * noun + verb


if __name__ == "__main__":
    with open('day02.input') as f:
        ints = [int(x.strip()) for x in f.readlines()[0].split(",")]

    print("part 1:", part01(list(ints), 12, 2)[0])
    print("part 2:", part02(list(ints), 19690720))
