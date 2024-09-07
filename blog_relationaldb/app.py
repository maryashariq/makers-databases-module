from lib.database_connection import DatabaseConnection
from lib.comments_repository import CommentsRepository
from lib.posts_repository import PostsRepository

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        # self._connection.seed('blog_seeds.sql')
    
    def run(self):
        posts_repo = PostsRepository(self._connection)
        posts = posts_repo.all()

        for post in posts:
            print(f'{post.id}: {post.title}, {post.content}')
    
    def run2(self, choice):
        posts_repo = PostsRepository(self._connection)
        post = posts_repo.find(choice)
        print(f'{post.id}: {post.title}, {post.content}')
    
    def run3(self):
        posts_repo = PostsRepository(self._connection)
        post = posts_repo.find_with_comments(1)


if __name__ == '__main__':
    app = Application()
    app.run3()