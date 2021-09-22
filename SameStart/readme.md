Terra and Beast Boy are looking at two similar mazes. Thanks to Beast Boy, he has a bird's eye view of both mazes (the perspective shown in the input). Terra chooses the maze at the top of the view, Beast Boy chooses the maze at the bottom of the view. Beast Boy wants to find the number of starting spots they can choose from in their mazes such that the chosen spot is open (.) in both of their mazes, not a wall (#). He doesn't care if the maze is completable from that starting spot, they can worry about that later.

# Input Format

The first line contains  and , the dimensions of the board.

The next  lines are each of length  describing the first maze.

There is then a blank line, then  more lines each of length  describing the second maze.

# Constraints
1 <= x, y <= 200

The maze will only contain "." (representing open space) and "#" representing wall

# Output Format

Output the number of starting spaces that can be chosen where those coordinates are an open space in both mazes.