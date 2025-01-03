


def extract_title(markdown):
    head_line = markdown.splitlines()[0]
    head_level = 0
    for char in head_line:
        if char == "#":
            head_level += 1
        else:
            break
    if head_level != 1:
        raise ValueError(f"Header level is off by {head_level - 1}")
    return head_line.replace("# ","",1).strip()