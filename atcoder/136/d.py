maps = [s for s in str(input())]
people = [{'pos': i, 'prev': -1, 'loop': -1} for i in range(len(maps))]
max_count = 10**100


def update(people, index):
    for p in people:
        if maps[p['pos']] == 'R':
            if p['prev'] == p['pos'] + 1:
                p['loop'] = index
            p['prev'] = p['pos']
            p['pos'] += 1
        else:
            if p['prev'] == p['pos'] - 1:
                p['loop'] = index
            p['prev'] = p['pos']
            p['pos'] -= 1


def get_output(people):
    output = [0] * len(people)

    for p in people:
        output[p['pos']] += 1

    return ' '.join(str(i) for i in output)


for index in range(max_count):
    # print(index, 'before', get_output(people))
    update(people, index)
    # print(index, 'after', get_output(people))

    if len([p for p in people if p['loop'] < 0]) == 0:
        # print(get_output(people))
        for p in people:
            mod = (max_count - p['loop'] + 1) % 2
            # print(mod)
            for i in range(mod):
                if maps[p['pos']] == 'R':
                    p['prev'] = p['pos']
                    p['pos'] += 1
                else:
                    p['prev'] = p['pos']
                    p['pos'] -= 1
        # print(get_output(people))
        break

print(get_output(people))
