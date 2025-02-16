graph = {}

graph["you"] = ["alice", "bob", "clare"]
graph["alice"] = ["peggi"]
graph["bob"] = ["anuj", "peggi"]
graph["clare"] = ["tom", "jonny"]
graph["peggi"] = []
graph["anuj"] = []
graph["peggi"] = []
graph["tom"] = []
graph["jonny"] = []

from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()

    def person_is_seller(name):
        return name[-1] == "m"

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False

search("you")