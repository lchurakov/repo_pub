import math


def recursion(size, out=[]):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    if size == 1:
        out.append(alphabet[size - 1])
    else:
        out.append(alphabet[size - 1])
        recursion(size - 1)
        out.append(alphabet[size - 1])
    return out


def draw_rangoli(start_list, central_string, draw_recursion_param, cut_symb_lr):
    if draw_recursion_param == 2:
        print('-'.join(start_list))

    else:
        second = '-'.join(start_list[cut_symb_lr:-cut_symb_lr])
        print(second.center(len(central_string), '-'))
        draw_rangoli(start_list, central_string, draw_recursion_param - 1, cut_symb_lr - 1)
        print(second.center(len(central_string), '-'))


def rangoli(size):
    start_list = recursion(n)  # Call of recursive function create central string symbols
    central_string = '-'.join(start_list)  # Creating a central string. From this string program will be positioning by
    # line x.
    draw_recursion_param = math.trunc(len(start_list) / 2 + 2)  # Recursion depth parameter.
    draw_rangoli(start_list, central_string, draw_recursion_param, cut_symb_lr=n - 1)  # Call of recursive function to
    # draw Rangoli.



if __name__ == '__main__':
    n = int(input())
    rangoli(n)