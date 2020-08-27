from flask_frozen import Freezer
from app import app

app.config['FREEZER_DESTINATION'] = "../dist"
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False

freezer = Freezer(app)

if __name__ == '__main__':

    @freezer.register_generator
    def templates():
        yield {"template": "/home.html"}

    @freezer.register_generator
    def static_file():
        yield {"path": "/index.css"}

    freezer.freeze()