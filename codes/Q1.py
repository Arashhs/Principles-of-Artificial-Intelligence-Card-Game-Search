import data_structure as ds
import copy

nodes_generated_num = 0
nodes_expanded_num = 0


def bfs(init_node):
    frontier = []
    explored = []
    global nodes_generated_num
    global nodes_expanded_num

    if ds.goal_test(init_node.state):
        return ds.get_solution(init_node)
    frontier.append(init_node)
    
    while True:
        if frontier == []:
            return 'failure'
        node = frontier.pop(0)
        nodes_expanded_num += 1
        explored.append(node.state)
        actions = ds.get_all_actions(node)
        for act in actions:
            child = ds.Node(node.state, node, None, act, node.cost+1)
            if child.state not in explored and child.state not in [n.state for n in frontier]:
                nodes_generated_num += 1
                if ds.goal_test(child.state):
                    return ds.get_solution(child)
                frontier.append(child)


def beauty_print(solution):
    solution_depth = solution[-1].cost
    print("Solution Depth (N): {}, Nodes Generated: {}, Nodes Expanded: {}\n".format(solution_depth, nodes_generated_num, nodes_expanded_num))
    for node in solution:
        print("Depth: {}, Action: {}".format(node.cost, node.action))
        print(node.state, "\n")



def main():
    initial_state = ds.init_game("test3.txt")
    initial_node = ds.Node(initial_state, None, None, None, 0)
    solution = bfs(initial_node)
    beauty_print(solution)
    

    


if __name__ == '__main__':
    main()