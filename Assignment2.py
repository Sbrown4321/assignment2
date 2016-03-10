#Steven Brown
#Assignment 2
#21FEB2016
import unittest

"""A palindrome is a word or sentence that is spelled the same forwards as backwards.
To detect whether a word or sentence is a palindrome, create two stand-alone (non-class) recursive methods.
The first should take a string and return a string with all the spaces removed.
The second should take a string and return True if it is a palindrome, False if not."""

# Recursive function to remove all spaces from a given string
def remove_spaces(s):
    while s != None:
        if s == "": return s
    #if s is None: return s
    if len(s) <= 1: return s

    if s[0] != " ":
        #return s.replace(" ","")
        return s[0] + remove_spaces(s[1:])
    else:
        return remove_spaces(s[1:])
# Recursive function to check if palindrome
def palindrome(s):
    #if s < 0: raise ValueError("Less than zero")
    while s != None:
        if s == "": return
    #if s == None: return
    #result to compare the two strings
    result = type(s)()
    if result == s: return s
    else:
        result != s

    result += palindrome(s[1:]) + s[:0]
    return (s)

#def palindrome(s):
    #if s =="": return ""
    #restrev = palindrome(s[1:])
    #first = s[0:1]
    #put the pieces together
    #result = restrev + first
    #if result == s:
        #return True
    #else:
        #return False


class test_remove_spaces (unittest.TestCase):
    def test_remove_space_none(self):
        self.assertEquals (remove_spaces (None), None)
    def test_remove_space_empty(self):
        self.assertEquals (remove_spaces (""), "")
    def test_remove_space_one(self):
        self.assertEquals (remove_spaces (" "), "")
    def test_remove_space_two(self):
        self.assertEquals (remove_spaces ("  "), "")
    def test_remove_space_inside(self):
        self.assertEquals (remove_spaces ("a b c"), "abc")
    def test_remove_space_before(self):
        self.assertEquals (remove_spaces (" a b c"), "abc")
    def test_remove_space_after(self):
        self.assertEquals (remove_spaces ("a b c "), "abc")
    def test_remove_space_before_and_after(self):
        self.assertEquals (remove_spaces (" a b c "), "abc")

    # this is extra credit
    # def test_raise_typerror(self):
        # self.assertRaises (TypeError, lambda: remove_spaces (1))

class test_palindrome (unittest.TestCase):
    def test_none(self):
        self.assertFalse (palindrome (None))
    def test_empty(self):
        self.assertTrue (palindrome (""))
    def test_one_letter(self):
        self.assertTrue (palindrome ("v"))
    def test_two_letters(self):
        self.assertTrue (palindrome ("vv"))
    def test_toyota(self):
        self.assertTrue (palindrome ("atoyota"))
    def test_toyota_with_spaces(self):
        self.assertTrue (palindrome (remove_spaces ("a toyota")))
    def test_odd_even(self):
        self.assertTrue (palindrome (remove_spaces ("never odd or even")))
    def test_rat(self):
        self.assertTrue (palindrome (remove_spaces ("Was It a Rat I saW")))
    def test_not(self):
        self.assertFalse (palindrome (remove_spaces ("i'm not a palindrome")))

if __name__ == '__main__':
    unittest.main()