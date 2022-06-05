words = []
f = open("inter_codes.txt", 'r')
outf = open("Pass2output.txt", 'a')
symbol = open("symtab.txt", 'r')
literal = open("littab.txt", 'r')
outf.truncate(0)

symbols = []
literals = []
for line in symbol:
    symbols.append(line.split())
for line in literal:
    literals.append(line.split())

print("\n********** Symbol Table **********\n")
print(symbols)
print("\n********** Literal Table **********\n")
print(literals)

print("\n********** Intermediate Code **********\n")
for line in f:

    line = line.replace('(', "")
    line = line.replace(')', "")
    words = line.split()
    print(words)

    # if end statement
    if 'AD,02' in words[1]:
        outf.write(f"{words[0]} 00 0 {words[2][2:]}")
        outf.write("\n")
    elif "AD" in words[0]:
        outf.write(" ----\n")

    else:
        if words[0].isnumeric():
            outf.write(words[0])

        MachineCode = words[1].split(',')
        outf.write(f" {MachineCode[1]}")

        if len(words) == 4:
            if words[2] == '1' or words[2] == '2' or words[2] == '3' or words[2] == '4':
                outf.write(f" {words[2]} ")
            else:
                outf.write(f" 0 ")

            symbolLiteral = words[3].split(",")
            if symbolLiteral[0] == 'S':
                outf.write(symbols[int(symbolLiteral[1])][2])
                outf.write("\n")
            elif symbolLiteral[0] == 'L':
                outf.write(literals[int(symbolLiteral[1]) - 1][2])
                outf.write("\n")
            else:
                outf.write(symbolLiteral[1])
                outf.write("\n")

        else:
            outf.write(f" 0 ")
            symbolLiteral = words[2].split(",")
            if symbolLiteral[0] == 'S':
                outf.write(symbols[int(symbolLiteral[1])][2])
                outf.write("\n")
            elif symbolLiteral[0] == 'L':
                outf.write(literals[int(symbolLiteral[1]) - 1][2])
                outf.write("\n")
            else:
                outf.write(symbolLiteral[1])
                outf.write("\n")

f.close()
outf.close()
symbol.close()