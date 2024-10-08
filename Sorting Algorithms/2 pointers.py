def find_two_sum(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return arr[left], arr[right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None  # No pair found

arr = [1, 2, 3, 5, 8, 12]
target = 10
result = find_two_sum(arr, target)

if result:
    print(f"Pair found: {result}")
else:
    print("No pair found")
