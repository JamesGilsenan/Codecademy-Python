from Deque import Deque
import math

class Palindrome:

    def get_input(self):
        deque = Deque()
        pallindrome_str = ""
        while pallindrome_str == "":
            pallindrome_str = input("PLease input a palindrome: ")
            for letter in pallindrome_str:
                deque.add_front(letter)
        print(deque)
        return deque

    def check_palindrome(self, palindrome):
        #racecar
        while palindrome.size() > 0:
            if palindrome.peek_front() == palindrome.peek_rear() and palindrome.size() > 1:
                print("Removing first and last letter")
                palindrome.remove_front()
                palindrome.remove_rear()
            elif palindrome.peek_front() == palindrome.peek_rear():
                return True
            else:
                return False
            print(palindrome)
        return True

palindrome = Palindrome()
user_input = palindrome.get_input()
print(palindrome.check_palindrome(user_input))
