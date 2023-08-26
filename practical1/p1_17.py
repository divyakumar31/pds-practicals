"""
Author: PATEL DIVYAKUMAR BHARATBHAI
Date: 21/08/2023
Practical 1.17: Write a program to create a dictionary from string in which individual character is key and its count in string is value of key.  
"""

def main():
    sentence = input("Enter the string: ")
    dict_sentence = string_to_dict(sentence)
    for key_pair in dict_sentence.items():
        print(f"{key_pair[0]} repeat {key_pair[1]} times.")
        


def string_to_dict(s: str) -> dict:
    dict_sentence = {}

    for i in s:
        if i not in dict_sentence.keys():
            dict_sentence[i] = s.count(i)

    return dict_sentence


if __name__ == "__main__":
    main()