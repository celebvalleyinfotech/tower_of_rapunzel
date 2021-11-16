
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.types.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types:  tor.types.Narrator

.. entity:: STYLIST
   :types:  tor.types.Character
   :states: tor.types.Occupation.stylist

Wigs
~~~~

Chat 0
------

.. condition:: STYLIST.state 0

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Ah, lovely to see you again.

Chat 1
------

.. condition:: STYLIST.state 1

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    I've had some wonderful feedback from one of our most valuable customers.

Chat 2
------

.. condition:: STYLIST.state 2

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Come on, you can tell me; what are you feeding her?

Chat 3
------

.. condition:: STYLIST.state 3

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    My only concern is the fragility of the supply chain.

    I'm trying to grow this business you know.

Chat 4
------

.. condition:: STYLIST.state 4

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Rapunzel's hair is quite the finest I've seen.

Chat 5
------

.. condition:: STYLIST.state 5

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Rapunzel's hair is quite the finest I know of.

    It's a very lustrous colour. It'll carry any dye, and yet it has
    a beautiful sheen all its own.

Chat 6
------

.. condition:: STYLIST.state 6

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    I had that Elton John in last week.

    I don't think you quite understand what's at stake right now. 

Chat 7
------

.. condition:: STYLIST.state 7

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    You know I'll always pay top prices.

    The demand for blonde is intense.

Chat 8
------

.. condition:: STYLIST.state 8

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Oh, this will be lovely to work with. You know, I never need
    my hand lotion when I've been handling the best Rapunzel.

Chat 9
------

.. condition:: STYLIST.state 9

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[STYLIST]_

    Am I glad to see you! What have you got for me?

Status
------

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    You have |COINS_N| coins.

.. |COINS_N| property:: NARRATOR.coins_n
