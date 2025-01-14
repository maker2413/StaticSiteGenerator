from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        node_sections = old_node.text.split(delimiter)
        if len(node_sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(node_sections)):
            if node_sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(node_sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(node_sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes
