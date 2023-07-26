import unittest

# Time Complexity: O(N), Space Complexity: O(N)
def missing_int(input_file):
    num_bits = 4_000_000_000
    bit_vector = 1<< num_bits
    for num in input_file:
        bit_vector = bit_vector| 1<<num

    for i in range(num_bits):
        if not bit_vector & 1<<i:
            return i

def get_missing_int(arr):
    n = len(arr) - 1
    total = (n + 1)*(n + 2)/2
    sum_of_arr = sum(arr)
    return total - sum_of_arr


# INT_MAX = 2**31 - 1
# bitfield = [0] * INT_MAX // 8
# If using proper byte array, bitfield can store up 8 billion bits with 1 GB
# of memory. For Python array purposes, we will test with only 512 elements


def find_missing_int(arr):
    bitfield = [0] * 512
    #file = open(filename, "r")
    for line in arr:
        n = int(line)
        # Finds the corresponding number in the bitfield by using the OR
        # operator to set the nth bit of a byte (e.g., 10 would correspond
        # to the 2nd bit of index 2 in the byte array).
        bitfield[n // 8] |= 1 << (n % 8)
    for i in range(len(bitfield)):
        for j in range(8):
            # Retrieves the individual bits of each byte. When 0 bit is found,
            # print the corresponding value.
            if bitfield[i] & (1 << j) == 0:
               return i * 8 + j

class Test(unittest.TestCase):
    test_cases = [
        ([0,1,2,3,4,5,6,7,8,9,10,12], 11)
    ]
    functions = [missing_int, get_missing_int, find_missing_int]
    def test_missing_int(self):
        for function in self.functions:
            for input_file, expected in self.test_cases:
                result = function(input_file)
                assert result == expected

if __name__ == '__main__':
    unittest.main()