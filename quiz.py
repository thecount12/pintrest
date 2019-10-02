"""
Question, write a function to take two lists, input1 and input2, as the input and return a merged list as below
input1 = [1, 2, 3, 4]
input2 = ["a", "b", "c", "d", "e"]
return [1, "a", 2, "b", 3, "c", 4, "d", "e"]
"""


def merge_list(list1, list2):
    """
    :param list1: list of integers
    :param list2: list of str
    :return: list of int and str in order
    """
    special_list = []
    count = 0
    if len(list1) >= len(list2):
        count = len(list1)
    else:
        count = len(list2)
    if all(isinstance(item, int) for item in list1) and all(isinstance(item, str) for item in list2):
        for line in range(count):
            if line < len(list1):
                special_list.append(list1[line])
            if line < len(list2):
                special_list.append(list2[line])
    return special_list


if __name__ == "__main__":
    input1 = [1,  2, 3, 4]
    input2 = ["a", "b", "c", "d", "e"]
    print(merge_list(input1, input2))
