from htmlnode import HTMLNode
from textnode import *

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    html_node = HTMLNode("a", "Google", props={"href": "https://www.google.com", "target": "_blank"})
    print(text_node)
    print(html_node)

    print(html_node.props)
    print(html_node.props_to_html())

main()
