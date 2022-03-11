"""
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
"""
rooms = [[1,3],[3,0,1],[2],[0]]


def canVisitAllRooms(rooms):

    seen = [False]*len(rooms)
    seen[0] = True

    stack = [0]
    while stack:
        node = stack.pop()
        for nei in rooms[node]:
            if not seen[nei]:
                seen[nei] = True
                stack.append(nei)    
    return all(seen)


def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        
        def dfs(room: int) -> None:
            if room not in visited: 
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    to_visit = [0]

    while to_visit:
        room = to_visit.pop()
        if room in visited: continue
        visited.add(room)
        to_visit.extend(rooms[room])
            
    return len(visited) == len(rooms)


def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    
    visited = set()
    
    def dfs(room: int) -> None:
        if room not in visited: 
            visited.add(room)
            for key in rooms[room]:
                dfs(key)
    dfs(0)
    return len(visited) == len(rooms)

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    to_visit = [0]

    while to_visit:
        room = to_visit.pop()
        if room in visited: continue
        visited.add(room)
        to_visit.extend(rooms[room])
            
    return len(visited) == len(rooms)

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = set()
    to_visit = {0}

    while to_visit:
        room = to_visit.pop()
        visited.add(room)
        to_visit |= set(rooms[room])-visited
            
    return len(visited) == len(rooms)

def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = 0
    ct = 0
    to_visit = [0]
    
    while to_visit:
        room = to_visit.pop()
        
        mask = 1 << room
        if visited & mask: continue
        
        visited |= mask
        ct += 1
        to_visit.extend(rooms[room])
			
def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    visited = [0] * len(rooms)
    to_visit = [0]
    
    while to_visit:
        room = to_visit.pop()
        if visited[room]: continue
        visited[room] = 1
        to_visit.extend(rooms[room])
    
    return sum(visited) == len(rooms)
        
print(
    canVisitAllRooms(rooms)
)