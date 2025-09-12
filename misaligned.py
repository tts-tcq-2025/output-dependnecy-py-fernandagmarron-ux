MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def iter_rows(): 
    for i, major in enumerate(MAJOR_COLORS):
        for j, minor in enumerate(MINOR_COLORS):
            yield i * 5 + j, major, minor

def format_row(n, major, minor): 
    return f'{n} | {major} | {minor}'

def build_table_text():
    return "\n".join(format_row(*row) for row in iter_rows())

def print_color_map():
    print(build_table_text())
    return len(MAJOR_COLORS) * len(MINOR_COLORS)

if __name__ == '__main__':
    result = print_color_map()
    assert(result == 25)
    print("All is well (maybe!)")
