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

def findRoutes(caves, route):
    routes = 0
    state = route[-1]
    if state == 'end':
        return 1
    for nxt in caves[state]:
        if nxt.islower() and nxt in route:
            continue
        route2 = route.copy()
        route2.append(nxt)
        routes += findRoutes(caves, route2)
    return routes

route = ['start',]
routes = findRoutes(caves, route)

print(routes)