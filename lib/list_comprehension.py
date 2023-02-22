#!/usr/bin/env python3

# Areeb Solution
def return_evens(num_list):
    list_evens = [i for i in num_list if (i % 2 == 0)]
    return list_evens

# Main Solution
# def return_evens(num_list):
#     return [n for n in num_list if n%2 == 0]
    




def make_exclamation(sentence_list):
    return [str + "!" for str in sentence_list]


# IT WORKS