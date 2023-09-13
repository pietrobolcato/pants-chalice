"""Main file launchable from pants"""

from lambda_app.helloworld.chalicelib.mylib import say_hello_world

if __name__ == "__main__":
    print(say_hello_world())