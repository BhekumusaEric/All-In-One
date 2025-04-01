# Question 1
def get_date_of_birth(id_number: str) -> str:
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    return format: DD/MM/YY:
    """
    id_num = list(id_number)
    return f"{''.join(id_num[4:6])}/{''.join(id_num[2:4])}/{''.join(id_num[0:2])}"

# Question 2
def get_gender(id_number: str) -> str:
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    id_num = list(id_number)
    if int("".join(id_num[6:10])) > 4999:
        return "Male"
    elif int("".join(id_num[6:10])) < 5000:
        return "Female"
# Question 3
def fizzbuzz(number):
    """
    Fizzbuzz is a programme that prints the numbers from 1 to n, 
    but for multiples of 3, it prints "Fizz" instead of the number, 
    and for multiples of 5, it prints "Buzz" instead of the number. 
    For numbers that are multiples of both 3 and 5, it prints "FizzBuzz.

    TODO: define a function called fizzbuzz and implement the fucntionality above.
    """
    for i in range(1 , number + 1):
        if i % 5 == 0 and i % 3 ==0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
# Question 4
def find_even_numbers(numbers):
    """Find the even numbers in the list 'numbers' and return them in
    in a tuple

    Hint: use modulus (%)"""
    even = [i for i in numbers if i % 2 == 0]
    return tuple(even)

# Question 5
def find_odd_numbers(numbers):
    """Find the odd numbers in the list 'numbers' and return them in
    in a tuple

    Hint: use modulus (%)"""
    odd= [i for i in numbers if i % 2 != 0]
    return tuple(odd)

# Question 6
def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
    dictionary of statics for the list. This dictionary must have
    the following keys:
        unique_numbers : a set containing unique numbers from the list 'numbers',
        max : largest number in the list 'numbers',
        min : smallest number in the list 'numbers',
        average : average of the numbers in the list 'numbers',
        even_numbers : a tuple of all the even numbers in the list
            'numbers',
        odd_numbers : a tuple of all the odd numbers in the list
            'numbers',
        number_of_even_numbers : the total number of even numbers in the
            list 'numbers',
        number_of_odd_numbers : the total number of even numbers in the list
             'numbers'
    """
    dict_numbers = {}
    dict_numbers['unique_numbers'] = set(numbers)
    dict_numbers['max'] = max(numbers)
    dict_numbers['min'] = min(numbers)
    dict_numbers['average'] = sum(numbers) / len(numbers)
    dict_numbers['even_numbers'] = find_even_numbers(numbers)
    dict_numbers['odd_numbers'] = find_odd_numbers(numbers)
    dict_numbers['number_of_even_numbers'] = len(find_even_numbers(numbers))
    dict_numbers['number_of_odd_numbers'] = len(find_odd_numbers(numbers))  
    return dict_numbers

# Question 7
def draw_triangle_reversed(height: int) -> None:
    """
    Draw an inverted number triangle where each row begins with its position number,
    with the top row having the most repeated numbers and each row below having one fewer repetition.

    Parameters:
        height (int): The height of the triangle. Must be a positive integer.

    Returns:
        None: Prints the inverted triangle pattern directly to console.

    """
    for i in range(1 , height + 1):
        print(" ".join([str(i)] * (height - (i - 1))) , "" , end = "\n")  # print the triangle with the specified height

# Question 8
def draw_triangle_prime(height: int) -> None:
    """
    Draws a triangle of prime numbers where each row contains the first n primes
    that fit the row width.

    Parameters:
        height (int): The height of the triangle. Must be a positive integer.

    Returns:
        None: Prints the prime number triangle pattern directly to console.

    """
    for i in range(1 , height ):
        row = []
        num = 2
        while len(row) < i + 1:
            if is_prime(num):
                row.append(num)
                num += 1
            else:
                num += 1
            print(" ".join(map(str, row)))  # print the triangle with the specified height

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
        return True
# Question 9
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    pass
