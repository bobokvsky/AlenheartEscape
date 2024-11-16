import textwrap

# with open('python\\temp\\encoded_tiles.txt', 'r') as f:
#     with open('python\\code_encoded_tiles.txt', 'w') as f2:
#         f2.write("public function getChapterX_tiles() returns integer\n")
#         for line in f:
#             sublines = textwrap.wrap(line, 1020)
#             for i, subline in enumerate(sublines):
#                 f2.write("    CHAPTERX_TILE[{}] = \"{}\"\n".format(i, subline))
#         f2.write("    return")


with open('python\\temp\\encoded_tilesBLP.txt', 'r') as f:
    with open('python\\code_encoded_tilesBLP.txt', 'w') as f2:
        f2.write("public function getChapter3_tiles() returns integer\n")
        for line in f:
            sublines = textwrap.wrap(line, 1020)
            for i, subline in enumerate(sublines):
                f2.write("    CHAPTER3_TILE[{}] = \"{}\"\n".format(i, subline))
        f2.write("    return")