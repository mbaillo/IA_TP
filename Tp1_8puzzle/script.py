import importlib
import time
puzzle = importlib.import_module("8puzzle")
import  random



l = [4, 0, 2, 7, 1, 3, 8, 5, 6]
random.shuffle(l)
s = ' '.join(str(elem) for elem in l)

goal = puzzle.EightPuzzle("1 2 3 4 5 6 7 8 0")
initial = puzzle.EightPuzzle(s)
h = puzzle.EightPuzzle.manhatten_distance
h1 = puzzle.EightPuzzle.tile_switches_remaining
# EightPuzzle.tile_switches_remaining
# output = puzzle.EightPuzzle.action_sequence
output = puzzle.EightPuzzle.state_transition

print("Test de Manhattan \n")
start_time = time.time()
print (initial.a_star(goal, h, output))
temps_exec = time.time() - start_time
print("\nL'Heuristique de manhattan dure "+str(temps_exec)+" secondes")
print("\nTest de Tile switch \n")
start_time2 = time.time()
print (initial.a_star(goal, h1, output))
temps_exec2 = time.time() - start_time2
print("\nL'Heuristique de Tile switch dure "+str(temps_exec2)+" secondes")
print("\nLa différence de ces 2 heuristiques est de "+str(temps_exec2-temps_exec)+" secondes")
