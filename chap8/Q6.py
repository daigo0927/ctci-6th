from collections import deque

class Tower(object):
    def __init__(self, i):
        self.disks = deque([])
        self.index = i
        
    def add(self, d):
        if len(self.disks) < 0 and self.disks[-1] <= d:
            print(f'Error for placing disk size {d}')
        else:
            self.disks.append(d)

    def move_to_top(self, t):
        top = self.disks.pop()
        t.add(top)
        return t

    def print(self):
        print(f'Contents of tower {self.index} : {list(self.disks)}')
    
    def move_disks(self, n, t_dest, t_buff):
        if n > 0:
            tag = f'move {n} disks from {self.index} to {t_dest.index} with buffer {t_buff.index}'
            print(f'<{tag}>')
            self.move_disks(n-1, t_buff, t_dest)
            # print(f'<move top from {self.index} to {t_dest.index}>')
            # print('<before>')
            # print('<source print>')
            # self.print()
            # print(f'</source print>')
            # print('<dest print>')
            # print('<before>')
            t_dest = self.move_to_top(t_dest)
            # print('<after>')
            # print('<source print>')
            self.print()
            # print('</source print>')
            # print('dest print')
            t_dest.print()
            # print('</dest print>')
            # print('</after>')
            # print(f'</move top from {self.index} to {t_dest.index}>')
            t_buff.move_disks(n-1, t_dest, self)
            print(f'</{tag}>')


if __name__ == '__main__':
    n = 3
    towers = [Tower(i) for i in range(3)]
    
    for i in range(n, 0, -1):
        towers[0].add(i)
        
    towers[0].move_disks(n, towers[2], towers[1])
