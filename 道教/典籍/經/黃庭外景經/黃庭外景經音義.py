path = "典籍/經/黃庭外景經/黃庭外景經音義.txt"
# line1, line2, line3 = "", "", ""
# print("line 2 is \""+line2+"\". ")
lines = []
content = ""; i=1

with open(path, 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        # print('\n---\''+line+'\'---')
        if not line:
            break
        if line[0] == "#" or line[0] == "!" or line == '---\n': # title?
            content = content + line + '\n'
        else:
            if len(lines) == 3:
                content = content + str(i).zfill(3) + ". <ruby>\n\t\t " + \
                    lines[0] + "\t\t <rt>\n\t\t\t " + \
                        lines[1] + "\t\t\t <br>\n\t\t\t <big><big><big>" + \
                            lines[2] + "\t\t </big></big></big></rt>\n\t </ruby><br><br>\n\n"
                lines = []; i += 1
            else:
                if line != '\n':
                    lines.append(line)
                # print(line, '\n---\n')
        # print(lines)
with open('典籍/經/黃庭外景經音義.md', 'w', encoding='utf-8') as f:
    f.write(content)