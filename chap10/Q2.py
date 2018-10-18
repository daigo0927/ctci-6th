def sort(array):
    map_list = {}
    for string in array:
        key = sort_chars(string)
        if not key in map_list.keys():
            map_list[key] = [string]
        else:
            map_list[key].append(string)

    index = 0
    for key in map_list.keys():
        for t in map_list[key]:
            array[index] = t
            index += 1

    return array
        
def sort_chars(s):
    return ''.join(sorted(list(s)))

if __name__ == '__main__':
    array = ["apple", "banana", "carrot", "ele", "duck",
             "papel", "tarroc", "cudk", "eel", "lee"]
    array = sort(array)
    print(array)

