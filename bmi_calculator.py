"""
Welcome to the Body Mass Index (BMI) Calculator project!

Your task is to implement a function called 'calculate_bmi' that takes
a person's weight in kilograms and height in meters as input, and
returns their BMI.

Here's the formula you'll need:
BMI = weight (kg) / (height (m) * height (m))

Let's break it down:
1.  **weight (kg):** This is the person's weight in kilograms.
2.  **height (m):** This is the person's height in meters.
3.  **height (m) * height (m):** This means height squared.

Your 'calculate_bmi' function should:
-   Accept two arguments: `weight_kg` (a float or int) and `height_m` (a float or int).
-   Return the calculated BMI as a float.
-   Consider edge cases: What if height is zero or negative? How should your function handle that?
    (Hint: You might want to return a specific value or raise an error for invalid inputs.)

Good luck!
"""

# --------------------------------------------------------------------------
# STUDENT'S TASK: Implement the calculate_bmi function below.
# DO NOT CHANGE the function signature (name and parameters).
# --------------------------------------------------------------------------

def calculate_bmi(weight_kg, height_m):
    """
    Calculates the Body Mass Index (BMI).

    Args:
        weight_kg (float or int): The person's weight in kilograms.
        height_m (float or int): The person's height in meters.

    Returns:
        float: The calculated BMI.
        (You might also consider returning None or raising an error for invalid inputs).
    """
    # Your code goes here!
    # Example placeholder:
    # if height_m <= 0:
    #     return None # Or raise ValueError("Height cannot be zero or negative.")
    # bmi = weight_kg / (height_m ** 2)
    # return bmi
    pass # Remove this line when you start implementing

# --------------------------------------------------------------------------
# You can add example usage here to test your function manually (optional)
# if __name__ == "__main__":
#     print("BMI for 70kg, 1.75m:", calculate_bmi(70, 1.75))
#     print("BMI for 0kg, 1.75m:", calculate_bmi(0, 1.75))
#     print("BMI for 70kg, 0m:", calculate_bmi(70, 0))
# --------------------------------------------------------------------------