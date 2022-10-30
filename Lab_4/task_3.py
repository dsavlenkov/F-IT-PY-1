def delete(list_, index=-1):
    if index < 0:
        index = len(list_) + index
    return list_[:index] + list_[index + 1:]


def delete_2(list_, index=-1):  # альтернативная реализация, бессмысленная и беспощадная :)
    list_.pop(index)
    return list_


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
