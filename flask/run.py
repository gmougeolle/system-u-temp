from livereload import Server
from app import app

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('../temp/index.css')
    server.watch('templates/**/*.html')
    server.serve()