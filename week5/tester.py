class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.ref_counter = 0

    def __str__(self):
        cur, s = self, str(self.value)
        while cur.next != None:
            s += ' -> ' + str(cur.next.value)
            cur = cur.next
        return s

def create_node(input_list):
    nodes = {}
    for inp in input_list:
        n1, n2 = inp.split('>')
        if n1 not in nodes:
            nodes[n1] = Node(n1)
        if n2 not in nodes:
            nodes[n2] = Node(n2)
        nodes[n1].next = nodes[n2]
        nodes[n2].ref_counter += 1
    return list(nodes.values())

def node_size(node):
    visited = []
    counter = 0
    while node != None:
        visited.append(node)
        node = node.next
        counter += 1
        if node in visited:
            return counter
    return counter

inp = input('Enter edges: ').split(',')
all_nodes = create_node(inp)

intersect_nodes = sorted([node for node in all_nodes if node.ref_counter > 1], key= lambda x: int(x.value))
if not intersect_nodes:
    print('No intersection')
    exit()
else:
    for intersect in intersect_nodes:
        print(f'Node({intersect.value}, size={node_size(intersect)})')

print('Delete intersection ', end='')
for node in intersect_nodes:
    if node.next != None:
        node.next.ref_counter -= 1
        node.next = None
pre_intersect = [node for node in all_nodes if node.next in intersect_nodes]
for node in pre_intersect:
    node.next = None

print('then swap merge:')
head_nodes = sorted([node for node in all_nodes if node.ref_counter == 0], key= lambda x: int(x.value))
new_merge = head_nodes[0]
cur = None
while len(head_nodes) > 1:
    cur = head_nodes[0]
    if cur.next != None:
        head_nodes.append(cur.next)
    head_nodes.pop(0)
    cur.next = head_nodes[0]

print(str(new_merge))