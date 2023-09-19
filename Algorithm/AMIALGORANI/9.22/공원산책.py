def solution(park, routes):
    row = len(park)
    col = len(park[0])
    x = 0
    y = 0
    for i in range(row):
        for j in range(col):
            if park[i][j] == 'S':
                x = i
                y = j
                break

    for route in routes:
        direction = route.split(" ")[0]
        distance = int(route.split(" ")[1])

        if direction == 'E':
            new_y = y
            for i in range(distance):
                new_y += 1
                if new_y >= col:
                    new_y = y
                    break
                elif park[x][new_y] == 'X':
                    new_y = y
                    break
            y = new_y
        elif direction == 'W':
            new_y = y
            for i in range(distance):
                new_y = new_y - 1
                if new_y < 0:
                    new_y = y
                    break
                elif park[x][new_y] == 'X':
                    new_y = y
                    break
            y = new_y

        elif direction == 'N':
            new_x = x
            for i in range(distance):
                new_x = new_x - 1
                if new_x < 0:
                    new_x = x
                    break
                elif park[new_x][y] == 'X':
                    new_x = x
                    break
            x = new_x

        elif direction == 'S':
            new_x = x
            for i in range(distance):
                new_x = new_x + 1
                if new_x >= row:
                    new_x = x
                    break
                elif park[new_x][y] == 'X':
                    new_x = x
                    break
            x = new_x
    return x, y

#print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
#print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))