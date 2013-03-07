## jack.ly

This is the repository for [jack.ly](http://jack.ly), my personal website.

It is a simple flask application that uses filesystem storage and
markdown to maintain content. Upon startup, it renders all of the
files into html and places them in a dictionary based cache.

This causes slow startup times and higher than normal memory requirements,
but for simple websites it works great and gives a nice performance bump
under load.

The backend is designed to be flexible, and uses patterns that may be
useful to others, but there is also domain specific logic intertwined.

## Sections

Most websites have different sections. In this case, a section
is both a directory and a route.

You can create as many sections as you want. All sections are stored
in a dictionary with all of the items for each section. Because of this,
it's easy to retrieve both a list of sections and the items for that
section.

To create a section, simply place a directory in the `sections` directory,
using the name of the section as the name of the directory.

*Note: Directories with dashes will automatically be replaced with spaces
as the section name.*

    name: A human readable name of the section.
    filename: The filename of the section directory.
    items: A list of items associated with the section.
    path: The relative path to access the section through the web server.


## Item

Sections are flexible, and simply have something called an "item".

Items for a section can be created by placing a markdown file in the
section it belongs to. Each item should be named according to it's title.

*Note: Item files with dashes will automatically be replaced with spaces
as the item name.*

By default, all items will be rendered in alphabetical order.

Attributes:

    name: A human readable name of the item.
    filename: The filename of the item file.
    path: The relative path to access the item through the web server.

## Retrieving and Displaying

Sections are rendered when accessed as a path. For example, if you had
a section named `blog`, you could access it on the path `/blog`.

That route would then render the associated section dict named `section`.

In templates, you can access it like this:

    <h1>{{ section.name }}</h2
    <ul>
    {% for item in section.items %}
        <li><a href="{{ item.path }}">{{ item.name }}</a></li>
    {% endfor%}
    </ul>

## Custom Location Data

People may or may not be interested in where I last was on my computer
and how long ago that was. In scenarios requiring a fast response, it
may be useful to the sender of an email to determine the likelihood I
will have access.

It also serves to keep the site "alive" and provide an element of
action in an otherwise archival creature.

This is done by using Apple's FindMyiPhone API's and the [findi](https://github.com/pearkes/findi) python
library that I maintain. The device that it looks for is my computer.

