from util import Stack


def earliest_ancestor(ancestors, starting_node):
    ancestors_graph = create_graph(ancestors)
    stack = Stack()
    stack.push([starting_node])

    visited = set()
    earliest_ancestor_path = [starting_node]

    while stack.size() > 0:
        current_path = stack.pop()
        current_node = current_path[-1]
        if current_node not in visited:
            if len(current_path) > len(earliest_ancestor_path):
                earliest_ancestor_path = current_path
            elif len(current_path) == len(earliest_ancestor_path) and current_node < earliest_ancestor_path[-1]:
                earliest_ancestor_path = current_path

            visited.add(current_node)
            if current_node in ancestors_graph:
                for parent in ancestors_graph[current_node]:
                    new_path = list(current_path)
                    new_path.append(parent)
                    stack.push(new_path)

    ancestor = earliest_ancestor_path[-1]
    if ancestor == starting_node:
        return -1
    else:
        return ancestor


def create_graph(ancestors):
    ancestors_dict = {}
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if child in ancestors_dict:
            ancestors_dict[child].add(parent)
        else:
            ancestors_dict[child] = set()
            ancestors_dict[child].add(parent)
    return ancestors_dict
