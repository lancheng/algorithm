# encoding: utf-8
# *********************************************************************************************************************** quick_sort.py
"""quick_sort.py
"""


# ***********************************************************************************************************************

# ======================================================================================================================= Imports

# ======================================================================================================================= Static
# numbers = [5, 10, 29, 4, 198, 34, 2]


# ======================================================================================================================= Classes

# ======================================================================================================================= Functions
class QuickSort:
    def __int__(self):
        pass

    @staticmethod
    def _get_pivot(start_pos, end_pos, num_list):
        return num_list[end_pos], end_pos

    @staticmethod
    def _sort(start_pos, end_pos, num_list):
        if start_pos > end_pos:
            return

        pivot, pivot_pos = QuickSort._get_pivot(start_pos, end_pos, num_list)
        num_list[pivot_pos], num_list[end_pos] = num_list[end_pos], num_list[pivot_pos]
        pivot_pos = start_pos

        for i in range(start_pos, end_pos):
            if num_list[i] < pivot:
                num_list[i], num_list[pivot_pos] = num_list[pivot_pos], num_list[i]
                pivot_pos += 1

        num_list[pivot_pos], num_list[end_pos] = num_list[end_pos], num_list[pivot_pos]

        # sort left
        QuickSort._sort(start_pos, pivot_pos - 1, num_list)

        # sort right
        QuickSort._sort(pivot_pos + 1, end_pos, num_list)

        return

    @staticmethod
    def sort(numbers):
        if len(numbers) <= 1:
            return

        QuickSort._sort(0, len(numbers) - 1, numbers)


# ***********************************************************************************************************************

if __name__ == '__main__':
    numbers = [5, 10, 29, 4, 198, 34, 2]

    import sys, ast
    if len(sys.argv) == 2 and isinstance(ast.literal_eval(sys.argv[1]), list):
        numbers = ast.literal_eval(sys.argv[1])

    quick_sort = QuickSort()
    quick_sort.sort(numbers)

    print numbers
# ***********************************************************************************************************************
