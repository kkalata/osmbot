class Element:
    def __init__(self, tags):
        self.tags = tags


class Node(Element):
    def __init__(self, coords, tags):
        super().__init__(tags)
        self.coords = coords


class Way(Element):
    def __init__(self, tags, nodes):
        super().__init__(tags)
        self.nodes = nodes


class Relation(Element):
    def __init__(self, tags, members):
        super().__init__(tags)
        self.members = members
