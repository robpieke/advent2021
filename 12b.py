with open('data/12.txt') as f:
    data = f.read().splitlines()

caves = {}

for d in data:
    s,e = d.split('-')
    if not s in caves:
        caves[s] = []
    caves[s].append(e)
    if not e in caves:
        caves[e] = []
    caves[e].append(s)

routes = 0

def findRoutes(caves, route, twice):
    routes = 0
    state = route[-1]
    if state == 'end':
        return 1
    for nxt in caves[state]:
        twice2 = twice
        if nxt.islower() and nxt in route:
            if twice or nxt == 'start':
                continue
            twice2 = True
        route2 = route.copy()
        route2.append(nxt)
        routes += findRoutes(caves, route2, twice2)
    return routes

route = ['start',]
routes = findRoutes(caves, route, False)

print(routes)