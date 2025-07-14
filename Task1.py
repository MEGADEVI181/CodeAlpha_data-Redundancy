def remove_duplicates(data_list):
    unique_data = []
    for item in data_list:
        if item not in unique_data:
            unique_data.append(item)
    return unique_data

old_data = ["apple", "banana", "apple", "orange", "banana"]
new_data = ["banana", "kiwi", "apple", "grape"]
combined_data = old_data + new_data
cleaned_data = remove_duplicates(combined_data)
print("Cleaned and Verified Data:", cleaned_data)
