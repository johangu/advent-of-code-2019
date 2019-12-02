def part01(modules):
    return sum(int(x)//3 - 2 for x in modules)


def part02(modules):
    return sum(do_calculate(int(x)) for x in modules)


def do_calculate(x, acc=0):
    s = x//3 - 2
    if s <= 0:
        return acc
    else:
        return do_calculate(s, acc+s)


if __name__ == "__main__":
    with open('day01.input') as f:
        modules = f.readlines()

    print("part 1:", part01(modules))
    print("part 2:", part02(modules))
