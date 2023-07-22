import unittest

#binary search
#Time Complexity: O(N) impossible for less than O(N) in worst case, Space Complexity: O(1)
def sparse_search_recursive(arr, low_index, high_index, target):
    if low_index > high_index: return None

    middle_index = (low_index + high_index) // 2

    if arr[middle_index] == "":
        middle_low_index = middle_index - 1
        middle_high_index = middle_index + 1
        while True:
            #check if indices are within the range
            if middle_low_index < low_index and middle_high_index > high_index:
                return None
            # Trying to get one references
            if middle_low_index >= low_index and arr[middle_low_index] != "":
                middle_index = middle_low_index
                break
            elif middle_high_index<= high_index and arr[middle_high_index] != "":
                middle_index = middle_high_index
                break
            # increase and decrease value to search by one reference
            middle_low_index -= 1
            middle_high_index += 1

    if arr[middle_index] == target:
        return middle_index
    elif arr[middle_index] > target:
        return sparse_search_recursive(arr,low_index, middle_index - 1, target)
    else:
        return sparse_search_recursive(arr, middle_index + 1, high_index, target)

def sparse_search(arr, low_index, high_index, target):
    while low_index < high_index:
        middle_index = (low_index + high_index) // 2

        if arr[middle_index] == "":

            middle_low_index = middle_index - 1
            middle_high_index = middle_index + 1

            while True:
                if middle_low_index < low_index and middle_high_index > high_index:
                    return None
                if middle_low_index >= low_index and arr[middle_low_index] != "":
                    middle_index = middle_low_index
                    break
                elif middle_high_index<= high_index and arr[middle_high_index] != "":
                    middle_index = middle_high_index
                    break

                middle_low_index -= 1
                middle_high_index += 1

        if arr[middle_index] == target:
            return middle_index
        elif arr[middle_index] > target:
            high_index = middle_high_index - 1
        else:
            low_index = middle_low_index + 1
    return None

class Test(unittest.TestCase):
    test_cases = [
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball", 4)
    ]
    functions = [sparse_search_recursive, sparse_search]
    def test_sorted_search_no_size(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, 0 , len(arr) - 1, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()