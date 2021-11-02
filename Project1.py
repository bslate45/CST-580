class Node():

    def __init__(self,
                 last = None,
                 pos = None,
                 F = 0,
                 G = 0,
                 H = 0):
        self.last = last
        self.pos = pos
        self.F = F
        self.G = G
        self.H = H

    def __eq__(self, other):
        return self.pos == other.pos


def AStarPathing(grid, start, end):

    start_node = Node(None, start)
    end_node = Node(None, end)

    open_set = [start_node]
    closed_set = []

    while len(open_set) > 0:

        current_node = open_set[0]
        lowest_index = 0
        
        for index, item in enumerate(open_set):
            if item.F < current_node.F:
                current_node = item
                lowest_index = index

        open_set.pop(lowest_index)
        closed_set.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.pos)
                current = current.last
            return path[::-1]

        neighbors = []
        
        for pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_pos = (current_node.pos[0] + pos[0], current_node.pos[1] + pos[1])

            if node_pos[0] > (len(grid) - 1) or node_pos[0] < 0 or node_pos[1] > (len(grid[len(grid)-1]) -1) or node_pos[1] < 0:
                continue

            if grid[node_pos[0]][node_pos[1]] != 0:
                continue

            node = Node(current_node, node_pos)
            neighbors.append(node)

        for neighbor in neighbors:

            for node in closed_set:
                if neighbor == node:
                    continue

            neighbor.G = current_node.G + 1
            neighbor.H = ((neighbor.pos[0] - end_node.pos[0]) ** 2) + ((neighbor.pos[1] - end_node.pos[1]) ** 2)
            neighbor.F = neighbor.G + neighbor.H

            for node in open_set:
                if neighbor == node and neighbor.G > node.G:
                    continue

            open_set.append(neighbor)


def main():

    grid = [[0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (0, 4)

    path = AStarPathing(grid, start, end)
    print(path)


if __name__ == '__main__':
    main()