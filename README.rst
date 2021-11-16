Tower of Rapunzel
=================

Install
-------

Create a Python virtual environment (version 3.7 or above)::

    python3 -m venv torvenv

Install the game (the version number may differ)::

    torvenv/bin/pip install tower_of_rapunzel-0.9.0.tar.gz

Play
----

Launch the server::

    torvenv/bin/torgame

You should see this message::

    ======== Running on http://127.0.0.1:8080 ========
    (Press CTRL+C to quit)


Point your browser to that address::

    firefox http://127.0.0.1:8080

When you get to Rapunzel's chamber for the first time, you may need to *enable audio* in your browser tab
if there is no sound to be heard.

Poster
======

Tower of Rapunzel is Free software. It is a web-native single-puzzle text adventure, built entirely of:

    * Python 3.7+
    * HTML5
    * CSS3

It's a piece of work to demonstrate the use of the `Turberfield dialogue`_ library, and to show how that
can be integrated into an asynchronous web framework.

Tower of Rapunzel's core logic is written in Python. The dialogue library provides a neat format to define and
schedule the speech of the non-player characters.

Other architectures are possible. Authors less focused on coding may prefer to implement game logic within
the dialogue itself. This too is supported by the `Turberfield dialogue`_ library.

I'm looking for feedback on the game and its underlying technology. Do please:

    * Leave a comment_ on the Itch.io game page
    * Flag a technical issue_ at the Github repository

.. _Turberfield dialogue: https://turberfield-dialogue.readthedocs.io/en/latest/
.. _comment: https://tundish.itch.io/tower-of-rapunzel
.. _issue: https://github.com/tundish/tower_of_rapunzel/issues
