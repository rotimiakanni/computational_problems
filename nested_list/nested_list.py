from os.path import realpath, join, dirname

def get_second_lowest_grade():
    """
    Given the names and grades for each student in a class of  students, 
    store them in a nested list and print the name(s) of any student(s) 
    having the second lowest grade.

    Sample Input: 
    5
    Harry
    37.21
    Berry
    37.21
    Tina
    37.2
    Akriti
    41
    Harsh
    39

    Sample Output:
    Berry
    Harry

    Explanation:
    There are  students in this class whose names and grades are assembled to 
    build the following list: 
    python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, 
    so we order their names alphabetically and print each name on a new line.
    """
    stdnt_list = []
    # Get data from std input
    input_file = join(dirname(realpath(__file__)), 'sample.txt')
    with open(input_file) as ip_file:
        for _ in range(int(ip_file.readline())):
            name = ip_file.readline()
            score = float(ip_file.readline())
            stdnt_list.append([name, score])
    # sort student list and convert to dictionary to iterate by key 
    # value pairs which is computationally faster
    stdnt_list = sorted(stdnt_list, key=lambda x:x[1])
    stdnt_dict = dict(stdnt_list)
    # Get a list of the values to get the smallest
    stdnt_values = stdnt_dict.values()
    min_stdnt_value = min(stdnt_values)
    # remove the smallest score first
    del_lis = []
    for k, v in stdnt_dict.items():
        if v == min_stdnt_value:
            del_lis.append(k)
    for itm in del_lis:
        del stdnt_dict[itm]
    # get the next smallest score
    stdnt_values = stdnt_dict.values()
    min_stdnt_value = min(stdnt_values)
    # Get thee names of second smallest in a seperate list
    # Using list comprehension because it's fairly fast computationally 
    answer_list = [str(k) if v==min_stdnt_value else 'zzzz' for k,v in stdnt_dict.items()]
    answer_list = sorted(answer_list)
    for person in answer_list:
        if person != 'zzzz':
            print(person)

if __name__ == '__main__':
    get_second_lowest_grade()