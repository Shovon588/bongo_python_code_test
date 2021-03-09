"""
Generating the tree from the question assuming the parent
of the root node as -1. Putting the node value and its parent
in a dictionary as a key value pair as per node stucture defined
in the question. We can also generate the tree by using
generate_tree function.
"""

tree = {1:-1, 2:1, 3:1, 4:2, 5:2, 6:3, 7:3, 8:4, 9:4}


def generate_tree():
    global tree
    tree = {}
    nodes = int(input("Number of nodes: "))
    print("Set the parent of the root node as -1")
    for node in range(nodes):
        value, parent = map(int,input("Enter the value and corresponding parent: ").split())
        tree[value] = parent


def first_node_ancestors(node):
    """
    Takes in a node, finds the ancestors of it and returns them as a dictionary
    """

    if node not in tree:
        raise KeyError("Node is not present in the tree")
    
    ancestors = {node: True}
    while tree[node]!=-1:
        parent = tree[node]
        if (parent in tree) and (parent not in ancestors):
            ancestors[parent] = True
            node = parent
        else:
            raise KeyError("The parent of the root node should be -1")

    return ancestors
        

def find_lca(node1,node2):
    """
    Takes in two nodes, finds the least common ancestor of them and returns it.
    """
    
    if node1 not in tree or node2 not in tree:
        raise ValueError("Node is not present in the tree")
    
    first_ancestors = first_node_ancestors(node1)

    while True:
        if node2 in first_ancestors:
            print(node2)
            return node2
        node2 = tree[node2]



"""
Time Complexity: O(h) where h is the height/depth of the tree.
We are traversing the tree as bottom up fashion, which will take
no more than h iterations to reach the root.
The number of nodes is two, so it will take O(2*h) -> O(h) time.
Also we need to look up the dictionary but it's complexity is O(1)
so it doesn't count. The complexity remains O(1)


Memory Complexity: O(n) where n is the number of nodes in the tree.
We are storing all the nodes of the tree  as a key, value pair in a dictionary.
So O(n) memory required.


Auxiliary Space: O(h) where h is the height/depth of the tree.
We need to store the ancestor list of the first node. We have h such
node, so the complexity will O(h)
"""







