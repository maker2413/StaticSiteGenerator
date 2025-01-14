import unittest

from htmlnode import HTMLNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text = TextNode("value", TextType.TEXT)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "value")

    def test_bold(self):
        text = TextNode("value", TextType.BOLD)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "value")

    def test_italic(self):
        text = TextNode("value", TextType.ITALIC)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "value")

    def test_code(self):
        text = TextNode("value", TextType.CODE)
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "value")

    def test_link(self):
        text = TextNode("value", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "value")
        self.assertEqual(html_node.props, {"href": "www.google.com"})

    def test_image(self):
        text = TextNode("value", TextType.IMAGE, "me.png")
        html_node = text_node_to_html_node(text)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "me.png", "alt": "value"})

if __name__ == "__main__":
    unittest.main()
