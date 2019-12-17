def calc(wl):
    for i in range(0, len(wl), 4):
        if wl[i] == 99:
            return wl
        elif wl[i] == 1: #Add the next 2 positions
            wl[wl[i + 3]] = wl[wl[i + 2]] + wl[wl[i + 1]]
        elif wl[i] == 2: #Multiply the next 2 positions
            wl[wl[i + 3]] = wl[wl[i + 2]] * wl[wl[i + 1]]
        else:
            raise ValueError('Unknown Opcode: ', wl[i])
    return wl[0]


def iterate(cp):
    for i1 in range(100):  # 0-99
        for i2 in range(100):
            wl = cp.copy()
            wl[1] = i1
            wl[2] = i2
            calc(wl)
            if wl[0] == 19690720:
                print('Answer is: ', 100 * i1 + i2)


def main():
    input_text = open("day_2_input.txt").read().splitlines()[0]
    data = [int(val) for val in input_text.split(",")]
    data2 = data.copy()
    data[1] = 12
    data[2] = 2
    calc(data)
    print('Answer is: ', data[0])
    iterate(data2)


if __name__ == "__main__":
    main()