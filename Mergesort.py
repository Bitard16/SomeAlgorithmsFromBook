# Realisation of MergeSort

data = [9,5,7,4,11,12,345]


def MergeSort(list):
    # Проверяем разбит ли список на отдельные части
    if len(list) < 2:
        return list
    # Находим середину списка
    middle = len(list)//2

    # Разбиваем список на 2 части
    left = MergeSort(list[:middle])
    right = MergeSort(list[middle:])

    # Объеденеям отсортированные части в одну
    print("Левая часть:",left)
    print("Правая часть :",right)
    # Объединены
    print("Объединены", merge)
    return merge


def merge(left,right):
    # Если левая и правая часть пуста и мы имеем дело с единственной частью которая уже отсортирована
    if not len(left):
        return left
    if not len(right):
        return right

    # Определение переменных для процесса слияния
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    #Работаем пока не будут обьединены все элементы

    while (len(result) < totalLen):
        #Выполняем сравнения и славаем части в соответвии со значением элементов
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(left[rightIndex])
            rightIndex += 1
        #  Если левая и правая часть длинее , добавляем
        # оставшиееся элементы к результату
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
    return result

data2 = MergeSort(data)

print(MergeSort(data))
print(data2)


