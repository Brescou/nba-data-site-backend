from flask_script import Manager, Command
from app.main import app

manager = Manager(app)


class RunServer(Command):
    def run(self):
        app.run()


class Hello(Command):
    def run(self):
        print('hello')


class Routes(Command):
    def run(self):
        print(app.url_map)


manager.add_command('runserver', RunServer())
manager.add_command('hello', Hello())
manager.add_command('routes', Routes())

if __name__ == "__main__":
    manager.run()
