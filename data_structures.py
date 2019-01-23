"""
How does a stack work?
It adds Item at the top so the first element
in is the last element out
Uses the principle LIFO(Last in first out)

Stacks can be implemented using lists in Python.
When you add elements to a stack, it is known as a push operation,
whereas when you remove or delete an element it is called a pop operation.
"""


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


"""
How does a queue work?
It works just like the normal queues, the first element in is the
first element out
Uses the principle FIFO(First in first out)
"""


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


"""
Lists: stores heterogenous data. They are mutable.
  - append : adds item by default to the end of the list.
  - insert : adds item in the position specified
  - remove : removes the first occurrence of the item
  - pop : removes item in a given index

"""

"""
Arrays : stores homogenous data
    -Thus, arrays can be very useful when dealing with a large
    collection of homogeneous data types.
    Numpy arrays: multidimensional arrays.
"""

"""
Tuples :
Tuples are another standard sequence data type.
The difference between tuples and list is that tuples are immutable,
which means once defined you cannot delete, add or edit any values inside it
"""
"""
Dictionaries :
Dictionaries are exactly what you need if you want to implement something
similar to a telephone book. None of the data structures that you have seen
before are suitable for a telephone book.
"""
"""
Sets :
Sets are a collection of distinct (unique) objects. These are useful to create
lists that only hold unique values in the dataset. It is an unordered collection
but a mutable one, this is very helpful when going through a huge dataset.
"""

"""
Graphs:
A graph in mathematics and computer science are networks consisting of nodes,
also called vertices which may or may not be connected to each other.
The lines or the path that connects two nodes is called an edge.
If the edge has a particular direction of flow, then it is a directed graph,
with the direction edge being called an arc. Else if no directions are specified,
the graph is called an undirected graph.
"""

graph = {
    "a": ["c", "d"],
    "b": ["d", "e"],
    "c": ["a", "e"],
    "d": ["a", "b"],
    "e": ["b", "c"],
}


def define_edges(graph):
    edges = []
    for vertices in graph:
        for neighbour in graph[vertices]:
            edges.append((vertices, neighbour))
    return edges


print(define_edges(graph))


"""
Trees : The root is always at the top of the tree.
The root is often called the parent and the nodes that
it refers to below it called its children.
The nodes with the same parent are called siblings.
"""


class Tree(object):
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return (
            str(self.info)
            + ", Left child: "
            + str(self.left)
            + ", Right child: "
            + str(self.right)
        )


tree = Tree(1, Tree(2, 2.1, 2.2), Tree(3, 3.1))
print(tree)
