# Diss-GwentBalancer

Masters dissertation - plays and balances Gwent classic.

### Game Structure

Best of three rounds. Highest score in a round wins, a matching score in a final round leads to a draw.


TO DO
* Think about how to present each card's information (faction, ability, row) and how to use each ability.
* Encode all card information in a csv that can be read into memory as individual card objects.
* Have a preset deck for each class in a csv.
* Think about the flow, logic, and events in each game and how to encode these.
* Think about how to present options for search.
* Think about how to create a basic CLI.

Card Ranges
* Close combat
* Ranged
* Siege
* Agile

Card Abilities
* Spy - played to the opponents side of the board and contributes to their score. The person who played the spy draws two additional cards from their deck.
* Commander's horn - Doubles strength of all other unit cards in the row (limited to once per row, check if a horn unit can be stacked with the horn card).
* Decoy - Swap with a card on the battlefield which is returned to your hand.
* Hero - immune to special effects and abilities (check if this includes decoy).
* Medic - after being played, choose one card from your discard pile to be played instantly (no heroes or special cards).
* Morale boost - all other cards in the row get +1
* Muster - find any cards in the deck with the same name and play them instantly.
* Scorch - destroy enemy’s strongest unit in a specific row, if the combined strength of all his or her units is 10 or more. (Hero cards not affected)
* Tight bond - placing this unit next to a card with the same name will double the strength of both cards.

Weather conditions
* Frost - strength of both players close combat cards set to one.
* Fog - strength of both players ranged cards set to one.
* Rain - strength of both players siege cards set to one.
* Clear weather - clears any weather effects on board.