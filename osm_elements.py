class Element:
    def __init__(self, tags):
        for key, value in tags.items():
            if type(key) is not str or type(value) is not str:
                raise TypeError("All keys and values must be str")
        self.tags = tags


class Node(Element):
    def __init__(self, coords, tags={}):
        super().__init__(tags)
        if coords["lat"] < -90 or coords["lat"] > 90:
            raise ValueError("Latitude is not in range [-90, 90]")
        elif coords["lon"] < -180 or coords["lon"] > 180:
            raise ValueError("Longitude is not in range [-180, 180]")
        self.coords = coords
        
    def __repr__(self):
        return f"Node()"


class Way(Element):
    def __init__(self, nodes, tags={}):
        super().__init__(tags)
        if len(nodes) < 2:
            raise ValueError("Way must contain at least 2 nodes")
        else:
            for node in nodes:
                if type(node) is not Node:
                    raise TypeError("A node must be Node object")
        self.nodes = nodes

    def __repr__(self):
        return f"Way()"


class Relation(Element):
    def __init__(self, members, tags={}):
        super().__init__(tags)
        if len(members) < 1:
            raise ValueError("Relation must contain at least 1 member")
        else:
            for member in members:
                if type(member["element"]) not in (Node, Way, Relation):
                    raise ValueError("A member element must be Node, Way or Relation object")
        self.members = members

    def __repr__(self):
        return f"Relation()"
