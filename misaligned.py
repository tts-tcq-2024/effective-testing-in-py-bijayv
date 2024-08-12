
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    sep = len(major_colors[0])
    for i, major in enumerate(major_colors):
        if(len(major) > sep):
            sep = len(major)
        for j, minor in enumerate(minor_colors):
            if(len(minor) > sep):
                sep = len(minor)

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {sep} | {major} | {sep} | {minor}')
    return len(major_colors) * len(minor_colors)


result = print_color_map()
assert(result == 25)
print("All is well (maybe!)\n")
