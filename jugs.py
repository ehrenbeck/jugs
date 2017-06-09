#Blake Ehrenbeck
#9 April 2017

from enum import Enum
from queue import Queue
import copy
import sys

vertices = {}
jugs = []

class Color(Enum):
    WHITE = 1
    BLACK = 3

class Jug():
    def __init__(self, capacity, state):
        self.capacity = capacity
        self.state = state

class Vertex():
    def __init__(self, jugs):
        self.color = Color.WHITE
        self.pi = None
        self.jugs = jugs

numberOfJugs = input("Enter the number of jugs: ")
for i in range(0,int(numberOfJugs)):
    capacity = input("Enter the capacity for jug "+str(i)+": ")
    state = input("Enter the amount of water in jug "+str(i)+": ")
    jugs.append(Jug(int(capacity), int(state)))
targetCapacity = int(input("Enter a target capacity: "))



s = Vertex(jugs)


q = Queue()
q.put(s)
s.pi = None
while not q.empty():
    v = q.get()

    for j in v.jugs:
        if j.state == targetCapacity:
            print(tuple(jug.state for jug in v.jugs), end=' <- ')
            while(v.pi):
                print(tuple(jug.state for jug in v.pi.jugs), end=' <- ')
                v.pi = v.pi.pi
            sys.exit()

    v.color = Color.BLACK
    for jug in range(len(v.jugs)):
        for otherjug in range(len(v.jugs)):
            if jug != otherjug:
                originalJugState = v.jugs[jug].state
                originalOtherJugstate = v.jugs[otherjug].state
                if v.jugs[jug].state + v.jugs[otherjug].state <= v.jugs[otherjug].capacity:
                    v.jugs[otherjug].state += v.jugs[jug].state
                    v.jugs[jug].state = 0
                else:
                    v.jugs[jug].state = v.jugs[jug].state - (v.jugs[otherjug].capacity - v.jugs[otherjug].state)
                    v.jugs[otherjug].state = v.jugs[otherjug].capacity

                v1 = Vertex(copy.deepcopy(v.jugs))
                v.jugs[jug].state = originalJugState
                v.jugs[otherjug].state = originalOtherJugstate
                v1.pi = v

                if tuple(i.state for i in v1.jugs) not in vertices:
                    v1.color = Color.WHITE
                    vertices[tuple(i.state for i in v1.jugs)] = 1
                else:
                    v1.color = Color.BLACK

                if v1.color == Color.WHITE:

                    q.put(v1)
print("not possible")
