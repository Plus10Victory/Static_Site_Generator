import unittest

from block_markdown import markdown_to_blocks, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    def test_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
            ],
            markdown_to_blocks(markdown)
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )


    def test_block_type_heading(self):
        block = "## This is a heading"
        self.assertEqual(
            "heading",
            block_to_block_type(block)
        )

    def test_block_type_code(self):
        block = "``` this is code ```"
        self.assertEqual(
            "code",
            block_to_block_type(block)
        )

    def test_block_type_quote(self):
        block = "> start of quote\n> second line\n> final line"
        self.assertEqual(
            "quote",
            block_to_block_type(block)
        )

    def test_block_type_ul(self):
        block = "* line 1\n* line 2\n* line 3"
        self.assertEqual(
            "unordered_list",
            block_to_block_type(block)
        )

    def test_block_type_ol(self):
        block = "1. first\n2. second\n3. third"
        self.assertEqual(
            "ordered_list",
            block_to_block_type(block)
        )

if __name__ == "__main__":
    unittest.main()