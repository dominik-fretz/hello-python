class Book:
    def __init__(self, title, revision, authors):
        self.title = title
        self.revision = revision
        self.authors = authors

    def lend(self, userName):
        print("Book {} lent by {}".format(self.title, userName))