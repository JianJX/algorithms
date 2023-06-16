#Determining DNA Health
###Unsolved, need Aho Corasick algorithm
'''
DNA is a nucleic acid present in the bodies of living things. Each piece of
DNA contains a number of genes, some of which are beneficial and increase
the DNA's total health. Each gene has a health value, and the total health
of a DNA is the sum of the health values of all the beneficial genes that
occur as a substring in the DNA. We represent genes and DNA as non-empty
strings of lowercase English alphabetic letters, and the same gene may
appear multiple times as a susbtring of a DNA.
'''

import math
import os
import random
import re
import sys

def get_health(d, g, h):
    total = 0
    gh_map = { }
    for i in range(len(g)):
        if g[i] not in gh_map:
            gh_map[g[i]] = h[i]
        else:
            gh_map[g[i]] += h[i]
    sub_strs = [ ]
    for i in range(1, len(d) + 1): #0 1 2 3 4
        index = 0
        while index < len(d) - i + 1: #5 4 3 2 1
            sub_str = d[index:index + i]
            sub_strs.append(sub_str)
            index += 1
    for s in sub_strs:
         if s in g:
            total += gh_map[s]
    return total

if __name__ == '__main__':
    n = int(input().strip())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))

    s = int(input().strip())
    h_list = [ ]
    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        first = int(first_multiple_input[0])

        last = int(first_multiple_input[1])

        d = first_multiple_input[2]
        g = genes[first:last + 1]
        h = health[first:last + 1]
        result = get_health(d, g, h)
        h_list.append(result)
    print(min(h_list), max(h_list))