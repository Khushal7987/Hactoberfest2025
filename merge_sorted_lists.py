def merge_sorted_lists(list1, list2):
    i = j = 0 # Pointers for list1 and list2
    merged_list = []
    
    # Compare elements from both lists and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
            
    # Append the remaining elements from whichever list is left
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    
    return merged_list

# --- Example Usage ---
L1 = [1, 5, 8]
L2 = [2, 6, 9, 10]
M = merge_sorted_lists(L1, L2)
print(f"Merged Result: {M}") # Output: [1, 2, 5, 6, 8, 9, 10]
