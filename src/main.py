from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    sample_text = "This is a text node"
    sample_type = TextType.BOLD
    sample_url = "https://www.boot.dev"

    sample_node = TextNode(sample_text, sample_type, sample_url)
    
    print(sample_node.__repr__())

main()