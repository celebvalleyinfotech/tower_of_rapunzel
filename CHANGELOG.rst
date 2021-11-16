Change Log
::::::::::

Versions
========

0.10.0
-----

* Fix packaging issues.

0.9.0
-----

* Refactor to use Balladeer as much as possible.

0.8.0
-----

* Add textures from https://www.transparenttextures.com/
* Fixed checks at win condition
* Restyled throughout
* First test release on Itch.io for Narrascope

0.7.0
-----

* Moved away from one special class for each character.
  Now using Occupation states to select entities.
* Narrator now the main object for holding game state.
* Fixed a bug where you could continually revisit the stylist.
* Swapped out the Presenter for one based on BlueMonday78 0.8.0
* Swapped out the render functions for ones based on BlueMonday78 0.8.0
* Added a tower image based on https://images.unsplash.com/photo-1576237013484-7ce69c40b10a
* Added a street image based on https://images.unsplash.com/photo-1517606261660-fd72f84596b3
* Added a win condition
* Recorded audio for the status and win pages
* Adopted styles and font from BlueMonday78 0.8.0

0.6.0
-----

As submitted to PyWeek 28.

Diary
=====

2019-09-23
----------

About three hours in. The basic idea came quickly, and
then my brain immediately complicated it with all sorts of
pointless embellishments.

I tried to draw it out on paper. Decided on a world with
8 separate locations, and then soon realised you'd have
to jump back and forth between them pretty quickly.

I need to be sure that the game is viable from the outset.
There'll be no time to build it and fix it later. All my
code so far is an attempt to simulate the thing to see if
a satisfying end state can be reached in a reasonable
amount of time.

After tweaking some rules it seems there should be a final
Gold/Silver/Bronze outcome. And you'll have to take a risk
to get the top prize.

Next steps are:

    * build out the game rules from my simulation
    * put in the framework for web interaction

2019-09-24
----------

This evening I took the game rule simulation and rewrote it so
it can be operated from within the app. Also put in the web
framework.

Everything is very much more solid now. But I can't say I feel
like I've made enough progress yet.

I need to allow two clear days to create music and content. Not
sure I'm going to get that at this rate.

2019-09-25
----------

Good news and bad news.

Firstly, styling. I always knew I wouldn't have time for much.
Luckily, my minimal styling looks OK.

Now the bad news. I took too long to achieve even that. I have to move
away from the technical stuff. If the game's going to be worth the play,
I need to engage my creative side. I need to inject a sense of fun.

I know I can do that, but I need to put myself in a different space.
Away from the code. Into the story. Fantasy time.

I should be going to bed in an hour. I've got to go to work in the morning.
Instead I need to conjure up enough playful energy to knock out 1200
words of interesting dialogue.

Wish me luck!

2019-09-27
----------

Well, the last 32 hours have been nuts.

After writing the preceding diary entry, I decided I'd take the next day
off work, or I'd never make it in time.

I went in to a cafe early and kept topping up on coffee while getting down
literally all the dialogue for the game on paper. It took about two hours.
I was blocked to begin with on Rapunzel's rhymes but by the end the words
seemed to arrive quite easily.

But I had made some false assumptions about how to organise the dialogue.
I had the speech separated out into themes. I thought I would change the
context at different points in the game, and all the characters would
switch in the same way to their appropriate phrases. But that was way too
complicated and required a lot greater wordage than I had time to make.

So when I got back I rejigged all that. There were also some bugs to fix,
in code I thought I could trust. So my perception of progress was never
reliable enough for me to feel confident.

The good news was that having all the words on paper made creating script
files a low-risk process. And in the background I started setting my
drum machine going, to find some beats I could use as a backing track.

By bedtime nearly all the script files were done. Sadly, I never hit on
any sounds that I felt would fit as a backing track. So it looks like
the game will have no music, which is a shame.

Still, it plays better than some of my other efforts. I've just fixed
the death screen. Python packaging is in place. A bit more dialogue
required here and there.

2019-09-28
----------

Grabbed an hour this morning (Saturday) to tweak some dialogue.

I took a screenshot which does a good job of showing the tone of the piece.

Although it would be nice to get some music in there, I'm starting to feel
some fatigue. I don't want to spoil this one with any hasty last minute
changes.

So I think I might leave it at that. This will be version `0.6.0`.
That's likely to be the version I submit for judging, unless I spot any
glaring issues.

I think in terms of effort the thinking, writing, coding, packaging and
testing took about 24 hours in total.

2020-05-28
----------

Decided to join the NarraScope Jam.
Objectives:

    * Fold in fixes and practices from Blue Monday 78
    * Rework the rendering and styling
    * Add audio FX

.. _not well received: https://pyweek.org/e/prorogue/ratings/
