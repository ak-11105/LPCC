lit_dict = {}
lc = 0
ad = ['START', 'END', 'LTORG']

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

for line in lines:
    x = clean_operands(line.strip().split())
    if not x: continue

    if x[0] == 'START':
        lc = int(x[1])
        continue

    for token in x:
        if token.startswith("='") or token.startswith('="'):
            if token not in lit_dict:
                lit_dict[token] = -1

    if x[0] in ['LTORG', 'END']:
        for i in lit_dict:
            if lit_dict[i] == -1:
                lit_dict[i] = lc
                lc += 1

file1.close()

with open('lit.text', 'w') as f2:
    f2.write("\tLiteral Table\nName\tAddress\n")
    for i in lit_dict:
        f2.write(i + "\t" + str(lit_dict[i]) + "\n")

print("✅ Literal Table generated: lit.text\n")
print("Literal Table:")
for k, v in lit_dict.items():
    print(f"{k}\t{v}")
