from flask_script import Manager

from spacelaunches import create_app


app = create_app('development')
manager = Manager(app)

@manager.command
def test():
    print('This is a Test! :D')

@manager.command
def run():
    app.run('0.0.0.0', 5001)

if __name__ == '__main__':
    manager.run()
