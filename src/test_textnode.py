import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false_text(self):
        node = TextNode("This is the text", TextType.BOLD)
        node2 = TextNode("This is not the text you are looking for", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false_type(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.cooldogs.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.cooldogs.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.coffee.com")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.coffee.com)", repr(node)
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_link(self):
        text_node = TextNode(
            "click here", 
            TextType.LINK, 
            url="https://www.links.com"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://www.links.com">click here</a>'
        )


if __name__ == "__main__":
    unittest.main()