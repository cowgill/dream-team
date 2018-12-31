import os

from app import create_app

# use the exported cli value OR set to dev by default
config_name = os.getenv('FLASK_CONFIG', 'default')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()