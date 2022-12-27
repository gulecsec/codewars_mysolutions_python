class Sleigh(object):
    def authenticate(self, name, password):
        return (name, password) == ('Santa Claus',"Ho Ho Ho!")
