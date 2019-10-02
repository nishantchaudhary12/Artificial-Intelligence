import sys
import queue as que


def makeGraph(input_file):
    graph = dict()
    read = open(input_file, 'r')
    for each in read:
        if each != 'END OF INPUT':
            data = each.split(' ')
            curr_src = data[0]
            curr_dest = data[1]
            curr_dist = data[2].strip('\n')

            graph.setdefault(curr_src, {})[curr_dest] = curr_dist
            graph.setdefault(curr_dest, {})[curr_src] = curr_dist

        else:
            break

    # print(graph)
    read.close()

    return graph


def makeHeuristic(heuristic_file):
    heurDict = dict()
    read = open(heuristic_file, 'r')

    for each in read:
        if each != 'END OF INPUT':
            line = each.split(' ')
            city = line[0]
            value = int(line[1])
            heurDict[city] = value
        else:
            break

    # print(heurDict)
    read.close()
    return heurDict


def unif_uniform_cost(src, dest, graph):
    print('Uninformed')
    if src not in graph and dest not in graph:
        return 'Path not found'

    else:
        visited = set()
        queue = que.PriorityQueue()
        queue.put((0, [src]))

        generated = 0
        expanded = 0

        result = dict()
        size = 1

        while not queue.empty():
            node = queue.get()
            curr = node[1][len(node[1]) - 1]

            # print('curr', curr)
            expanded += 1

            if curr not in visited:
                visited.add(curr)
                if dest in node[1]:
                    result['path'] = node[1]
                    result['cost'] = str(node[0])
                    print('Generated:', generated)
                    print('Expanded:', expanded)
                    print('Maximum nodes:', size)
                    return result

                cost = node[0]
                for child in graph[curr]:
                    temp = node[1][:]
                    temp.append(child)
                    generated += 1
                    # if child not in visited:
                        # queue.put((cost + int(graph[curr][child]), temp))
                    queue.put((cost + int(graph[curr][child]), temp))
                    size = max(size, queue.qsize())

        print('Generated:', generated)
        print('Expanded:', expanded)
        print('Maximum nodes:', size)
        # return 'Path does not exist'


def inf_aStar(src, dest, graph, heuristic):
    print('Informed')
    visited = set()
    queue = que.PriorityQueue()
    queue.put((0, [src], 0))
    result = dict()

    generated = 0
    expanded = 0
    size = 1

    while not queue.empty():
        node = queue.get()
        curr = node[1]
        length = len(curr)
        city = curr[length - 1]

        if city not in visited:
            visited.add(city)
            expanded += 1
        if city == dest:
            curr.append(node[2])
            result['path'] = curr[:-1]
            result['cost'] = curr[-1]
            print('Generated:', generated)
            print('Expanded:', expanded)
            print('Maximum nodes:', size)
            return result

        children = graph[city]
        for child in children.keys():
            if child not in visited:
                cost = node[0] + heuristic[child]
                heur = node[2] + int(children[child])
                path = curr[:]
                path.append(child)
                queue.put((cost, path, heur))
                size = max(size, queue.qsize())
                generated += 1

    print('Generated:', generated)
    print('Expanded:', expanded)
    print('Maximum nodes:', size)





def main():
    input_file = sys.argv[1]
    graph = makeGraph(input_file)
    # print(graph)

    src = sys.argv[2]
    dest = sys.argv[3]

    if len(sys.argv) == 4:
        result = unif_uniform_cost(src, dest, graph)
        if result:
            # print(result)
            print('Distance: ', result['cost'])
            print('Path: ')
            for i in range(len(result['path']) - 1):
                print(result['path'][i] + ' to ' + result['path'][i+1] + ': ' +
                      graph[result['path'][i]][result['path'][i+1]] + ' kms')
        else:
            print('Path not found')

    elif len(sys.argv) == 5:
        heuristic_file = sys.argv[4]
        heuristic = makeHeuristic(heuristic_file)
        result = inf_aStar(src, dest, graph, heuristic)
        if result:
            # print(result)
            print('Distance: ', result['cost'])
            print('Path: ')
            for i in range(len(result['path']) - 1):
                print(result['path'][i] + ' to ' + result['path'][i + 1] + ': ' +
                      graph[result['path'][i]][result['path'][i + 1]] + ' kms')
        else:
            print('Path not found')

    else:
        print('Enter valid arguments')


main()