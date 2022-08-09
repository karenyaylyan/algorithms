class Node:
    def __init__(self, value, frequency, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.value} - {self.frequency}'


def get_letter_frequency(string):
    d = {}
    for s in string:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return d


def generate_tree(lst):
    def min_node_pop(lst):
        result = 0
        for i in range(len(lst)):
            if lst[i].frequency < lst[result].frequency:
                result = i
        return lst.pop(result)

    while len(lst) > 1:
        min_1 = min_node_pop(lst)
        min_2 = min_node_pop(lst)
        lst.append(Node(min_1.value + min_2.value, min_1.frequency + min_2.frequency, left = min_1, right = min_2))
    return lst[0]


def make_dict_haff(node):
    result = {}

    def generate_code(node, acc_number=''):
        if node.left:
            generate_code(node.left, acc_number+'0')
        if node.right:
            generate_code(node.right, acc_number+'1')
        if not node.left and not node.right:
            result[node.value] = acc_number

    generate_code(node)
    return result

def build_string_huff(d, string):
    result = ''
    for s in string:
        result += d[s]
    return result

def show_letter_code(letter_code_dict):
    for key, value in letter_code_dict.items():
        print(f'{key}: {value}')

def main():
    string = input().rstrip()
    letter_frequency_dict = get_letter_frequency(string)
    if len(letter_frequency_dict) == 1:
        print(f'1 {len(string)}')
        print(f'{string[0]}: 0')
        print('0'*len(string))

    else:
        letter_frequency_nodes = [Node(key, value) for key, value in letter_frequency_dict.items()]
        head = generate_tree(letter_frequency_nodes)
        letter_code_dict = make_dict_haff(head)
        string_huff = build_string_huff(letter_code_dict, string)
        print(len(letter_code_dict), len(string_huff))
        show_letter_code(letter_code_dict)
        print(string_huff)
    

if __name__== '__main__':
    main()
