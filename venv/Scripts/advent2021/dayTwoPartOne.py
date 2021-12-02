def calculate_coordinates():
    text = open("input", "r")
    lines = text.readlines()
    print(lines)
    horizontal = 0
    depth = 0
    for i in range (len(lines)):
        position = lines[i].split(" ")
        direction = position[0]
        distance = int(position[1].strip())

        if direction == "forward":
            horizontal += distance
        elif direction == "down":
            depth += distance
        else:
            depth -= distance
    print(horizontal)
    print(depth)
    print(horizontal*depth)

if __name__ == '__main__':
    calculate_coordinates()

