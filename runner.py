#! /usr/local/env python
from flask.ext.script import Manager, Server

# Create and configure our Flask application

from app import app
manager = Manager(app)

manager.add_command("runserver_public", Server(
    use_reloader=True,
    use_debugger=True,
    host='0.0.0.0')
)

if __name__ == '__main__':
    manager.run()
