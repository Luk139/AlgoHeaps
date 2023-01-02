from abc import ABC, abstractmethod
from typing import List
from CityDataManagement.City import City




class AbstractCityHeap(ABC):
    """
    Abstract Class with the responsibility to offer the common methods of both a Min and Max heap.

    This class is divided into two parts:

    -Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)

    -Shared Methods Block (Methods identical for both a min and a max heap)


    Param:
    ------
    rawCityData: List[City]: raw unsorted List of City Objects

    recursiv: bool: should the heapify be recursiv? False = use the iterative approach; True = Recursiv approach
    
    floyd: bool: should Floyds algorithm be used for insertion? True = instead of the iterative or recursiv approach Floyds algorithm will be used instead.

    Hint:   
    -----
    Think of the index of all elements in the heap as an array. Array: ([0],[1],[2],[3]...)
    The root is located at index 0, so it`s children must be on Index 1 and 2 and so on...
    """

    heapStorage: List[City] = [0]  # empty List of City Objects
    maximumHeapCapacity = 0
    currentHeapLastIndex = 0  # current last Index of the Heap based on the inserted City Objects, this is also the current Size of the Heap
    rawCityData: List[City]

    recursive: bool = False
    floyd: bool = False

    def __init__(self, raw_city_data: List[City], recursive: bool, floyd: bool):
        self.rawCityData = raw_city_data
        self.maximumHeapCapacity = len(self.rawCityData)  # set Maximum Heap Capacity to the amount of City Objects
        self.heapStorage = self.heapStorage * self.maximumHeapCapacity

        self.recursive = recursive
        self.floyd = floyd

        self.insert_raw_city_data_into_heap()

    # ----Abstract Methods Block (Methods necessary for both a min and a max heap but with different implementations)--

    @abstractmethod
    def heapify_up_iterative(self):
        """
        Establish heap conditions iterative upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_up_recursive(self, index):
        """
        Establish heap conditions recursive upwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_floyd(self, index, amount_of_cities):
        """
        Establish heap conditions via Floyds Heap Construction Algorithmus
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_iterative(self):
        """
        Establish heap conditions iterative downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def heapify_down_recursive(self, index):
        """
        Establish heap conditions recursive downwards.
        """
        ...
        raise NotImplementedError

    @abstractmethod
    def remove(self):
        """
        Remove a City from the Heap.
        """
        ...
        raise NotImplementedError

    # ------Shared Methods Block (Methods identical for both a min and a max heap)------

    def insert_raw_city_data_into_heap(self):
        # Add the new city to the end of the heap's list of cities
        self.insert(City)
        # Heapify the heap starting at the newly inserted city
        self.heapify_up_recursive(self.currentHeapLastIndex - 1)

        if self.floyd:
            self.build_heap_via_floyd()
        else:
            for i in self.rawCityData:
                self.insert(i)

    def insert(self, city):
        # Add the new city to the end of the heap
        self.heapStorage.append(city)

        # Call the heapify_up method to restore the heap property
        self.heapify_up_iterative()
        #self.heapStorage.sort()

        if self.recursive:
           self.heapify_up_recursive(self.currentHeapLastIndex - 1)
        else:
            self.heapify_up_iterative()

    def build_heap_via_floyd(self):
        """
        Build a Heap via Floyds Heap Construction Algorithm from an unsorted List Of Cities.
        """
        amount_of_cities = len(self.rawCityData)
        for i in range(amount_of_cities // 2, -1, -1):
            self.heapify_floyd(i, amount_of_cities)

    def get_root_city(self):
        if self.currentHeapLastIndex == 0:  # heap is empty, return None
            return None
        return self.heapStorage[0]

    def get_left_child_index(self, index):
        """
        Return the index of the left child.
        """
        return 2 * index + 1

    def get_right_child_index(self, index):
        """
        Return the index of the right child.
        """
        return 2 * index + 2

    def get_parent_index(self):
        """
        Return the index of the parent node.
        """
        if self == 0:  # root node has no parent, return None
            return None
        return (self - 1) // 2

    def has_parent(self, index) -> bool:
        # If the index is 0, the element is the root and has no parent
        if index == 0:
            return False

        # If the index is not 0, the element has a parent at index (index - 1) // 2
        return True

    def has_left_child(self, index):
        # The left child of an element at index i is located at index 2 * i + 1
        left_child_index = 2 * index + 1

        # If the left child index is within the bounds of the heap, the element has a left child
        return left_child_index < len(self.heapStorage)

    def has_right_child(self, index):
        # The right child of an element at index i is located at index 2 * i + 2
        right_child_index = 2 * index + 2

        # If the right child index is within the bounds of the heap, the element has a right child
        return right_child_index < len(self.heapStorage)

    def get_city_population(self, index):
        # Get the city object at the given index
        city = self.heapStorage[index]

        # Return the population of the city
        return city.population

    def get_parent_population(self, index):
        # Calculate the index of the parent element
        parent_index = (index - 1) // 2

        # Get the city object at the parent index
        parent = self.heapStorage[parent_index]

        # Return the population of the parent city
        return parent.population

    def get_left_child_population(self, index):
        # Calculate the index of the left child element
        left_child_index = 2 * index + 1

        # Get the city object at the left child index
        left_child = self.heapStorage[left_child_index]

        # Return the population of the left child city
        return left_child.population

    def get_right_child_population(self, index):
        # Calculate the index of the right child element
        right_child_index = 2 * index + 2

        # Get the city object at the right child index
        right_child = self.heapStorage[right_child_index]

        # Return the population of the right child city
        return right_child.population

    def check_if_heap_is_full(self):
        # Compare the number of elements in the heap to the maximum capacity
        return len(self.heapStorage) == self.maximumHeapCapacity

    def swap_nodes(self, fst_node_index, sec_node_index):
        # Swap the elements at the given indices
        self.heapStorage[fst_node_index], self.heapStorage[sec_node_index] = self.heapStorage[sec_node_index], \
            self.heapStorage[fst_node_index]

    def get_heap_data(self) -> List[City]:
        """
        Return the sorted List of City Objects

        return
        ------
        List[City]:
        """
        return self.heapStorage

