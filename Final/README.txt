SI507 Winter2020 Final
Stephen Hayden
schayden@umich.edu

This project fulfills the final requirement for SI507 W2020 at the University of Michigan

Required packages:

requests
bs4 -> Beautiful Soup
flask -> Flask, render_template, request
sqlite3



[1] Gathering Data Set

Begin with "scrape_pokemon_list.py," running will take ~2 hours wherein serebii.net
will be scraped to return a list, cached into "pokemon_list.csv," of each pokemon, its types,
and its stats.

[1.1]
Next, run "get_list_of_moves.py," which scrapes through bulbapedia.com to return a list of
each attack and its stats, cached into "moves.csv"



[2] Creating database

Begin with "create_type_table.py," which reads through "pokemon_list.csv" to return each type,
paired with a number, which serves as that type's ID. "id" is the PRIMARY KEY of this database
where the next two tables will refer to it for their type.

__DATA MASSAGING POINT__

This file requires a few manipulations within dbbrowser. For an undetermined reason, the unique
identifying aspect of the creation code does not perfectly differentiate between types, such 
that a number are duplicated, and a number are over-written. To fix this, within dbBrowser, it
is possible to manually replace the three duplicated values with those that were overwritten,
such that the types tied to "15," "18," and "19" are rewritten to "Flying," "Steel," and "Ice,"
respectively. 


[2.1]
Next, "create_pokemon_table.py" is run to create a table containing each pokemon and its data.
This information is also read from "pokemon_list," though in lieu of the first type being
written automatically, it is written with the associated id from the types table, such that
later it may be used in a join statement.

[2.2]
Finally, "create_moves_table.py" is run to create a table "moves" within the "pokemon.sqlite"
database alongside the other two tables. This table reads "moves.csv" for its data, though 
also using the id numbers out of "types_table.id" for its type, where a foreign key is written.


__DATA MASSAGING POINT__

This table must be additionally massaged in dbBrowser to fix an encoding error within the
"Power" column. The "-"'s which were scraped out serebii.net are translated as "â€”" into
sqlite. It was possible to fix this within the code, as the "PP" and "Accuracy" columns also
faced this condition, though for an undetermined reason the same fix which replaced those hyphens
did replace a number of those within the Power column, such that 

"UPDATE moves
SET
	Power = REPLACE(Power, "â€”", "0")"
had to be run within dbBrowser.



[3] Running the Flask app
To run the app, run "507_final.py," which launches at "http://127.0.0.1:5000/"
This app uses two templates, one "index.html," for the front page, and "results.html"
for the results page after completing the query.
