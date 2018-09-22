def compute_byte_num(width, x, y):
    return (width*y + x) // 8

def draw_line(screen, width, x1, x2, y):
    start_offset = x1%8
    first_full_bytes = x1//8
    if start_offset != 0:
        first_full_bytes += 1

    end_offset = x2%8
    last_full_bytes = x2//8
    if end_offset != 7:
        last_full_bytes -= 1

    for b in range(first_full_bytes, last_full_bytes+1):
        screen[(width//8) * y + b] = 0xFF

    start_mask = 0xFF>>start_offset
    end_mask = ~(0xFF>>(end_offset+1))

    if x1//8 == x2//8:
        mask = start_mask&end_mask
        screen[(width//8) * y + (x1 // 8)] |= mask
    else:
        if start_offset != 0:
            byte_number = (width//8) * y + first_full_bytes - 1
            screen[byte_number] |= start_mask
        if end_offset != 7:
            byte_number = (width//8) * y + last_full_bytes + 1
            screen[byte_number] |= end_mask
            
    return screen

def print_byte(b):
    for i in range(7, -1, -1):
        c = '1' if (b>>i)&1 == 1 else '_'
        print(c, end = "")

def print_screen(screen, width):
    height = len(screen)*8//width
    for r in range(height):
        for c in range(0, width, 8):
            b = screen[compute_byte_num(width, c, r)]
            print_byte(b)
        print('')


if __name__ == '__main__':
    width = 8*1
    height = 1
    for r in range(height):
        for c1 in range(width):
            for c2 in range(c1, width, 2):
                screen = [0]*(width*height//8)

                print(f'Row {r} : {c1} -> {c2} : ', end = '')
                screen = draw_line(screen, width, c1, c2, r)
                print_screen(screen, width)

