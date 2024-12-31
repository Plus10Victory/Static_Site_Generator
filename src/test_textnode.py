import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()