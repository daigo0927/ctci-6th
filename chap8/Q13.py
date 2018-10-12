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

def create_stack(boxes, bottom_index):
    box_b = boxes[bottom_index]
    max_height = 0
    for i in range(bottom_index+1, len(boxes)):
        if boxes[i].is_smaller(box_b):
            height = create_stack(boxes, i)
            max_height = max(height, max_height)

    max_height += box_b.height
    return max_height

if __name__ == '__main__':
    boxes = [Box(6, 4, 4), Box(8, 6, 2), Box(5, 3, 3),
             Box(7, 8, 3), Box(4, 2, 2), Box(9, 7, 3)]
    boxes = sorted(boxes, key = lambda b: b.height, reverse = True)

    max_height = create_stack(boxes, 0)
    print(f'Max height is {max_height}')
