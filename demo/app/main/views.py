import platform
import random
import string
import os
from flask import render_template, request, jsonify
from . import main


# Generate Random String
def get_random_string():
    # Grab the list of all ascii_letters + all digits
    letters_and_numbers = string.ascii_letters + string.digits

    # Using a random length between 5 and 15, generate a string of that length
    # The string will randomly choose from  all ascii_letters and all digits
    # Then join the string together
    random_string = ''.join(random.choice(letters_and_numbers) for _ in range(random.randint(5, 15)))

    return random_string


# Our route for displaying the bootstrap template
@main.route('/', methods=['GET', 'POST'])
def index():
    # Check if get got a POST request meaning someone click on a button
    if request.method == "POST":
        # Check if the button that was pressed was the "random-button"
        if request.form.get("random-button"):
            # Grab the name text string and then render the index.html page
            return render_template("index.html", random_text=get_random_string(), arch=str(platform.machine())), 200

    # If the request was a not a POST request then render the template with the default message
    return render_template("index.html", random_text="This text will change.... hit the button!",
                           arch=str(platform.machine())), 200


# Our route for display build info
@main.route('/build', methods=['GET'])
def build():
    # JSON blob
    build_object = {
        "VERSION": os.getenv('VERSION'),
        "CIRCLE_BUILD_URL": os.getenv('CIRCLE_BUILD_URL'),
        "CIRCLE_SHA1": os.getenv('CIRCLE_SHA1'),
        "CIRCLE_USERNAME": os.getenv('CIRCLE_USERNAME'),
        "CIRCLE_BUILD_NUM": os.getenv('CIRCLE_BUILD_NUM'),
        "ARCH": str(platform.machine())
    }

    # Return and render JSON object
    return jsonify(build_object)
