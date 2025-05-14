# mdt_generator.py
def generate_mdt():
    with open("input.txt", "r") as code:
        lines = code.readlines()

    flag = False
    mdtp = 0
    macro_name = ""
    fpTable = {}

    with open("mdt.txt", "w") as mdt:
        for line in lines:
            tokens = line.strip().split()
            if not tokens:
                continue

            if tokens[0] == "MACRO":
                flag = True
                macro_name = tokens[1]
                # build parameter mapping
                param_dict = {}
                if len(tokens) > 2:
                    for i in range(2, len(tokens)):
                        param_dict[tokens[i]] = f"#{i - 2}"
                fpTable[macro_name] = param_dict

            elif tokens[0] == "MEND":
                flag = False

            elif flag:
                param_dict = fpTable.get(macro_name, {})
                mdline = []
                for word in tokens:
                    mdline.append(param_dict.get(word, word))
                mdline.append(str(mdtp))
                mdt.write(" ".join(mdline) + "\n")
                mdtp += 1

generate_mdt()
