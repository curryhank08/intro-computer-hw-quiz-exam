""" 
author: H24111057 姚博瀚
"""

class Solution:
    # Find n-th fibonacci sequence number by recursion.
    def fibonacci(self, n:int) -> int:
        x0 = 0
        x1 = 1
        if n == 0:
            return x0
        elif n == 1:
            return x1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str, Max_Len
    
    # k is from the Fibonacci(n); a, b are the length of LPS for s1, s2. 
    def encryption(self, string, k, a, b):
        characters = list(string[i] for i in range(len(string)))
        x = list(ord(string[i]) for i in range(len(string)))
        
        ''' encrypted only by one method (caesar or affine)
        ## encryption by Caesar Cipher
        # encryption result in ASCII code 
        y_caesar = list(x[i]+k for i in range(len(x)))
        # transform into range of A(65)~Z(90) 
        y_caesar_further = list(((y_caesar[i] - 65) % 26) + 65 for i in range(len(y_caesar)))

        ## encryption by Affine Cipher 
        # encryption result in ASCII code 
        y_affine = list(a * x[i] + b for i in range(len(x)))
        # transform into range of A(65)~Z(90) 
        y_affine_further = list(((y_affine[i] - 65) % 26) + 65 for i in range(len(y_affine)))

        ## Retrieve corresponding characters from ASCII code
        y_caesar_characters = list(chr(y_caesar[i]) for i in range(len(y_caesar)))
        y_affine_characters = list(chr(y_affine[i]) for i in range(len(y_affine)))

        y_caesar_further_characters = list(chr(y_caesar_further[i]) for i in range(len(y_caesar_further)))
        y_affine_further_characters = list(chr(y_affine_further[i]) for i in range(len(y_affine_further)))

        # Combine characters in list into a string which is the encrypted text
        entrypted_text_by_caeser = ''.join(y_caesar_characters)
        entrypted_text_by_affine = ''.join(y_affine_characters)
        
        entrypted_text_by_caeser_further = ''.join(y_caesar_further_characters)
        entrypted_text_by_affine_further = ''.join(y_affine_further_characters)
        
        return entrypted_text_by_caeser, entrypted_text_by_affine, entrypted_text_by_caeser_further, entrypted_text_by_affine_further
        '''
        ### 2-stage encryption (Caesar first then Affine)
        # first: caesar
        y_caesar = list(x[i]+k for i in range(len(x)))
        # second: Affine
        y_affine = list(a * y_caesar[i] + b for i in range(len(x)))
        # transform into range of A(65)~Z(90) 
        y_affine_further = list(((y_affine[i] - 65) % 26) + 65 for i in range(len(y_affine)))
        # Retrieve corresponding characters from ASCII code
        y_affine_further_characters = list(chr(y_affine_further[i]) for i in range(len(y_affine_further)))
        # Combine characters in list into a string which is the encrypted text
        entrypted_text_by_two_stage = ''.join(y_affine_further_characters)
        
        return entrypted_text_by_two_stage

    def main(self):
        n_fibonacci = int(input("The number 'n' of the requested element in Fibonacci (n) ="))
        s1_palindromic = input("The first string for Palindromic detection (s1) =")
        s2_palindromic = input("The second string for Palindromic detection (s2) =")
        plaintext = input("The plaintext to be encrypted:")
        
        print("----- extract key for encrypt method -----")
        
        fibonacci_n_result = self.fibonacci(n_fibonacci)
        print(f"The {n_fibonacci}-th Fibonacci sequence number is {fibonacci_n_result}")
        
        LPS_length_s1 = self.longestPalindrome(s=s1_palindromic)
        LPS_length_s2 = self.longestPalindrome(s=s2_palindromic)
        
        print(f"Longest palindrome substring within first string is: {LPS_length_s1[0]}")
        print(f"Length is: {LPS_length_s1[1]}")
        
        print(f"Longest palindrome substring within second string is: {LPS_length_s2[0]}")
        print(f"Length is: {LPS_length_s2[1]}")
        
        print("----- encryption completed -----")
        
        ''' encrypted only by one method (caesar or affine)
        encrypted_by_caesar, encrypted_by_affine, encrypted_by_caesar_further, encrypted_by_affine_further = self.encryption(string=plaintext,
                                                                                                                             k=fibonacci_n_result,
                                                                                                                             a=LPS_length_s1[1],
                                                                                                                             b=LPS_length_s2[1])

        print(f"The encrypted text by Caesar Cipher is: {encrypted_by_caesar}, {encrypted_by_caesar_further}\n"
              f"The encrypted text by Affine Cipher is: {encrypted_by_affine}, {encrypted_by_affine_further}")
        '''
        two_stage_encrypted_text = self.encryption(string=plaintext,
                                                   k=fibonacci_n_result,
                                                   a=LPS_length_s1[1],
                                                   b=LPS_length_s2[1])
        print(f"The encrypted text is: {two_stage_encrypted_text}")

# Instance of the Solution class and run main()
solution_instance = Solution()
solution_instance.main()