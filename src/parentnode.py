from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children nodes")
        parent_plus_child_html = f"<{self.tag}>"
        for child in self.children:
            parent_plus_child_html += child.to_html()
        parent_plus_child_html += f"</{self.tag}>"
        return parent_plus_child_html

