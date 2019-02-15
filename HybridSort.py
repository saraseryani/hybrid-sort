def merge_sort(unsorted, threshold, reverse):
    """
    Merges and sorts two lists
    :param unsorted: the unsorted list
    :param threshold: the index to sort up to
    :param reverse: a bool to reverse the list
    :return: a merged sorted list
    """
    n = len(unsorted)

    if n < 2:
        return unsorted

    elif n <= threshold:
        insertion_sort(unsorted, reverse)
    mid = n // 2
    S1 = unsorted[0:mid]
    S2 = unsorted[mid:n]
    nS1 = merge_sort(S1, threshold, reverse)
    nS2 = merge_sort(S2, threshold, reverse)
    return merge(nS1, nS2, reverse)


def merge(first, second, reverse):
    """
    Merges two items
    :param first: first item
    :param second: second item
    :param reverse:  a bool to reverse the list
    :return: a list of two merged items
    """
    i = j = 0
    combine = first + second

    if reverse:
        while(i + j < len(combine)):
            if j == len(second) or (i < len(first) and first[i] > second[j]):
                combine[i+j] = first[i]
                i += 1
            else:
                combine[i+j] = second[j]
                j += 1
    if not reverse:
        while(i + j < len(combine)):
            if j == len(second) or (i < len(first) and first[i] < second[j]):
                combine[i+j] = first[i]
                i += 1
            else:
                combine[i+j] = second[j]
                j += 1

    return combine


def insertion_sort(unsorted, reverse):
    """
    Inserts and sorts the objects into a list
    :param unsorted: an unsorted list
    :param reverse:  a bool to reverse the list
    :return: a list
    """
    n = len(unsorted)

    if reverse:
        for i in range(1, n):
            current = unsorted[i]
            j=i
            while j > 0 and unsorted[j-1] < current:
                unsorted[j] = unsorted[j-1]
                j -= 1
            unsorted[j] = current

    else:
        for i in range(1, n):
            current = unsorted[i]
            j=i
            while j > 0 and unsorted[j-1] > current:
                unsorted[j] = unsorted[j-1]
                j -= 1
            unsorted[j] = current

    return unsorted
