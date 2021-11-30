from os.path import realpath, join, dirname
from collections import deque

def get_edges(lis):
    return (lis[0], lis[-1])

def check_pile(pile_list):
    '''
    There is a horizontal row of  cubes. The length of each cube is given. 
    You need to create a new vertical pile of cubes. The new pile should 
    follow these directions: if  is on top of  then .

    When stacking the cubes, you can only pick up either the leftmost 
    or the rightmost cube each time. Print Yes if it is possible to stack t
    he cubes. Otherwise, print No.

    Example

    Result: No

    After choosing the rightmost element, , choose the leftmost element, . 
    After than, the choices are  and . These are both larger than the top block of size .

    Result: Yes
    Choose blocks from right to left in order to successfully stack the blocks.

    sample input:
    STDIN        Function
    -----        --------
    2            T = 2
    6            blocks[] size n = 6
    4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
    3            blocks[] size n = 3
    1 3 2        blocks = [1, 3, 2]

    sample output:
    Yes
    No
    '''
    last_pile = 0
    dequed_list = deque(pile_list)
    stackable = True
    while stackable and dequed_list:
        first, last = get_edges(dequed_list)
        if first >= last and last_pile == 0:
            dequed_list.popleft()
            last_pile = first
        elif first <= last and last_pile == 0:
            dequed_list.pop()
            last_pile = last
        elif first >= last and first <= last_pile:
            dequed_list.popleft()
            last_pile = first
        elif first <= last and last <= last_pile:
            dequed_list.pop()
            last_pile = last
        else:
            stackable = False
            break
    return 'Yes' if stackable else 'No'

input_file = join(dirname(realpath(__file__)), 'sample.txt')
ip_file = open(input_file)
for x in range(int(ip_file.readline())):
    list_len = int(ip_file.readline())
    pile_list = [int(x) for x in ip_file.readline().split()]
    print(check_pile(pile_list))
    