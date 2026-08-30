class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        visited = set()
        def dfs(course):
            if adjList[course] == []:
                return True
            if course in visited:
                return False
            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq): return False
            visited.remove(course)
            adjList[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True