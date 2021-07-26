'''Implement the following algorithm:
Sort(A):
    for j = 2 to A.length:
        i = j-1
        key = A[j]
        while i>0 and key<A[i]:
            a[i+1] = a[i]
            i = i-1
        A[j] = key
'''


class PavanSorting  ():
    '''This class has several sorting methods. All of them have the same API structure:
        sort_name(nums, showsteps) where nums is a list of numbers only
        '''
    @staticmethod
    def insertion_sort( numbers, showsteps = False):
        '''
            Nums is a list of numbers. Accepts lists only. 1-d only
            Show steps = False, to see the result of every step, helpful in understanding various algorithms
        '''
        try:
            nums = numbers[:] #This makes a separate copy of the numbers, don't want to mess with the original. Pure function
            if not isinstance(nums, Iterable): #Check if they send a single value, reject it
                raise Exception
            else:
                for j in range(1, len(nums)):
                    i=j-1
                    key = nums[j]
                    while i > -1 and key < nums[i]:
                        nums[i+1] = nums[i]
                        i = i-1
                    nums[i+1] = key
                    if showsteps:
                        print(nums)
                return (nums)


        except Exception:
            print("A non iterable or immutable iterable passed")

import sys
if __name__ == "__main__":
    num = (int(arg) for arg in sys.argv[1:])
    algo = PavanAlgorithms()
    algo.insertion_sort(nums=num, showsteps=False)
    print(num) #All mutable objects are passed by reference
