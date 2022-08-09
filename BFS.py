from collections import deque

graph = {}

def person_we_are_looking_for(person):
    pass

def search(starting_node):
    search_queue = deque()
    search_queue += graph[starting_node]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_we_are_looking_for(person):
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
