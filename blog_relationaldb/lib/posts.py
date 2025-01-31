from lib.comments import Comment

class Post:
    def __init__(self, id, title, content, comments = []):
        self.id = id
        self.title = title
        self.content = content
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Post({self.id}, {self.title}, {self.content})'
        