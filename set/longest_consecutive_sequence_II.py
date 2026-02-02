"""
Now this can have any ASCII characters.
"""
def longest_repeating_substring(s: str) -> int:
    n = len(s)
    seen = {}  # Dictionary to store the last index of each substring
    max_len = 0
    start = 0  # The start of the sliding window

    # Iterate through the string
    for end in range(n):
        # If the character is already seen, move the start to avoid overlap
        if s[end] in seen and seen[s[end]] >= start:
            start = seen[s[end]] + 1
        
        # Update the position of the current character      
        seen[s[end]] = end
        
        # Calculate the current length of the substring
        max_len = max(max_len, end - start + 1)
    
    return max_len

# Test the function with the string "arvindaj"
s = "arvindaj"
result = longest_repeating_substring(s)
print(result)  # Output should be 7 (longest repeating substring is "rvindaj")
