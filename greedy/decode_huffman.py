class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None


def add_code(node, code, letter):
    for i in range(len(code)):
        if code[i] == '0' and node.left:
            node = node.left
        elif code[i] == '0' and not node.left:
            node.left = Node()
            node = node.left          
        elif code[i] == '1' and node.right:
            node = node.right
        else:
            node.right = Node()
            node = node.right

        if i == len(code) - 1:
            node.value = letter

def decode(string, head):
    node = head
    result = ''
    for i in range(len(string)):
        if string[i] == '0' and node.left:
            node = node.left
        elif string[i] == '0' and not node.left:
            result += node.value
            node = head.left
        elif string[i] == '1' and node.right:
            node = node.right
        else:
            result += node.value
            node = head.right

        if i == len(string) - 1:
            result += node.value
    return result       

def main():
    count_letters, string_len = map(int, input().strip().split())
    dict_letters = {}
    for i in range(count_letters):
        l, c = input().split()
        dict_letters[l[0]] = c
    string_code = input()
    head = Node()
    for key, val in dict_letters.items():
        add_code(head, val, key)
    print(decode(string_code, head))


if __name__== '__main__':
    main()