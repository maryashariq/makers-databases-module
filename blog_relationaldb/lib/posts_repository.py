from lib.posts import Post
from lib.comments import Comment

class PostsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []

        for row in rows:
            item = Post(row["id"], row["title"], row["post_content"])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * FROM posts WHERE id = %s', [post_id]
        )
        row = rows[0]
        return Post(row["id"], row["title"], row["post_content"])
    
    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            "SELECT posts.id, posts.title, posts.post_content, comments.id, comments.username, comments.comment_content " \
            "FROM posts JOIN comments ON posts.id = comments.post_id " \
            "WHERE posts.id = %s", [post_id])
        
        comments = []
        for row in rows:
            comment = Comment(row["id"], row["username"], row["comment_content"], row["post_id"])
            comments.append(comment)

        return Post(rows[0]["post_id"], rows[0]["title"], rows[0]["post_content"], comments)
    