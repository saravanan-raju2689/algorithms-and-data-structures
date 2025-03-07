def pair_sum(arr, target):
    seen = set()
    for number in arr:
        complement = target - number
        if complement in seen:
            return True
        seen.add(number)
    return False