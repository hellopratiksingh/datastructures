from collections import deque

def zigzagLevelOrder(root):
    if not root:
            return []
    res = []
    q = deque()

    p = root
    res.append([p.val])
    q.append(p)
    while len(q) > 0:
        lvl = []
        for i in range(len(q)):
            p = q.popleft()
            if p.left:
                lvl.append(p.left.val)
                q.append(p.left)

            if p.right:
                lvl.append(p.right.val)
                q.append(p.right)

        if lvl:
            res.append(lvl)

    for i in range(len(res)):
        if i % 2 != 0:
            res[i] = res[i][::-1]

    return res
