# 写一段冒泡排序的python代码
def bubble_sort(arr):
    n = len(arr)
    # 外层循环控制需要比较的轮数
    for i in range(n):
        # 内层循环控制每轮需要比较的次数
        for j in range(0, n-i-1):
            # 如果前一个元素大于后一个元素，则交换它们的位置
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# 测试代码
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print("原始数组:", test_array)
    sorted_array = bubble_sort(test_array)
    print("排序后数组:", sorted_array)
