# __The Monk Game__


## <b>Situation</b>

Two Zen monks, Tozan and Seppo, sit down to play a game of Tic-Tac-Toe.

They begin to place their tiles and quickly approach a draw, so Tozan remarks that "It is earthly chains which keep us from enlightenment, the path of the Buddha knows no bounds" to which Seppo agrees and makes the board larger. 

They keep playing on this larger board but keep that they must line up 3 tiles in a row in order to win. As Tozan nears a victory, Seppo exclaims that "True enlightenment is seeking to push beyond oneself and find new heights. It is the sign of a weak man who takes pride in complacency". Tozan understands and proposes they increase the number of tiles in a row needed to win. 

And so the game continues on as the board grows larger and the number of tiles increases. Soon they find themselves completely out of tiles and no one else in the monastery have anymore. 

At a lost for what to do, a monk comes up to them and states that "Our virtue is marked by what we are able to give to the world, not what we are able to take". Upon hearing this, Tozan and Seppo agree that the winner of the game should be determined by who allowed the other more chances to win. 

They ask the third monk if he would count how many more opportunities to win Tozan has than Seppo.  If Tozan has more, than Seppo is more generous and thus he wins the game. If Tozan has less, than he is more generous and thus he wins the game.

## <b>Objective</b>

You are acting as the monk who has to count all of the tiles for Tozan and Seppo. More specifically, you are counting the number of <b>"Winning Spots"</b> that  each player has. A <b>"Winning Spot"</b> is anywhere a player can put a tile and immediately win. If both monks can place a tile in the same spot and win, then the <b>"Winning Spot"</b> is counted for both of them. The monks do not care about the total number of spots but rather how many more spots <u>__Tozan__</u> has over <u>__Seppo__</u>.


## <b>Input</b>

Every game the monks play they choose a different sized board and a different amount of tiles that need to be lined up in order to win. Addtionally, the monks sometimes use boards that arent perfect squares to play on to test their skills.

## __Sample Input 1__

    3 3 3
    S T ~
    T ~ T
    S ~ S

## __Sample Output 1__
    -1

## __Sample Input 2__

    4 4 3
    S ~ S ~
    ~ T S T
    S ~ ~ ~ 
    ~ T ~ T

## __Sample Output 2__

    1
    
