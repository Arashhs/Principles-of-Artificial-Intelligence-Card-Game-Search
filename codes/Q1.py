import data_structure as ds
import copy

frontier = []
explored = []

def bfs(init_node):
    actions = ds.get_all_actions(init_node)
    print(actions)
    return actions



def main():
    initial_state = ds.init_game("test.txt")
    initial_node = ds.Node(initial_state, None, None, None, 0)
    solution = bfs(initial_node)
    

    


if __name__ == '__main__':
    main()