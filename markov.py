import random


class MarkovChain():
    def __init__(self, edges):
        self.adj_list = dict()
        for v, w, weight in edges:
            if v not in self.adj_list:
                self.adj_list[v] = set()
            if w not in self.adj_list:
                self.adj_list[w] = set()

            self.adj_list[v].add((w, weight))
    
    def simulate(self, v, n):
        trajectory = [v]
        for _ in range(n):
            w = self.sample(self.adj_list[v])
            v = w
            trajectory.append(v)
        return trajectory
        
    # Sample an element from a probability distribution vector
    def sample(self, distribution):
        u = random.random()
        cumulative_sum = 0
        for w, weight in distribution:
            cumulative_sum += weight
            if u < cumulative_sum:
                return w        
    

    def dfs(self, v, visited, postorder: list=None):
        visited.add(v)
        for w, _ in self.adj_list[v]:
            if w not in visited:
                self.dfs(w, visited, postorder)
        # Modification for Kosaraju's algorithm
        if postorder is not None:
            postorder.append(v)
            return postorder
    
    def transpose(self):
        transposed_edges = []
        for v, edge in self.adj_list.items():
            for w, weight in edge:
                transposed_edges.append((w, v, weight))
        return MarkovChain(transposed_edges)
    
    def kosaraju(self):
        visited = set()
        postorder = []
        for v in self.adj_list.keys():
            if v not in visited:
                po = self.dfs(v, visited, [])
                postorder.extend(self.dfs(v, visited, []))
        
        mc_transpose = self.transpose()
        visited = set()
        classes = []

        while postorder:
            v = postorder.pop()
            if v not in visited:
                _class = set(mc_transpose.dfs(v, visited, []))
                classes.append(_class)
        return classes