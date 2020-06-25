# This was my solution submitted and passed all the test cases
'''
Author: Ashutosh Srivastava
Python3 solution
You can also use the A* algorithm with little modification to solve the problem.
'''

from collections import deque
def solution(maze):
    h= len(maze)
    w= len(maze[0])
    q = deque([(0, 0, 1, True)])
    maze[0][0] = -1
    while (True):
        x, y, step, wall = q.popleft()
        if (x == h-1 and y == w-2 or x == h-2 and y == w-1): 
            return step+1
        for a, b in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if (not (0 <=a < h and 0 <=b < w) or maze[a][b] == -1 or maze[a][b] == -2 and not wall or maze[a][b] == 1 and not wall): 
              continue
            elif (maze[a][b] in [0, -2]):
              q.append((a, b, step+1, wall))
            elif (maze[a][b] == 1):
              q.append((a, b, step+1, False))
            maze[a][b] = -1 if wall else -2
    return maze[a][b]
