import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text</h2>"
        )



if __name__ == "__main__":
    unittest.main()