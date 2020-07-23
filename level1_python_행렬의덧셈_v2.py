# 파싱 버전_
import re


def solution(arr1, arr2):
    answer = par1(arr1, arr2)
    return answer


def solution_1(arr1, arr2):
    def addlists(a, b):
        return list(map(lambda x, y: x + y, a, b))
    return list(map(lambda x, y: addlists(x, y), arr1, arr2))


def par1(array, array2):
    ary1 = distributer(array)
    ary2 = distributer(array2)
    return solution_1(ary1, ary2)


def distributer(array):
    _array1, _array2 = array.split("], [")
    _array1 = list(map(int, ps.findall(_array1)))
    _array2 = list(map(int, ps.findall(_array2)))
    return [_array1]+[_array2]


init_input = input()
ps = re.compile('\d')
arr1, arr2 = init_input.split("]], [[")
solution(arr1, arr2)
