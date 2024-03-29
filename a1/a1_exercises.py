import math


def is_a_triple(n):
    return n%3 == 0


def last_prime(m):
    """Return the largest prime number p that is less than or equal to m.
    You might wish to define a helper function for this.
    You may assume m is a positive integer."""
    def is_prime(m):
        if m==3: return True
        if m%2==0 or m<2: return False
        for i in range(3, int(m**0.5)+1, 2):
            if m%i==0:
                return False    
        return True
    
    #edge case
    if m == 2:
        return 2 
    if m%2==0:
        m -= 1

    for i in range(m, 1, -2):
        if is_prime(i):
            return i


def quadratic_roots(a, b, c):
    """Return the roots of a quadratic equation (real cases only).
    Return results in tuple-of-floats form, e.g., (-7.0, 3.0)
    Return "complex" if real roots do not exist."""
    d = (b**2) - (4*a*c)
    if d < 0:
        return "complex"
    else:
        return ((-b-math.sqrt(d))/(2*a), (-b+math.sqrt(d))/(2*a))


def new_quadratic_function(a, b, c):
    """Create and return a new, anonymous function (for example
    using a lambda expression) that takes one argument x and 
    returns the value of ax^2 + bx + c."""
    return lambda x: a*x**2 + b*x + c


def perfect_shuffle(even_list):
    """Assume even_list is a list of an even number of elements.
    Return a new list that is the perfect-shuffle of the input.
    Perfect shuffle means splitting a list into two halves and then interleaving
    them. For example, the perfect shuffle of [0, 1, 2, 3, 4, 5, 6, 7] is
    [0, 4, 1, 5, 2, 6, 3, 7]."""
    new = []
    mid = int(len(even_list)/2)
    for i in range(mid):
        new.append(even_list[i])
        new.append(even_list[i+mid])
    return new

def list_of_3_times_elts_plus_1(input_list):
    """Assume a list of numbers is input. Using a list comprehension,
    return a new list in which each input element has been multiplied
    by 3 and had 1 added to it."""
    return [num * 3 + 1 for num in input_list]

def triple_vowels(text):
    """Return a new version of text, with all the vowels tripled.
    For example:  "The *BIG BAD* wolf!" => "Theee "BIIIG BAAAD* wooolf!".
    For this exercise assume the vowels are
    the characters A,E,I,O, and U (and a,e,i,o, and u).
    Maintain the case of the characters."""
    chars = 'aAeEiIoOuU'
    return ''.join([char * 3 if char in chars else char for char in text])

def count_words(text):
    """Return a dictionary having the words in the text as keys,
    and the numbers of occurrences of the words as values.
    Assume a word is a substring of letters and digits and the characters
    '-', '+', *', '/', '@', '#', '%', and "'" separated by whitespace,
    newlines, and/or punctuation (characters like . , ; ! ? & ( ) [ ] { } | : ).
    Convert all the letters to lower-case before the counting."""

    white_space = """.,;!?$&()[]{}"|:^<>`\_=~"""

    for c in white_space:
        text = text.replace(c, ' ')

    counts = {}
    words = text.lower().split()
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts

