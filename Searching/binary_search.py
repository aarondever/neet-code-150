def binarySearch(arr: list[int], target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
