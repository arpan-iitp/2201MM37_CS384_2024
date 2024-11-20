def find_unique_triplets(nums):
    nums.sort()  # Sort the array to help avoid duplicates
    triplets = []

    for i in range(len(nums)):
        # Avoid duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])

                # Avoid duplicates for the second and third elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets

# Take input from the user
input_string = input("Enter the array of integers (space-separated): ")
nums = list(map(int, input_string.split()))

# Find and display unique triplets
result = find_unique_triplets(nums)
print("Unique triplets that sum to zero:", result)
