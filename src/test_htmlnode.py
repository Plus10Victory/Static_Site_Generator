import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_tag(self):
        node = HTMLNode(tag="p")
        self.assertEqual(node.tag, "p")

    def test_repr(self):
        node = HTMLNode(
            "p",
            "I love coffee",
            None,
            {"coffee": "espresso tonic"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, I love coffee, children: None, {'coffee': 'espresso tonic'})"
        )

    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "click this",
            None,
            {"href": "https://www.coffee.com"}
        )
        self.assertEqual(
            node.props_to_html(),
            ' href="https://www.coffee.com"'
        )

    def test_leaf_to_html(self):
        node = LeafNode(
            "a",
            "Click for ☕",
            props={"href": "https://www.coffee.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.coffee.com">Click for ☕</a>'
        )




if __name__ == "__main__":
    unittest.main()