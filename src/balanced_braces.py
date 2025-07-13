"""
Check if braces are properly matched in a string containing only '{' and '}' braces.
"""

def check_balanced_braces(s):
    balance = 0
    
    for char in s:
        if char == '{':
            balance += 1
        elif char == '}':
            balance -= 1
            if balance < 0:  # More closing braces than opening
                return "Not Matching"
    
    return "Matching" if balance == 0 else "Not Matching"

if __name__ == "__main__":
    n = input()
    print(check_balanced_braces(n))