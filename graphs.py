# a breadth-first search function to find if within a network we know a doctor

from collections import deque


def person_is_doctor(name):
    return name == 'jonny'


graph = {}

graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']

# anuj, peggy, thom, and jonny don't have neighbours.
# They have arrows pointing to them, but no arrows from them to someone else.
# this is called a directed graph

graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_doctor(person):
                print(f"{person} is a doctor")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('bob')