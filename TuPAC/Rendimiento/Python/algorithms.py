#-*-coding:utf-8-*-

class InsertionSort:
    def __init__(self):
        self.name = "Insert"

    def sort(self, data = []):
        
        for i in range(1, len(data)):
            current = data[i]

            while(i>0 and data[i-1]> current):
                data[i] = data[i-1]
                i = i-1
                data[i] = current

        return data

class SelectionSort:
    def __init__(self):
        self.name = "Select"

    def sort(self, data = []):
        for i in range(len(data)):
            min_indx = i
            for j in range (i+1, len(data)):
                if data[min_indx] > data[j]:
                    min_indx = j

            data[i], data[min_indx] = data[min_indx], data[i]

        return data

class BubbleSort:
    def __init__(self):
        self.name = "Bubble"

    def sort(self, data = []):
        for i in range (len(data)):

            for j in range (len(data)):

                if (data[j] < data[i]):
                    data[i], data[j] = data[j], data[i]

        return data

class QuickSort:
    def __init__(self):
        self.name = "Quick"

    def partition(self, arr, low, high):
        i = (low-1)
        pivot = arr[high]

        for j in range(low, high):
            if arr[j] <= pivot:
                i=i+1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return (i+1)

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)

            self.partition(arr, low, pi-1)
            self.partition(arr, pi+1, high)

    def sort(self, data = []):
        return self.quickSort(data, 0, len(data)-1)