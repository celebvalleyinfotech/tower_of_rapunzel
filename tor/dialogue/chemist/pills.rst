
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.story.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types:  tor.story.Narrator

.. entity:: CHEMIST
   :types:  tor.story.Character
   :states: tor.story.Occupation.chemist

Pills
~~~~~

Chat 0
------

.. condition:: CHEMIST.state 0

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Take one now, with a little water.

    Whatever you do, don't breathe on any children or pets.

Chat 1
------

.. condition:: CHEMIST.state 1

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Frankly, I'd recommend emergency surgery.

Chat 2
------

.. condition:: CHEMIST.state 2

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Homeopathy. It's not what it used to be.

Chat 3
------

.. condition:: CHEMIST.state 3

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Always read the label.

Chat 4
------

.. condition:: CHEMIST.state 4

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Would you like to apply for our online loyalty card?

Chat 5
------

.. condition:: CHEMIST.state 5

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Can you please stand on the plastic.

Chat 6
------

.. condition:: CHEMIST.state 6

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    Repeat prescriptions. The healing never stops.

Chat 7
------

.. condition:: CHEMIST.state 7

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    I can arrange for an ambulance.

Chat 8
------

.. condition:: CHEMIST.state 8

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    I'm afraid my defibrilator training was some time ago.

Chat 9
------

.. condition:: CHEMIST.state 9

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 20000

[CHEMIST]_

    The suppositories are behind you.
