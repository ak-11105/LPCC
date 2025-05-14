# mnt_generator.py
def generate_mnt():
    with open("input.txt", "r") as code:
        lines = code.readlines()

    mntable = []
    mntp = 0
    mdtp = 0
    flag = False

    with open("mnt.txt", "w") as mnt:
        mnt.write("Macro_Name\tStart-End\n")
        
        for line in lines:
            tokens = line.strip().split()
            if not tokens:
                continue

            if tokens[0] == "MACRO":
                flag = True
                mntp += 1
                macro_name = tokens[1]
                start = mdtp
                mntable.append((macro_name, start))
            
            elif tokens[0] == "MEND":
                flag = False
                mntable[-1] = (mntable[-1][0], mntable[-1][1], mdtp - 1)
            
            elif flag:
                mdtp += 1

        for macro in mntable:
            mnt.write(f"{macro[0]}\t{macro[1]}-{macro[2]}\n")

generate_mnt()
