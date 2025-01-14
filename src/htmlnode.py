class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag =tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_string = ""
        if isinstance(self.props, dict):
            p_string = ""
            for ele in self.props:
                p_string += f"{ele}=\"{self.props[ele]}\" "

            props_string = p_string[:-1]

        return props_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value can not be None")

        if self.tag == None:
            return self.value

        if self.props == None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag can not be None")

        if self.children == None:
            raise ValueError("children can not be None")

        string = f"<{self.tag}>"
        for leaf in self.children:
            string += leaf.to_html()

        string += f"</{self.tag}>"
        return string
