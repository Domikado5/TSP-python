import numpy as np
from math import sqrt


def calc_dist(x1: float, y1: float, x2: float, y2: float):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


# def find_min(ind, data): # to zakomentowane to raczej zle xD
#     for index in range(len(data)):
#         if not np.array_equal(data[ind], data[index]):
#             tmp_min = calc_dist(data[ind][0], data[ind][1], data[index][0], data[index][1])
#             tmp_index = index
#             break
#     for index in range(len(data)):
#         next_min = calc_dist(data[ind][0], data[ind][1], data[index][0], data[index][1])
#         if next_min < tmp_min and next_min != 0:
#             tmp_min = next_min
#             tmp_index = index
#     return tmp_min, tmp_index
#
#
# def main(data):
#     dist = 0
#     current_pos = 0
#     while len(data) > 1:
#         to_add, current_pos = find_min(current_pos, data)
#         dist += to_add
#         data = np.delete(data, current_pos, axis=0)
#     return dist
def find_min(curr_pnt, data, vis):
    for index in range(len(data)):
        if not np.array_equal(data[curr_pnt], data[index]) and index not in vis:
            tmp_min = calc_dist(data[curr_pnt][0], data[curr_pnt][1], data[index][0], data[index][1])
            tmp_index = index
            break
    for index in range(len(data)):
        next_min = calc_dist(data[curr_pnt][0], data[curr_pnt][1], data[index][0], data[index][1])
        if index not in vis and tmp_min > next_min > 0:
            tmp_min = next_min
            tmp_index = index
    return tmp_min, tmp_index


def main(data, vis):
    pos = 0
    dist = 0
    vis.add(pos)
    path = []
    while len(vis) < len(data):
        to_add, pos = find_min(pos, data, vis)
        dist += to_add
        vis.add(pos)
        path.append(pos)
    dist += calc_dist(data[0][0], data[0][1], data[pos][0], data[pos][1])
    return dist


cities = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], dtype=np.float32)
visited = set()
print(main(cities, visited))
