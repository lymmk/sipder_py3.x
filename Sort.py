# coding:utf-8
import time


# 冒泡排序
class bubble_sort():
    def __init__(self):
        pass
    def sort(self,list):
        for index in range(len(list)):
            for _index in range(len(list)-1-index):
                if list[_index] > list[_index+1]:
                    temp = list[_index]
                    list[_index] = list[_index + 1]
                    list[_index + 1] = temp
        print list
#





if __name__ == "__main__":
    list = [3,7,4,8,9,0,4,2,4,6,7,56,5,3,4,234,234,43,567,5,8,9,0,4,8,9,8,9,0,4,2,4,6,7,56,5,3,4,234,234,43,567,0,4,2,4,6,7,56,5,3,4,234,234,43,567,2,4,8,9,0,4,2,4,6,7,56,5,3,4,234,234,43,567,6,7,56,5,3,4,234,234,43,567,678,2345,234,312,4,564,213,12,1,45,7,435,24,456,]
    sort = bubble_sort()
    print "start:", time.time()
    sort.sort(list)
    print "end:", time.time()

