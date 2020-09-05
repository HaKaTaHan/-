import heapq
def makeNode(begin, words):
    g = {}
    
    for i in words:
        count = 0
        for m in range(len(begin)):
            if begin[m] == i[m]:
                count += 1
                
        if count == len(begin) - 1:
            if g.get(begin) == None:
                g[begin] = {i: 1}
            else:
                temp = g.get(begin)
                temp.update({i: 1})
                g[begin] = temp
    
    for i in words:
        for j in words:
            if i == j:
                continue

            count = 0
            for m in range(len(begin)):
                if i[m] ==j[m]:
                    count += 1

            if count == len(begin) - 1:
                if g.get(i) == None:
                    g[i] = {j:1}
                else:
                    temp = g.get(i)
                    temp.update({j:1})
                    g[i] = temp

    return g

def daikstra(graph, begin, target):
    distances = {vertex: [float('inf'), begin] for vertex in graph}
    distances[begin] = [0, begin]

    queue = []

    heapq.heappush(queue, [distances[begin][0], begin])

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex][0] < current_distance:
            continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[adjacent][0]:
                distances[adjacent] = [distance, current_vertex]
                heapq.heappush(queue, [distance, adjacent])

    path = target
    path_output = 1
    while distances[path][1] != begin:
        path_output += 1
        path = distances[path][1]
    
    return path_output
        

def solution(begin, target, words):
    answer = 0
    graph = {}
    
    if target not in words:
        return 0

    graph = makeNode(begin, words)
    if len(graph) == 1:
        return 1
    answer = daikstra(graph, begin, target)

    return answer

print(solution(	"hit", "hot", ["hot"]))
