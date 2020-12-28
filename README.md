# Principles-of-Artificial-Intelligence-First-Project
The codes for the first project of my Principles of AI course that I have written in Python, in which I solve a card game using BFS, IDS, and A* search strategies. Input is given (as a text file) to the program, which contains a number of cards from different colors in different rows, each holding a value between 1 and n (configurable). The goal of this game is to do a series of actions that will lead us to a state in which every card is placed in a row containing all of the cards with the same color, and the cards' values are sorted in descending order. The only action we can do is to move the final card of a row to the end of another row.

Sample Input:
```
5 3 5	-- (number of rows, number of colors, number of cards of each color)
2g
5g 4g 3g 1g
5y 4y 3y 2y 1y
2r
5r 4r 3r 1r
```

Output: 
```
Solution Depth (N): 6, Nodes Generated: 211, Nodes Expanded: 64
'#' means empty row

Depth: 0, Heuristic: 2, F: 2, Action: 2 to 4
1:  2g 
2:  5g 4g 3g 1g 
3:  5y 4y 3y 2y 1y 
4:  2r 
5:  5r 4r 3r 1r  

Depth: 1, Heuristic: 3, F: 4, Action: 1 to 2
1:  2g
2:  5g 4g 3g
3:  5y 4y 3y 2y 1y
4:  2r 1g
5:  5r 4r 3r 1r

Depth: 2, Heuristic: 2, F: 4, Action: 4 to 2
1:  #
2:  5g 4g 3g 2g
3:  5y 4y 3y 2y 1y
4:  2r 1g
5:  5r 4r 3r 1r  

Depth: 3, Heuristic: 1, F: 4, Action: 5 to 1
1:  #
2:  5g 4g 3g 2g 1g
3:  5y 4y 3y 2y 1y
4:  2r
5:  5r 4r 3r 1r

Depth: 4, Heuristic: 2, F: 6, Action: 4 to 5
1:  1r
2:  5g 4g 3g 2g 1g
3:  5y 4y 3y 2y 1y
4:  2r
5:  5r 4r 3r

Depth: 5, Heuristic: 1, F: 6, Action: 1 to 5
1:  1r
2:  5g 4g 3g 2g 1g
3:  5y 4y 3y 2y 1y
4:  #
5:  5r 4r 3r 2r

Depth: 6, Heuristic: 0, F: 6, Action: None
1:  #
2:  5g 4g 3g 2g 1g
3:  5y 4y 3y 2y 1y
4:  #
5:  5r 4r 3r 2r 1r
```
