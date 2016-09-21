A = raw_input()
B = raw_input()
C = raw_input()
dic = {"a": A, "b": B, "c": C}
turn = "a"
while True:
    try:
        nx = dic[turn][0]
    except:
        print turn.upper()
        exit()
    dic[turn] = dic[turn][1:]
    turn = nx
