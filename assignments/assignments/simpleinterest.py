# Question: Write a program in Python to compute Simple Interest.

def simple_interest(principal, rate, time):
    # Simple Interest formula: SI = (P * R * T) / 100
    interest = (principal * rate * time) / 100
    return interest

# Example usage:
principal = 1000
rate = 5
time = 2
interest = simple_interest(principal, rate, time)
print(f"Simple Interest: {interest}")
