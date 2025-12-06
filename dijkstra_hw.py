import heapq
from collections import deque
from random import randint
import math

class Graph():
    def __init__(self, field) -> None:
        self.edges = {} 
        self.field = field
    
    def field_to_graph(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), 
                     (0, -1),           (0, 1), 
                     (1, -1),  (1, 0),  (1, 1)]
        
        for x in range(len(self.field)):
            for y in range(len(self.field[x])):
                if self.field[x][y] == -1:
                    continue   
                if (x, y) not in self.edges:
                    self.edges[(x, y)] = []
                for dx, dy in directions:
                    x_new = x + dx
                    y_new = y + dy
                    if (0 <= x_new < len(self.field) and 0 <= y_new < len(self.field[x]) and self.field[x_new][y_new] != -1):
                        self.edges[(x, y)].append((x_new, y_new))  
        
        return self.edges
    
    def speed_type(self, cell_type):
        if cell_type == 0:
            return 1.0 
        elif cell_type == 1:
            return 0.75 
        elif cell_type == 2:
            return 0.5
        else: return 0 
    
    def calculate_time(self, start, end, path_mode=False):
        sx, sy = start
        ex, ey = end
        if sx != ex and sy != ey: # диагональое расстояние
            distance = round(math.sqrt(2 * (10 ** 2)), 2)
        else: distance = 10 # горизон./вертикал. расстояние
        
        speed_start = self.speed_type(self.field[sx][sy])
        speed_end = self.speed_type(self.field[ex][ey])
        half_distance = distance / 2
        
        if speed_start > 0 and speed_end > 0:
            time_first_half = half_distance / (speed_start * 10)  
            time_second_half = half_distance / (speed_end * 10) 
        else: 
            time_first_half = float('inf')
            time_second_half = float('inf')
        total_time = time_first_half + time_second_half
        
        return round(total_time, 2)
    
    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.edges}
        distances[start] = 0
        previous_nodes = {node: None for node in self.edges}
        
        pq = [(0, start)]
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            if current_node == end:
                break
            if current_distance > distances[current_node]:
                continue
            for neighbor in self.edges[current_node]:
                time = self.calculate_time(current_node, neighbor)
                if time == float('inf'):
                    continue
                
                new_distance = current_distance + time
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor))
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()
        
        return distances[end], path
    
    def find_time(self, start, end, output_path=False):
        if start not in self.edges or end not in self.edges:
            print("В точку невозможно попасть")
            return None
        
        total_time, path = self.dijkstra(start, end)
        
        if output_path:
            self.print_path(path)
        
        return round(total_time, 2)
    
    def print_path(self, path):
        if not path:
            print("error2")
            return
        
        for i, node in enumerate(path):
            if i < len(path) - 1:
                print(f"{node} -> ", end="")
            else:
                print(f"{node}")

n = int(input("Введите количество строк (N): "))
m = int(input("Введите количество столбцов (M): "))
    
field = []
for i in range(n):
    row = []
    for col in range(m):
        row.append(randint(-1, 2))
    field.append(row)
    
print("\nИгровое поле:")
for i in range(len(field)):
    print(field[i])
    
g = Graph(field)
g.field_to_graph()
    
print("\nГраф:")
for node, neighbors in g.edges.items():
    print(f"{node}: {neighbors}")

start_x = int(input("\nНачальная точка по х: "))
start_y = int(input("Начальная точка по у: "))
end_x = int(input("Конечная точка по х: "))
end_y = int(input("Конечная точка по у: "))

start = (start_x, start_y)
end = (end_x, end_y)

print("\nМаршрут кратчайшего пути:")
total_time = g.find_time(start, end, output_path=True)
if total_time is not None:
    print(f"\nВремя от {start} до {end} (диагональ): {total_time}")