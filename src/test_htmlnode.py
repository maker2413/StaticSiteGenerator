import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Google", props={"href": "https://www.google.com", "target": "_blank"})
        expected = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_default_values(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        node1 = HTMLNode("a", "Google", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("a", "Boot.Dev", [node1], {"href": "https://www.boot.dev"})

        self.assertRaises(NotImplementedError, node2.to_html)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_empty_tag(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")

    def test_to_html_empty_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_tag_empty(self):
        node = ParentNode(
            None,
            [],
        )
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_children_empty(self):
        node = ParentNode(
            "p",
            None,
        )
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_nested_parents(self):
       node = ParentNode(
           "p",
           [
               ParentNode(
                   "p",
                   [
                       LeafNode("b", "Bold text"),
                       LeafNode(None, "Normal text"),
                       LeafNode("i", "italic text"),
                       LeafNode(None, "Normal text"),
                   ],
               ),
               LeafNode("b", "Bold text"),
               LeafNode(None, "Normal text"),
               LeafNode("i", "italic text"),
               LeafNode(None, "Normal text"),
            ],
        )

       self.assertEqual(node.to_html(), "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

if __name__ == "__main__":
    unittest.main()
