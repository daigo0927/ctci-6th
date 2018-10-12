class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = width
        self.depth = depth

    def is_smaller(self, box_tar):
        if self.width < box_tar.width and self.height < box_tar.height and self.depth < box_tar.depth:
            return True
        else:
            return False

def create_stack(boxes, box_b, offset, stack_map):
    if offset >= len(boxes):
        return 0
    
    box_b_new = boxes[offset]
    height_with_bottom = 0
    if box_b is None or box_b_new.is_smaller(box_b):
        if stack_map[offset] == 0:
            stack_map[offset] = create_stack(boxes, box_b_new, offset+1, stack_map)
            stack_map[offset] += box_b_new.height

        height_with_bottom = stack_map[offset]

    height_without_bottom = create_stack(boxes, box_b, offset+1, stack_map)
    
    return max(height_with_bottom, height_without_bottom)

if __name__ == '__main__':
    boxes = [Box(6, 4, 4), Box(8, 6, 2), Box(5, 3, 3),
             Box(7, 8, 3), Box(4, 2, 2), Box(9, 7, 3)]
    boxes = sorted(boxes, key = lambda b: b.height, reverse = True)

    stack_map = [0]*len(boxes)
    max_height = create_stack(boxes, None, 0, stack_map)
    print(f'Max height is {max_height}')
