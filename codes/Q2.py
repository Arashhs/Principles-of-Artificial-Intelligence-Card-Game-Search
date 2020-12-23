import data_structure as ds
import copy

MAXIMUM_DEPTH = 1000000
INITIAL_DEPTH = 0

nodes_generated_num = 0
nodes_expanded_num = 0


def dls(node, limit):
    global nodes_generated_num
    global nodes_expanded_num

    nodes_expanded_num += 1
    if ds.goal_test(node.state):
        return ds.get_solution(node)
    elif limit == 0:
        return 'cutoff'
    else:
        cutoff_occurred = False
        actions = ds.get_all_actions(node)
        nodes_generated_num += len(actions)
        for act in actions:
            child = ds.Node(node.state, node, None, act, node.cost+1)
            result = dls(child, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                return result
        if cutoff_occurred:
            return 'cutoff'
        return 'failure'


def ids(node, initial_depth):
    global MAXIMUM_DEPTH
    for limit in range(initial_depth, MAXIMUM_DEPTH):
        result = dls(node, limit)
        if result != 'cutoff' and result != 'failure':
            return result
        


def beauty_print(solution):
    solution_depth = solution[-1].cost
    print("Solution Depth (N): {}, Nodes Generated: {}, Nodes Expanded: {}\n".format(solution_depth, nodes_generated_num, nodes_expanded_num))
    for node in solution:
        print("Depth: {}, Action: {}".format(node.cost, node.action))
        print(node.state, "\n")



def main():
    initial_state = ds.init_game("test3.txt")
    initial_node = ds.Node(initial_state, None, None, None, 0)
    solution = ids(initial_node, INITIAL_DEPTH)
    beauty_print(solution)
    

    


if __name__ == '__main__':
    main()