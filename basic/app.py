from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask words."""

    prompts = story.prompts

    return render_template("questions.html", prompts=prompts)
    # Similar to explanation below, we need to tell the html file what prompts is so it knows what to do. Prompts is a list, we need to loop through it, so we pass it through to the html so that can happen


@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)
    # text=text is included because 'text' is a keyword included in the html file and we need to pass data to the html file to tell it what 'text' is. In this situation it's often given the same name (so same thing on both sides of the =) to keep things simple.
