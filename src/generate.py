from extract import extract_title

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
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    text_to_children,
    block_to_html_node,
    handle_quote,
    handle_unordered_list,
    handle_ordered_list,
    handle_code_block,
    handle_headings,
    handle_paragraph_block
)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    contents = from_file.read()
    
    template_file = open(template_path, "r")
    template = template_file.read()
    
    html = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)
    new_html = template.replace("{{ Content }}", html).replace("{{ Title }}", title)

    new_file = open(dest_path, "w")
    new_file.write(new_html)

    from_file.close()
    template_file.close()
    new_file.close()
