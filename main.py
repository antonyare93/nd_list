nd_index_list = []

def recalculate_values(nd_indexes: list, initial_value: int):
    has_changed = False
    while not has_changed:
        for index, value in enumerate(nd_indexes):
            if nd_indexes[(index+1)*-1] == 0:
                
        print(pos)
        if pos == 0:
            pos == initial_value
            next
        nd_indexes[index] -= 1
    return nd_indexes

n = 5
shape = 100
init_list = [shape for i in range(n)]
while not all(init_list) == 0:
    nd_index_list.append(tuple(init_list))
    print(tuple(init_list))
    init_list = recalculate_values(init_list, shape)

print(nd_index_list)