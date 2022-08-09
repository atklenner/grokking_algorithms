from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_we_are_looking_for(person):
    return person[-1] == "m"

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

print(search("you"))