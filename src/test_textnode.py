import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_text(self):
        node = TextNode("This is not the text you are looking for", TextType.BOLD)
        node2 = TextNode("This is not the text you are looking for", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_type(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https//www.cooldogs.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "https//www.cooldogs.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()