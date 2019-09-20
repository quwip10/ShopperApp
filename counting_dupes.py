def duplicate_count(text):
    dupe_count = 0
    
    for num, letter in enumerate(text.lower()):
        if text.count(letter) > 1 and text.find(letter) == num:
            dupe_count += 1
        
    return dupe_count

print(duplicate_count(input()))