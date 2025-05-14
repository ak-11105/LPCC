IS = ['READ', 'ADD', 'MOVER', 'SUB', 'MOVEM', 'MULT', 'COMP', 'BC', 'STOP']
DL = ['DS', 'DC', 'EQU']
ad = ['START', 'END', 'LTORG']
reg = ['AREG', 'BREG', 'CREG', 'DREG']
sym_dict = {}

def clean_operands(x):
    result = []
    for item in x:
        parts = item.strip().split(',')
        for part in parts:
            part = part.strip().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
            if part:
                result.append(part)
    return result

file1 = open("INPUT.txt", 'r')
lines = file1.readlines()
lc = 0

for line in lines:
    x = clean_operands(line.strip().split())
    if not x: continue

    if x[0] == 'START':
        lc = int(x[1])
        continue

    if x[0] not in IS + DL + ad and x[0] not in reg:
        label = x[0]
        if 'EQU' in x:
            if x[2].isdigit():
                sym_dict[label] = int(x[2])
            elif x[2] in sym_dict:
                sym_dict[label] = sym_dict[x[2]]
        else:
            sym_dict[label] = lc
        x = x[1:]

    if x and x[0] in IS:
        lc += 1
    elif x and x[0] == 'DS':
        lc += int(x[1])
    elif x and x[0] == 'DC':
        lc += 1

file1.close()

with open('sym.text', 'w') as f1:
    f1.write("\tSymbol Table\nName\tAddress\n")
    for i in sym_dict:
        f1.write(i + "\t" + str(sym_dict[i]) + "\n")

print("✅ Symbol Table generated: sym.text\n")
print("Symbol Table:")
for k, v in sym_dict.items():
    print(f"{k}\t{v}")
