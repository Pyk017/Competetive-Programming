BusStops = [ "TH", "GA", "IC", "HA", "TE", "LU", "NI","CA" ]
Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
ls = list(zip(BusStops, Path))
n = len(Path)

def rate(src, dest):
    if src not in BusStops or dest not in BusStops:
        return "INVALID OUTPUT"

    i = (BusStops.index(src) + 1) % n
    j = (BusStops.index(dest) + 1) % n
    total = 0
    while True:
        total += ls[i][1]
        if i == j - 1:
            return round((total * 5) / 1000)
        i = (i + 1) % n


src = input()
dest = input()
res = rate(src, dest)
print(res)
