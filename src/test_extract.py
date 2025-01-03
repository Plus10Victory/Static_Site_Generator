import unittest

from extract import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_hello(self):
        markdown = "# Hello world"
        self.assertEqual(
            "Hello world",
            extract_title(markdown)
        )


    def test_whitespace(self):
        markdown = "#   There should be no white space   "
        self.assertEqual(
            "There should be no white space",
            extract_title(markdown)
        )


    def test_large_header(self):
        markdown = "### this header is too large"
        self.assertRaises(
            ValueError,
            extract_title, markdown
        )


    def test_no_header(self):
        markdown = "missing head tag"
        self.assertRaises(
            ValueError,
            extract_title, markdown
        )


    def test_large_doc(self):
        markdown = "# header\nnot a header\nmore not header"
        self.assertEqual(
            "header",
            extract_title(markdown)
        )

if __name__ == "__main__":
    unittest.main()