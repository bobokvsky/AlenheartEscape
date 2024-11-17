import re

pattern = re.compile(r"set wurst_stack\[wurst_stack_depth\] = ")

lines = []
with open("C://Users//Alexander//Dropbox//war3//AlenheartEscape//_build//compiled.j.txt", "r", encoding='utf-8') as jass:
    for line in jass:
        lines.append(line)
        found = pattern.search(line)
        if found is not None:
            new_line = "\t" * found.start()
            variable = line[found.end():-1]
            new_line += f"call DisplayTimedTextToPlayer(Player_localPlayer, 0., 0., 45., {variable})\n"

            lines.append(new_line)


with open("C://Users//Alexander//Dropbox//war3//AlenheartEscape//_build//war3map.j", "w", encoding = 'utf-8') as f:
    f.write("".join(lines))