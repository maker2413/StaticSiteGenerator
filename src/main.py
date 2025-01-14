from htmlnode import HTMLNode
from textnode import *

def main():
    text_node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    html_node = HTMLNode("href", "https://www.google.com")
    print(text_node)
    print(html_node)

main()
