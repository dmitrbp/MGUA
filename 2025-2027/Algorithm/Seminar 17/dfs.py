def dfs_iterative(graph, start):
    """
    Итеративный DFS с использованием стека
    graph: dict {vertex: [neighbors]}
    """
    visited = set()
    stack = [start]
    parent = {start: None}

    while stack:
        vertex = stack.pop()  # Извлекаем из КОНЦА стека (LIFO)

        if vertex not in visited:
            visited.add(vertex)
            print(f"Посещаем: {vertex}")

            # Добавляем соседей в стек (в обратном порядке для сохранения порядка)
            for neighbor in reversed(graph[vertex]):  # reversed для сохранения исходного порядка
                if neighbor not in visited:
                    stack.append(neighbor)
                    if neighbor not in parent:
                        parent[neighbor] = vertex

    return visited, parent


# Пример использования
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_iterative(graph, 'A')
# Порядок: A -> C -> F -> B -> E -> D (зависит от порядка добавления)