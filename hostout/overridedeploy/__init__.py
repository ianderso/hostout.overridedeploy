class Recipe:
    """"""

    def __init__(self, buildout, name, options):
        self.name, self.options, self.buildout = name, options, buildout

    def install(self):
        return []

    def update(self):
        return []

    def writeVersions(self):
        pass
