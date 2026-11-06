from collections import deque


def bfs(graph, start, goal=None):
    """
    graph: dict {vertex: [neighbors]}
    start: начальная вершина
    goal: целевая вершина (опционально)
    """
    visited = set([start])
    queue = deque([start])
    parent = {start: None}
    distance = {start: 0}

    while queue:
        vertex = queue.popleft()  # O(1) - эффективно

        print(f"Посещаем вершину: {vertex}")

        if vertex == goal:
            print(f"Цель найдена! Расстояние: {distance[vertex]}")
            return parent, distance

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                distance[neighbor] = distance[vertex] + 1
                queue.append(neighbor)

    return parent, distance  # Если цель не найдена


# Восстановление пути
def get_path(parent, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    return list(reversed(path))


# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

parent, dist = bfs(graph, 'A', 'F')
print(f"Путь: {get_path(parent, 'A', 'F')}")  # A -> C -> F или A -> B -> E -> F (BFS найдет первый)