# print all subsets whose sum
# is equal to a given value
from itertools import combinations
from functools import reduce
from operator import __and__


def subsetSum(li, comb, sums):
    # Iterating through all subsets of
    # list li from length 0 to length of li:
    for i in range(len(li) + 1):
        for subset in combinations(li, i):
            # Storing all the subsets in list comb:
            comb.append(list(subset))

            # Storing the subset sums in list sums:
            sums.append(sum(subset))


def calcSubsets(n, arr, x):
    res = []
    # Dividing the list arr into two lists
    # arr1 and arr2 of about equal sizes
    # by slicing list arr about index n//2:
    arr1, arr2 = arr[:n // 2], arr[n // 2:]

    # Creating empty lists comb1 and sums1
    # to run the subsetSum function and
    # store subsets of arr1 in comb1
    # and the subset sums in sums1:
    comb1, sums1 = [], []
    subsetSum(arr1, comb1, sums1)

    # Creating empty lists comb2 and sums2
    # to run the subsetSum function and
    # store subsets of arr2 in comb2
    # and the subset sums in sums2:
    comb2, sums2 = [], []
    subsetSum(arr2, comb2, sums2)

    # Iterating i through the indices of sums1:
    for i in range(len(sums1)):

        # Iterating j through the indices of sums2:
        for j in range(len(sums2)):

            # If two elements (one from sums1
            # and one from sums2) add up to x,
            # the combined list of elements from
            # corresponding subsets at index i in comb1
            # and j in comb2 gives us the required answer:
            if sums1[i] + sums2[j] == x:
                res.append(set(comb1[i] + comb2[j]))

    # intersection of sets -> functional programming
    res = reduce(__and__, res)
    # entry std_out
    str_out2 = " ".join(map(str, res))
    with open("stdout", "w") as file_out:
        file_out.write(f'{len(res)}\n{str_out2}')


if __name__ == '__main__':
    # read std_in
    with open("stdin", "r") as file_in:
        lines = file_in.readlines()
    in1 = list(map(int, lines[0].split()))
    in2 = list(map(int, lines[1].split()))

    calcSubsets(in1[0], in2, in1[1])
