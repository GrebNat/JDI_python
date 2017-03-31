
def constant(f):
    def set(self, value):
        raise TypeError
    def get(self):
        return f(self)
    return property(get, set)