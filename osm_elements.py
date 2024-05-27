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
        self.nodes = nodes

    def __repr__(self):
        return f"Way()"


class Relation(Element):
    def __init__(self, members, tags={}):
        super().__init__(tags)
        self.members = members

    def __repr__(self):
        return f"Relation()"
