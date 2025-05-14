lit_dict = {}
pool_table = [0]
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
        pool_table.append(len(lit_dict))

file1.close()

with open('pool_table.txt', 'w') as f4:
    f4.write("\tPool Table\nPool #\tIndex\n")
    for i in range(len(pool_table)):
        f4.write(str(i + 1) + "\t" + str(pool_table[i] + 1) + "\n")

print("✅ Pool Table generated: pool_table.txt\n")
print("Pool Table:")
for i in range(len(pool_table)):
    print(f"#{i+1} → {pool_table[i]+1}")
