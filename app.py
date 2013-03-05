"""
Jack Pearkes' personal website, designed for simple maintenance
and content addition. See github.com/pearkes/jack.ly for more.
"""
import os
from flask import Flask, render_template

DEFAULT_SECTION = 'technical-projects'

# Main app and configuration
app = Flask(__name__)


def generate_cache():
    "Generates the cache of the sections and their entries."
    # Glob the section directory
    # Clean up the section names and cache them
    # Glob each section to get a list of the entries
    # Fix up the item titles and build the paths
    # Render the markdown to html for each item
    # Place the item data in the cache for it's section
    # You're done!
    pass


cache = generate_cache()  # Kicking it new school


def retrieve_section():
    "Returns a section we grabbed from the cache."
    pass


def retrieve_item():
    "Returns an item we grabbed from the cache."
    pass


@app.route('/')
def index():
    "The homepage. Renders a default section."
    section = retrieve_section(DEFAULT_SECTION)
    return render_template('section.html', section=section)


@app.route('/<section>')
def section(section):
    "Looks up a section based on it's name and renders it."
    section = retrieve_section(section)
    return render_template('section.html', section=section)


@app.route('/<section>/<item>')
def item(item):
    "Looks up an item based on it's name and section and renders it."
    item = retrieve_item(section, item)
    return render_template('item.html', section=section, item=item)


if __name__ == '__main__':
    # Bind to PORT if defined in the environment, otherwise default to 5000.
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
