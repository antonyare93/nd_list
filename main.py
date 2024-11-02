nd_index_list = []

def recalculate_values(nd_indexes: list, initial_value: int):
    has_changed = False
    index = 1
    while not has_changed:
        if nd_indexes[-index] == 0:
            nd_indexes[-index] = initial_value
            index += 1
            continue
            
        nd_indexes[-index] -= 1
        has_changed = not(has_changed)

    return nd_indexes

n = 5
shape = 10
init_list = [shape-1 for i in range(n)]
while not all(x == 0 for x in init_list):
    nd_index_list.append(tuple(init_list))
    init_list = recalculate_values(init_list, shape)
    if all(x == 0 for x in init_list):
        nd_index_list.append(tuple(init_list))

nd_index_list.reverse()
with open('./nd_index_list.txt', 'w') as f:
    f.write(str(nd_index_list))

