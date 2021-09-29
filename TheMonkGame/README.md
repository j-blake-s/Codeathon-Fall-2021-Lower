# __The Monk Game__


## <b>Situation</b>

"The Monk Game" is a boardgame similar to Tic-Tac-Toe common among the monks of a particular monastery. Each player takes turns setting down tiles onto an <b>M</b> x <b>N</b> board with the goal to connect <b>K</b> tiles in a row. In order to keep the game interesting, the monks change the size of the board and the number of tiles every time they play. 

Two monks from the monastery, Tozan and Seppo, are long-time rivals who play "The Monk Game" to test each others wit and strategy. In their most recent game, they attempted to prove their enlightenment and detachment by intentionally not winning. This resulted in the longest game they have ever played, eventually using up all the tiles in the entire monastery. With no more tiles and neither monk having won, they were about to be forced to call it a draw when a third monk approached them. He suggested that whoever had given their opponent more opportunities to win was the more generous/detached monk. Tozan and Seppo agreed with his reasoning and asked if he would count all the tiles on the board to figure out who had been given more opportunities to win.

## <b>Objective</b>

You will take the place of the third monk to determine the winner of Tozan and Seppo's bet. For each monk, you will count the number of spots where their tile being placed would result in their victory. The monk with the most number of spots loses the bet. To make it easier, the monks have asked that you specifically report how many more spots Tozan has over Seppo. If Tozan had 5 spots to win and Seppo had 3, you would report back 2. If the numbers were reversed you would report back -2.

## <b>Input</b>

The first line contains the numbers <b>M N K</b> where:
-   M is the number of rows on the board.
-   N is the number of columns on the board.
-   K is the number of tiles in a row needed to win.

Following the first line will be <b>M</b> lines with <b>N</b> characters.  

Each line corresponds to a row on the board and every character corresponds to a spot in that row.  

Empty tiles are marked with "~" while Tozan and Seppo's tiles are marked with "T" and "S" respectively.

## __Sample Input__

    3 3 3
    S T ~
    T ~ T
    S ~ S

## __Sample Output__
    -1

## Explanation


## __Sample Input__

    4 4 3
    S ~ S ~
    ~ T S T
    S ~ ~ ~ 
    ~ T ~ T

## __Sample Output__

    1

## Explanation
    
