import data_structure as ds
import copy

nodes_generated_num = 0
nodes_expanded_num = 0


def a_star(init_node):
    frontier = []
    explored = []
    global nodes_generated_num
    global nodes_expanded_num

    if ds.goal_test(init_node.state):
        return ds.get_solution(init_node)
    frontier.append(init_node)
    
    while True:
        frontier.sort(key=lambda x: x.f)
        if frontier == []:
            return 'failure'
        node = frontier.pop(0)
        nodes_expanded_num += 1
        if ds.goal_test(node.state):
                    return ds.get_solution(node)
        explored.append(node.state)
        actions = ds.get_all_actions(node)
        for act in actions:
            child = ds.Node_H(node.state, node, None, act, node.cost+1)
            if child.state not in explored and child.state not in [n.state for n in frontier]:
                frontier.append(child)
                nodes_generated_num += 1


def beauty_print(solution):
    solution_depth = solution[-1].cost
    print("Solution Depth (N): {}, Nodes Generated: {}, Nodes Expanded: {}\n".format(solution_depth, nodes_generated_num, nodes_expanded_num))
    for node in solution:
        print("Depth: {}, Heuristic: {}, F: {}, Action: {}".format(node.cost, node.heuristic, node.f, node.action))
        print(node.state, "\n")



def main():
    initial_state = ds.init_game("test3.txt")
    initial_node = ds.Node_H(initial_state, None, None, None, 0)
    solution = a_star(initial_node)
    beauty_print(solution)
    

    


if __name__ == '__main__':
    main()