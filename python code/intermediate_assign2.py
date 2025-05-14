# intermediate_generator.py
def generate_intermediate():
    with open("input.txt", "r") as code:
        lines = code.readlines()

    flag = False

    with open("intermediate.txt", "w") as intermediate:
        for line in lines:
            tokens = line.strip().split()
            if not tokens:
                continue

            if tokens[0] == "MACRO":
                flag = True
            elif tokens[0] == "MEND":
                flag = False
            elif not flag:
                intermediate.write(line)

generate_intermediate()
