"""
Jack Pearkes' personal website, designed for simple maintenance
and content addition. See github.com/pearkes/jack.ly for more.
"""
import os
import glob
import markdown2
from flask import Flask, render_template, abort

# Main app
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def check_index():
    "Checks to make sure the index file exists."
    if not os.path.isfile('sections/index.md'):
        raise Exception('You must have an index file in sections.')


def list_sections():
    "Returns a list of sections from the filesystem."
    listed_sections = os.listdir('sections/')
    sections = [s for s in listed_sections if not '.' in s]
    sections.sort()
    return sections


def list_items(section):
    "Returns a list of items from the filesystem."
    listed_items = glob.glob('sections/%s/*.md' % section)
    listed_items.sort()
    return listed_items


def human_name(filename, title=True):
    "Makes a filename human readable and returns it as a string."
    name = filename.replace('-', ' ')
    name = name.split('.')[0]
    if '_' in name:
        name = name.split('_')[-1]
    if title:
        name = name.title()
    return name


def build_path(slug, section=None):
    "Makes a path relative and returns it as a string."
    if section:
        path = "/%s/%s" % (section, slug)
    else:
        path = "/%s" % (slug)
    return path


def generate_cache():
    "Generates the cache of the sections and their entries."
    print "Generating cache..."
    # The cache we are building.
    cache = {}
    sections = list_sections()

    # Add the index to the cache.
    check_index()
    cache['index'] = {'html': markdown2.markdown_path('sections/index.md')}

    for section in sections:
        cache[section] = {'name': human_name(section),
                          'filename': section,
                          'path': build_path(section),
                          'items': []}

        # Get all the items for each section.
        items = list_items(section)

        # Generate HTML from markdown files.
        for item in items:
            filename = item.split('/')[-1].split('.')[0]
            slug = filename.split("_")[-1].lower()
            item_cache = {'name': human_name(filename, title=False),
                          'filename': filename,
                          'slug': slug,
                          'path': build_path(slug, section),
                          'html': markdown2.markdown_path(item)}

            cache[section]['items'].append(item_cache)

    print "Cache succesfully generated with %s sections." % len(sections)
    return cache

cache = generate_cache()  # Kicking it new school


def retrieve_sections():
    "Returns an array of all sections and their dicts."
    sections = cache.values()
    sections.sort()
    return sections


def retrieve_section(id):
    "Returns a section we grabbed from the cache."
    return cache.get(id)


def retrieve_item(section, id):
    "Returns an item we grabbed from the cache."
    s = retrieve_section(section)
    if not s:
        return
    # Performance concerns with large lists.
    for item in s['items']:
        if item['slug'] == id:
            return item, s
    return None, None


@app.route('/')
def index():
    "The homepage. Renders a default section."
    section = retrieve_section('index')
    return render_template('index.html', sections=retrieve_sections(),
                           section=section)


@app.route('/<section>')
def section(section):
    "Looks up a section based on it's name and renders it."
    section = retrieve_section(section)
    if not section:
        abort(404)
    return render_template('section.html', sections=retrieve_sections(),
                           section=section)


@app.route('/<section>/<item>')
def item(section, item):
    "Looks up an item based on it's name and section and renders it."
    item, section = retrieve_item(section, item)
    if not item:
        abort(404)
    return render_template('item.html', sections=retrieve_sections(),
                           section=section, item=item)


if __name__ == '__main__':
    # Bind to PORT if defined in the environment, otherwise default to 5000.
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port, debug=True)
