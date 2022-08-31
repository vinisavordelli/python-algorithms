def find_duplicate(nums):
    scanned_nums = []
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in scanned_nums:
            return num
        scanned_nums.append(num)
    return False
