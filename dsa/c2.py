def median_followers(nums):
    sorted_nums = sorted(nums) 
    median = 0
    seq_med = len(nums) // 2

    if len(nums) == 0:
        return None
    elif len(nums) % 2 == 0:
        median += (sorted_nums[seq_med-1] + sorted_nums[seq_med]) / 2
    else:
        median += sorted_nums[seq_med]

    return median