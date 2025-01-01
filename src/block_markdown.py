import re

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.splitlines()

    if re.match(r"^#{1,6} ", block):
        return "heading"
    if re.match(r"^```.*```$", block):
        return "code"
    if all(map(lambda x: False if x[0] != ">" else True, lines)):
        return "quote"
    if all(map(lambda x: True if x.startswith(("* ","- ")) else False, lines)):
        return "unordered_list"
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return "paragraph"
            i += 1
        return "ordered_list"
    return "paragraph"


def markdown_to_html_node(markdown):