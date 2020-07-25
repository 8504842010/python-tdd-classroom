def reverse_list(input_list):

    length = len(input_list) - 1
    l1 = []
    while length >= 0:
        l1.append(input_list[length])
        length = length - 1
    return l1


def count_digits(number):
    str1=str(number)
    lgth=len(str1)
    return lgth

