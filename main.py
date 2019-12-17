def calc(Day2):
    i = 0
    while Day2[i] != 99: #look for the exit code
        print('...')
        if Day2[i] == 1: # 1 for +
            print('more gravity...')
            Day2[Day2[i + 3]] = Day2[Day2[i + 2]] + Day2[Day2[i + 1]]
        elif Day2[i] == 2: # 2 for *
            print('fold gravity...')
            Day2[Day2[i + 3]] = Day2[Day2[i + 2]] * Day2[Day2[i + 1]]
        else:
            print('Not Gravity, exiting until heat death')
            break
        i += 4
    return Day2[0]


def main():
    input_text = open("day_2_input.txt").read().splitlines()[0]
    data = [int(val) for val in input_text.split(",")]
    data[1] = 12
    data[2] = 2
    calc(data)
    print('Answer is: ', data[0])


if __name__ == "__main__":
    main()