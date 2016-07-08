do = "WBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBWWBWBWWBWBWBW"
zu = ["Do", "Do", "Re", "Re", "Mi", "Fa", "Fa", "So", "So", "La", "La", "Si"]
S = raw_input()
for i in range(12):
    if do[i:].startswith(S):
        print zu[i]
