# Clampdown - Planning

## Feature list

* 1 = Highest priority, 4 = Lowest priority, * = I don't care
* 1 means "First release must include this feature"
* 4 means "This is an idea for a future version of the product"
* Syntax: (Priority hellerbarde / hat-guy) <Feature Description>


* (1/1) Standard controls
    * (1/1) Play/Pause/Stop/Prev/Next
        * (4/4) Stop after current track
        * (2/4) Random
        * (1/3) Repeat
    * (2/2) Seeking
        * (3/2) By slider
        * (4/4) By fixed increments
    * (1/1) Show information about currently playing song
        * (1/1) Album
        * (1/1) Artist
        * (1/1) Title
        * (1/1) Length
        * (1/1) Current position
        * (2/3) Other metadata (track,name,genre,date,composer,performer,comment,disc)
    * (3/2) Volume Control
        * (1/3) Mute button
* (1/1) Queue
    * (1/1) Listing songs
    * (1/1) Moving one song within the queue
    * (1/1) Removing one song from the queue
    * (4/2) Selecting multiple songs, and moving them
    * (4/2) Selecting multiple songs, and removing them from the queue
    * (4/3) Save the queue as a playlistfile
* (1/1) Library
    * (1/1) Add songs to queue from library
    * (1/1) *Specifics of library to be determined elsewhere*
* (4/4) Upload files (and have them added to the library)
* (4/2) Enter a stream URL, and have it added to the queue
* (3/4) Sleep timer (stop playback in <x> minutes)
* (1/1) Technical Interface
    * (1/1) A "human-readable" Web interface
        * (2/2) Automatically update the changed parts of the GUI (such as currently playing song information)
        * (1/1) Usable by mouse
        * (3/3) Keyboard shortcuts
        * (3/4) Epic Logo/Favicon
    * (1/*) RESTful API (as much as needed)
* (1/1) Configuration of Clampdown
    * (1/1) Credentials for accessing MPD
        * (1/1) Set in config file
        * (3/4) Configured through the webinterface
        * (4/3) MPDrights are displayed to the user on the "human-readable" web interface

## Special considerations for Library features (WIP)

hellerbarde: Search is top of my list. I need a free form search field, ideally with some syntax stuff, maybe DDG-like "!artist  Van Canto" searches the field "artist". IDK...

Generally: 
Minimum resolution the GUI should work: Smartphone. (480px-720px)

Maximum resolution the GUI should be optimized for: Full-HD?

Banshee search specifics: http://banshee.fm/support/guide/searching/ (hellerbarde: seems very complex. Actually, on second look, it looks ok and well thought out)


# Clampdown - Glossary

For MPD, certain terms are already occupied with a specific meaning. We should be careful with certain expressions, and agree on what they mean in this section.

## Playlist
An element in MPDs library called playlist. MPD stores playlists in a special place, given by the option "playlist_directory" in the config file.

## Playlistfile
A file that ends in something like .m3u, or .pls. What is commonly referred to as a playlist. If such a file is placed in MPDs "playlist_directory" it becomes a playlist.

## Queue
The list of songs that MPD will play when "Play" is pressed. (But in mpc, the commandline client, this is called "playlist", so they don't really use their own terminology consistently. We'll call it queue)

## MPDRights
The level of permissions that MPD differentiates. Namely: read,add,control,admin.


# MPD Webfrontend that does not suck - Name

## Result

We decided on "clampdown" for the name for now. The way these things go, this will never change... But that's okay :)


## Rules

- You have to be able to tell your mother the URL with the name in it without spelling it out. (I guess provided your mother can speak and spell english fluently.. Argh, this is tricky)
- Other people should not do a double-take when they see the name
- "Normal" people should think it sounds neat.
- Nothing rude or perceived to be rude.


## Suggestions

- N2play (it sounds like "into play", as in bringing a nice web frontend into play. Finally. (like n'sync? :P))
- DullBoy ("All work and no _play_ make Jack a dull boy.")
- MusicLove (on second thought, meh...)
- MusiClove (haha. - problem: Google will give you mostly shit, when searching for this. - No kidding...)
- FlaconFM (A play on flask (backend), and the naming of most radio stations on air - and your favourite lossless audio codec. -  Actually, I picked it because of the alliteration). My next favorite would be canteenFM
- claMPDdown (hellerbarde: ooooooh, good one ^^)
- wiMPyD
- criMPeD
- stoMPeD
- lampshade
- Ampede (drop the st-)
- amp'd (doesnt really follow the rules...)
- ampersand
- Amp it up (actually, works with adding C or R)
- ampsite
- happy Amper
- Ampus
- Ampy (already used for software)
- We can just try to match up words ending in MP and starting with D: swampdrain, shrimpdish, tempdraft, thumpdonk

