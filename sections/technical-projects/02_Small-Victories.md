Small Victories is a simple way to host a website using Dropbox
as a CMS (Content Management System).

The Small Victories backend works by polling Dropbox checking for changes
to a folder created by the application. If changes exists, files are
downloaded and parsed according to their type – photos are injected
as `<img>` tags, Markdown is rendered and injected as HTML, etc.

This allows you to manage a website with a simple, familiar interface.
It doesn't require you to create an account past logging in with Dropbox –
or even provide your name or email address.

Small Victories was initially dreamed up by [Jacob Heftmann](http://www.jacobheftmann.com),
and he did the design while I created the backend. We both collaborated on the
product experience.

- The Small Victories [homepage](https://smallvictori.es)
- An [example](http://demo.smallvictori.es) of a Small Victory
- Jacob's [blog post](http://notes.jacobheftmann.com/all/07-24-small-victories/) about the product

