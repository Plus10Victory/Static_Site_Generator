import unittest
from htmlnode import HTMLNode

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




if __name__ == "__main__":
    unittest.main()