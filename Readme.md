


# Python Challenge

Create a simple command-line REST client called `restful.py` able to `GET` and `POST` from [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

## Requirements

1. Written in Python 3 using `requests` library (no framework).
2. Should include `requirements.txt` file for `pip3 install -r requirements.txt` into a `venv` virtual environment.
3. `restful.py` should be an executable Linux script. Usage should be `./restful.py` not `python3 restful.py`.
4. Script should use `argparse` library to process the command-line arguments and options.
5. Error-handling: script should always display the response's HTTP status code. If the response code is not `2XX`, the script should exit with an error message and non-zero exit code, and not perform any additional action.
6. Object-oriented: all functionality after argument parsing should be performed by class methods, rather than in procedural-style functions.
#### Make sure you have the requests library installed (pip install requests). 
   You can then run the script from the command line and use the following commands:

- To get all posts: python restful.py get_posts
- To get a specific post by ID: python restful.py get_post --post_id <post_id>
- To create a new post: python restful.py create_post --title <title> --body <body> --user_id <user_id>
- Replace <post_id>, <title>, <body>, and <user_id> with the appropriate values.



