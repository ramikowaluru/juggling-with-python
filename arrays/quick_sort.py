class QuickSort:
    def __init__(self, list_of_values):
        self.list_of_elements = list_of_values

    def partition(self, low, high):
        pivot_position_temp = low - 1
        pivot = self.list_of_elements[high]
        for i in range(low, high):
            if self.list_of_elements[i] <= pivot:
                pivot_position_temp += 1
                self.list_of_elements[pivot_position_temp], self.list_of_elements[i] = self.list_of_elements[i], \
                                                                                       self.list_of_elements[
                                                                                           pivot_position_temp]
        self.list_of_elements[pivot_position_temp+1],self.list_of_elements[high] = self.list_of_elements[high], \
                                                                                   self.list_of_elements[pivot_position_temp+1]

        return pivot_position_temp + 1

    def quick_sort(self, low, high):
        if len(self.list_of_elements) == 1:
            return self.list_of_elements
        if low < high:
            pivot_position = self.partition(low, high)
            self.quick_sort(low, pivot_position - 1)
            self.quick_sort(pivot_position + 1, high)


if __name__ == '__main__':
    q = QuickSort([12, 69654, 12, 32, 2, 16, 1, 6])
    q.quick_sort(0, len(q.list_of_elements) - 1)
    print(q.list_of_elements)
