def solution(targets):
    targets = sorted(targets)
    count = 1
    rocket = targets[0][1]
    for i in targets[1:]:
        start, end = i
        if rocket <= start:
            count += 1
            rocket = end
        if rocket > end:
            rocket = end
    return count
    