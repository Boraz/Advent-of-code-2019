def main():
    input_text = open("day_2_input.txt").read().splitlines()[0]
    input_program = [int(val) for val in input_text.split(",")]
    archived_program = input_program.copy()

    #1202 restore
    input_program[1] = 12
    input_program[2] = 2
    run_program(input_program)
    print(f"Day 2, Pt 1: {input_program[0]}")

    for idx_a in range(99):
        for idx_b in range(99):
            program = archived_program.copy()
            program[1] = idx_a
            program[2] = idx_b
            run_program(program)
            if program[0] == 19690720:
                #print(f"Values for output 19690720: {idx_a}, {idx_b}")
                #print(f"100 * idx_a + idx_b = {100 * idx_a + idx_b}")
                print(f"Day 2, Pt 2: {100 * idx_a + idx_b}")

def run_program(program):
    for idx in range(0, len(program), 4):
        if program[idx] == 99: #End. No inputs
            return program
        elif program[idx] == 1: #Add. Take next two inputs as indices for values to add
            program[program[idx+3]] = program[program[idx+1]] + program[program[idx+2]]
        elif program[idx] == 2: #Multiply. Take next two inputs as incides for values to add
            program[program[idx+3]] = program[program[idx+1]] * program[program[idx+2]]
        else:
            raise ValueError(f"Unknown Opcode: {program[idx]}")

if __name__ == "__main__":
    main()