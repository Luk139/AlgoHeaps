from typing import List
from CityDataManagement.City import City
from CityDataManagement.AbstractCityHeap import AbstractCityHeap, get_parent_index


class CityMaxHeap(AbstractCityHeap):
    """
    Class with the responsibility to create a Max-Heap-structure based on unstructured data.
    (Every Parents Key must be greater than its children Key)

    """

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        """
        Creation of a Max-City-Heap.

        :param raw_city_data:    A unsorted List of Cities
        :param recursive:    Should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
        :param floyd:       Should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.
                            For removal the approach specified in :param recursiv will be used.
        """
        super().__init__(raw_city_data, recursive, floyd)

    def heapify_up_iterative(self):
        """
        establish heap conditions for a Max-Heap iterative upwards.
        """
        index = self.currentHeapLastIndex - 1  # start at the last node in the heap

        while self.has_parent(index) and self.get_city_population(index) > self.get_parent_population(index):
            # while the node has a parent and the population of the current node is greater than the population of
            # the parent
            self.swap_nodes(index, get_parent_index(index))
            index = get_parent_index(index)  # update the index to the parent

    def heapify_up_recursive(self, index):
        """
        Establish heap conditions for a Max-Heap recursive upwards.
        """
        if not self.has_parent(index):  # base case: node has no parent, stop recursion
            return

        parent_index = get_parent_index(index)

        if self.get_city_population(index) > self.get_parent_population(index):
            # if the population of the current node is greater than the population of the parent
            self.swap_nodes(index, parent_index)
            self.heapify_up_recursive(parent_index)  # recursive call with the parent index

    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions via Floyds Heap Construction Algorithmus
        """
        largest = index  # initialize largest as root
        l = 2 * index + 1  # left =

    def heapify_down_iterative(self):
        # Find the index of the last element in the heap
        # Only here because Pycharm is annoyed by a not global parent_index variable.
        global parent_index
        last_index = len(self.rawCityData) - 1

        # Start at the last element
        current_index = last_index

        # While the current element is not the root
        while current_index > 0:
            # Find the index of the parent element
            parent_index = (current_index - 1) // 2

        # If the value of the current element is greater than its parent, swap them
        if self.heapStorage[current_index] > self.heapStorage[parent_index]:
            self.heapStorage[current_index], self.heapStorage[parent_index] = self.heapStorage[parent_index], self.heapStorage[current_index]

        # Move on to the next element
        current_index = parent_index

    def heapify_down_recursive(self, index):
        # Find the indices of the left and right children
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Find the index of the largest element
        largest_index = index
        if left_child_index < len(self.heapStorage) and self.heapStorage[left_child_index] > self.heapStorage[largest_index]:
            largest_index = left_child_index
        if right_child_index < len(self.heapStorage) and self.heapStorage[right_child_index] > self.heapStorage[largest_index]:
            largest_index = right_child_index

        # If the largest element is not the current element, swap them and heapify down recursively
        if largest_index != index:
            self.heapStorage[index], self.heapStorage[largest_index] = self.heapStorage[largest_index], self.heapStorage[index]
            self.heapify_down_recursive(largest_index)

    def remove(self):
        # Find the city object in the heap using its name
        city_index = -1
        for i in range(len(self.heapStorage)):
            if self.heapStorage[i].name == City:
                city_index = i
                break

        # Remove the city object from the heap
        if city_index != -1:
            self.heapStorage[city_index] = self.heapStorage[-1]
            self.heapStorage.pop()

            # Bubble down the remaining elements to restore the heap property
            self.bubble_down(city_index)

    def bubble_down(self, index):
        # Get the left and right child indices
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # If the left child index is within the bounds of the heap, compare the element at the index
        # to its left child
        if left_child_index < len(self.heapStorage):
            # If the element is smaller than its left child, swap them and continue bubbling down
            # from the left child's index
            if self.heapStorage[index] < self.heapStorage[left_child_index]:
                self.heapStorage[index], self.heapStorage[left_child_index] = self.heapStorage[left_child_index], \
                self.heapStorage[index]
                self.bubble_down(left_child_index)

        # If the right child index is within the bounds of the heap, compare the element at the index
        # to its right child
        if right_child_index < len(self.heapStorage):
            # If the element is smaller than its right child, swap them and continue bubbling down
            # from the right child's index
            if self.heapStorage[index] < self.heapStorage[right_child_index]:
                self.heapStorage[index], self.heapStorage[right_child_index] = self.heapStorage[right_child_index], \
                self.heapStorage[index]
                self.bubble_down(right_child_index)

        


