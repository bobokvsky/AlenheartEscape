import textwrap

with open('python\\temp\\encoded_destructs.txt', 'r') as f:
    with open('python\\code_encoded_destructs.txt', 'w') as f2:
        f2.write("public function getChapter3_destructs() returns integer\n")
        for line in f:
            sublines = textwrap.wrap(line, 1014)
            for i, subline in enumerate(sublines):
                f2.write("    CHAPTER3_DESTRUCTS[{}] = \"{}\"\n".format(i, subline))
        f2.write("    return")