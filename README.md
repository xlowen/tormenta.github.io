# Torment Grimoire
## Video Demo: https://youtu.be/vGrOSLiWodM

#### Description:

A spell database for tormenta20, a brazillian pen and paper role playing game that can be found on this link: https://tormentarpg.com.br/

My idea was to create an easy to use and access database for spells contained in the game, since it uses either an ebook or a physical book, and it was a great opportunity to dable into databases using sqlite3, as taught during the course, templating using Jinja, python for the backend, css and bootstrap 5 for the appearance and overall design of the webpage.

I Created a landing page, index.html which uses bootstrap's navbar, so that I could add links and also use it as a layout, by doing this and using jinja I have created all other .html files.

Inside of the project folder there is a static folder, containing styles.css file with all of the custom looks of the website and images I have used.

As far as css goes, I tried to make the most out of using classes, avoiding inline styles, as I was also using bootstrap 5 as a framework, sometimes it has to be overwritten given some design choices, which I tried to play with, such as transitions, though my final goal was to make the website as clean as possible for the user to be used only as a quick reference, be it mid playthrough using a smartphone or while on a desktop when creating a new character and making it easier to copy and paste spell descriptions directly into a character sheet.

As far as design went, some parts were challenging, such as making the website responsive, hiding column elements from my tables (which are actually collapsible divs, borrowing bootstraps accordion classes), and figuring out flexbox/grid positioning. This was actually a pretty nice learning experience since I had to go through bootstrap's documentation, which led me to figure out a lot of its functionality.

I used sqlite3, to manage the storage of all spells, as per spells.db, divided into 4 tables, 2 for arcane spells, 2 for divine spells. These tables contain the short description of spells (Name, circle, execution, range, area, duration and short description) aswell as a full description, in a separate table. All spells are accessed and dynamically printed into the .html files through jinja loops, iterating for each row in a given table, as seen on arcana.html and divina.html.

I wanted to create a "zebra" style collapsible table, and had to go through jinja's documentation in order to be able to make the correct correlation between the row that shortly describes a spell and its elements through jinja and the spell's full description. For that, the arcane table inside of spells.db correlates to the adesc table, through primary and foreign id keys.

In order to make the collapsible element show the correct spell description, we have to reference that spell's full description id, for example - 'row1 -> spell 1 short description clickable collapsible when clicked should display a textbox containing spell 1 full description' for that we make row1 target another html element that will have spell 1 full description.

I achieved that through the usage of jinja's built in counter for each iteration. so 'row1 spell n short description' targets #spell n, where n is the id of a given spell. Spell 1 short relates to Spell 1 full, the integer being the matching id.

So Spellshort n targets Spellfull n, as seen on "data-bs-target="#spell{{ loop.index }}" where loop.index is the current iteration, starting at 1, and it targets an id (as the # indicates), in order for it to match the correct full description of the current #spell I used "span class="collapse" id="spell{{ loop.index0 + 1 }}" since loop.index0 starts counting from 0, the + 1 had to be added.

Notice that loop.index and loop.index0 are 2 separate counters, had I used loop.index inside the same for loop I would end up mismatching as spell since each iteration would result in a +1 count for each, hence why both loop.index and loop.index0 are used.

The purpose of this project was to provide the player base with an alternative, other than the actual book, to filter spells and find them faster, improving gameplay experience, speeding up the access to the information, since through sqlite3 queries we can filter for any words contained in the database and presenting the results to the user in an easy way.

Copyright could be an issue so only content that falls under an open game license was used, and there is a link to said license terms and conditions available in the homepage.

Since this is an academic project. there is also a link in layout.html that shows in every page with a link to my personal github and to cs50.html which shows that this webapp was built as the final project for cs50.