# Самая далекая планета

def find_farthest_orbit(orbits):
    lst = []
    for i in orbits:
        lst.append(sum(list(i)))
    for i in orbits:
        if sum(list(i)) == max(lst):
            print(list(i))

orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
find_farthest_orbit(orbits)