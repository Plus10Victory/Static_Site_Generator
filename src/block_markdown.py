import re
from textnode import (
    TextType,
    TextNode,
    text_node_to_html_node
)
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
)
from htmlnode import (
    HTMLNode,
    LeafNode,
    ParentNode
)

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


# take full markdown document
# beakdown into blocks
# block content -> TextNodes
# TextNodes -> HTMLNodes
# HTMLNodes -> children of <div> HTMLNode

def markdown_to_html_node(markdown):
    #split markdown into blocks
    blocks = markdown_to_blocks(markdown)
    nodes = []
    #loop over each block
    for block in blocks:
        # create new HTMLNode with the proper data
        # assign the proper child HTMLNode (text_to_children)
        html_block_node = block_to_html_node(block)
        nodes.append(html_block_node)
    # make all block nodes children of <div> HTMLNode
    return ParentNode("div", nodes)



def text_to_children(text):
    # works for all block types
    # take string of text
    # use previously created functions
    text_nodes = text_to_textnodes(text)
    # TextNode -> HTMLNode
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children


# create functions block -> HTMLNode for each type
def block_to_html_node(block):
    # determins block type
    block_type = block_to_block_type(block)
    # strip the type and convert text to children
    match block_type: 
        case "quote":
            return handle_quote(block)
        case "unordered_list":
            return handle_unordered_list(block)
        case "ordered_list":
            return handle_ordered_list(block)
        case "code":
            return handle_code_block(block)
        case "heading":
            return handle_headings(block)
        case "paragraph":
            return handle_paragraph_block(block)
        case _:
            raise ValueError("Invalid block type")


# Quote <blockquote></blockquote>
def handle_quote(block):
    lines = block.splitlines()
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_line = line[2:]
        new_lines.append(new_line)
    content = " ".join(new_lines)
    children = text_to_children(content)        
    return ParentNode("blockquote", children)


# unordered_list <ul><li></li></ul>
def handle_unordered_list(block):
    html_items = []
    lines = block.splitlines()
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

# ordered_list <ol><li></li></ol>
def handle_ordered_list(block):
    html_items = []
    lines = block.splitlines()
    for line in lines:
        text = line[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

# code <pre><code></code></pre>
def handle_code_block(block):
    if not block.startswith("```") or not block.endwith("```"):
        raise ValueError("Invalid code block")    
    text = block[4:-3]
    children = text_to_children(text)
    code_node = ParentNode("code", children)
    return ParentNode("pre", [code])

# headings <h{i}></h{i}> i = len(string(#))
def handle_headings(block):
    heading_size = len(block.split()[0])
    text = block[heading_size+1:]
    children = text_to_children(text)
    return ParentNode(f"h{heading_size}", children)


# paragraph <p></p>
def handle_paragraph_block(block):
    lines = block.splitlines()
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)