code="""
,[>>>+<<<-]
>>>[<+<<+>>>-]<<
,[>>>+<<<-]
>>>[<+<<+>>>-]<
[<->-]<
>+<
[
    >-<[-]
    <<.>>
    ++++++++[>++++<-]>+.[-]<
    ++++++++[>++++++++<-]>---.[-]<<.
    >[-]
]
>[<+>-]<
[
    [-]
    <<.>>
    ++++++++[>++++++++<-]>---..[-]<
    <.>
]
"""
def info():
    print(f"\n\n{pointer = }")
    print("mem:")
    for x in range(0,len(mem)//10):
        stroke = ""
        for y in range(0,len(mem)%11):
            stroke += str(mem[x*10+y]) + " "
        print(stroke)
        
asc_t=[chr(x) for x in range(0,128)]
def asc(s):
    for i in range(0,len(asc_t)):
        if asc_t[i]==s:
            return i
mem = [x*0 for x in range(0,10)]
pointer = 0
loop = [x*0 for x in range(0,5)]
iter = 0
cmd = 0
while cmd < len(code):
    match code[cmd]:
        case ">":
            pointer += 1
        case "<":
            pointer -= 1
        case "+":
            mem[pointer] += 1
            if mem[pointer] > 255:
                mem[pointer] -= 255
        case "-":
            mem[pointer] -= 1
            if mem[pointer] < 0:
                mem[pointer] += 255
        case ".":
            print(chr(mem[pointer]),end="")
        case ":":
            print(mem[pointer],end="")
        case ",":
            mem[pointer] = asc(input("input:"))
        case ";":
            mem[pointer] = int(input("input:"))
        case "[":
            if mem[pointer] != 0:
                loop[iter] = cmd
                iter += 1
            else:
                op=1
                while op>0:
                    cmd += 1
                    if code[cmd]=="[":
                        op+=1
                    if code[cmd]=="]":
                        op-=1
        case "]":
            if mem[pointer] != 0:
                cmd = loop[iter-1]
            else:
                loop[iter-1] = 0
                iter -= 1
    cmd+=1
info()
