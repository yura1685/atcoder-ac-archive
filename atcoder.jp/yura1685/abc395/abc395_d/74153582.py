N, Q = map(int, input().split())

box_to_label = list(range(N))
label_to_box = list(range(N))
pigeon_to_box = list(range(N))

for _ in range(Q):
    q = [int(x) - 1 for x in input().split()]
    if q[0] == 0:
        pigeon, to = q[1], q[2]
        pigeon_to_box[pigeon] = label_to_box[to]
    elif q[0] == 1:
        label0, label1 = q[1], q[2]
        label_to_box[label0], label_to_box[label1] = label_to_box[label1], label_to_box[label0]
        box_to_label[label_to_box[label0]], box_to_label[label_to_box[label1]] = box_to_label[label_to_box[label1]], box_to_label[label_to_box[label0]]
    else:
        pigeon = q[1]
        print(box_to_label[pigeon_to_box[pigeon]] + 1)