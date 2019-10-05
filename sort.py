"""排序"""

class Sort:
    def __init__(self,lst):
        self.lst = lst

    #冒泡排序
    def bubble(self):
        #外层循环表示 轮数
        for i in range(len(self.lst)-1):
            #内层循环表示 比较次数
            for j in range(len(self.lst)-i-1):
                #左右两个数比较
                if self.lst[j] > self.lst[j+1]:
                    self.lst[j],self.lst[j+1] = self.lst[j+1],self.lst[j]

    #选择排序
    def select(self):
        #外层循环表示 轮数
        for i in range(len(self.lst)-1):
            #每轮选取第一个作为最小
            min = i
            #内层循环表示 比较次数
            for j in range(i+1,len(self.lst)):
                if self.lst[min] > self.lst[j]:
                    min = j
            if i != min:
                self.lst[i],self.lst[min] = self.lst[min],self.lst[i]


    #插入排序
    def insert(self):
        #外层循环表示 轮数
        for i in range(1,len(self.lst)):
            #取出每一轮的数
            x = self.lst[i]
            j = i
            #内层循环表是比较的次数
            while j > 0 and self.lst[j-1] > x:
                self.lst[j] = self.lst[j-1]
                j -= 1
            self.lst[j] = x

    #快排
    def sub_sort(self,low,high):
        #一轮交换
        key = self.lst[low]
        while low < high:
            #后面的数往前甩
            while low < high and self.lst[high] >= key:
                high -= 1
            self.lst[low] = self.lst[high]

            #前面的数往后甩
            while low < high and self.lst[low] < key:
                low += 1
            self.lst[high] = self.lst[low]
        self.lst[low] = key
        return low

    def quick(self,low,high):
        #快排函数
        if low < high:
            key = self.sub_sort(low,high)
            self.quick(low,key -1)
            self.quick(key +1,high)


#二分查找法
def search(ls,key):
    #初始值
    low = 0
    #终值
    high = len(ls)-1

    while low <= high:
        mid = (low + high) // 2
        if ls[mid] < key:
            low = mid + 1
        elif ls[mid] > key:
            high = mid - 1
        else:
            return mid
    return



if __name__ == '__main__':
    ls = [2,4,1,2,5,7,99,65,42,22,88,3,1,77,65,8]

    st = Sort(ls)

    # 冒泡排序
    # st.bubble()

    # 选择排序
    # st.select()

    # 插入排序
    # st.insert()

    # 快速排序
    st.quick(0,len(ls)-1)

    print(ls)


