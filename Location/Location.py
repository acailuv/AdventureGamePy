class Location:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
    
    def enter(self, target):
        target.location = self

    def leave(self, target):
        target.location = None
