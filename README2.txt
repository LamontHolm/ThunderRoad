Game Design for a backup copy of my physical board game of  "Thunder Road Board game"


Scope:
This is a learning exercise for python programming. I have this board game and love to play it.  My vision for the 1.0 will be:
* "Hot seat" format for 2 - 4 players.
*  The game mechanic is easy and should be a good starting point to learn programming with.
* Optional "Holm" rule that I had while playing the game.  Dune Buggy got the road bonus if on the road.  Off road they got a +1
* Graphics will be simple text or limited art.  That will come later.
* Play will be local computer.  No Internet connectivity planned at this time.
  


What is "Thunder Road":
http://en.wikipedia.org/wiki/Thunder_Road_(board_game)
http://boardgamegeek.com/boardgame/804/thunder-road

Rules for board game:
http://www.hasbro.com/common/instruct/thunderroad.pdf



Notes on game Play:

* 6 Dice
	3 red dice are active players dice
* Typical Dice generator should work
	3 yellow dice are defense rolls
* Typical Dice Generator should work
	1 black "road" Bonus Dice
* Modify the dice generator to match this sequence
* 1=1
* 2=1
* 3=1
* 4=2
* 5=2
* 6=3
	Repair Rolls
	Road Bonus Rolls
	If a car is on the road for a complete turn it can add the road bonus result to the move count.  This road bonus applies to all vehicles that start the turn on road. 
2 Game Boards
	14 squares per tile.
	7 squares deep.  Rows Offset by 1/2 square
	Three rows on top are "dirt"
	Two rows in middle are "road"
	Two rows on bottom are "dirt"
	See figure 5 on page 2 in PDF
* 12 Cars
	4 players
	Car colors Green, Tan, White, Orange
	3 cars each value 6,5,4
	6 = heavy car
	5= midsize car
	4= dune buggy (+1 dirt bonus)
o 4 Choppers
	Color Green, Tan White, Orange
	Value 6 (holm rule)
	8 Wrecks
o Avoid them or ram through them	

Game Play in a nutshell:
* Random color/number method generates the starting order.
* First turn each player in turn:
o Roll and move: Roll three yellow dice. Each die shows the number of movement one of can do.
o First Turn is over.
* Start Of Second Turn:
o Roll and Move
* Never move Backwards
* Must move full roll.  Road Bonus optional but must move full bonus.  Car must be on road at start of turn.
* Never Pass Through another car
* Two cars in same square = RAM.  No more than 2 cars in same square
* Road Bonus
* Fix/Repair car
o Try to attack
* RAM algorithm
* Attack Car Value +1d6 -Def Car Value + 1d6.  whom ever is greater = winner
* Shoot algorithm 
Attack player rolls 1d6.  Attack Value Greater than def car value = kill.
* Chopper
* Move anywhere on board. Attack using same formula as shooting. Chopper. If chopper leave back board to the front board the machine cannot move back.
o Dumping opponents and Winning the game.
* Killed cars are replaced left on the board where they died.  They act as a "wrecked car" for RAMS.
* The players still in action will attempt drive down the road.  Once the active cars cross the board the rear board is brought to the front and the cars on the board are dumped. This includes active and destroyed cars. A player has 3 cars.  It is possible to "dump" one of his slower cars if he chooses. Dumped cars are out of the game. 
* Winning the game.  When one player has "dumped" all other cars






