# Algorithms and solutions for coding interview questions

After earning my Msc in Mathematics, I started working on practical things. 
So I never had time to try solving these algorithms questions that you are expected to know on 
coding interviews in software companies.
I finally wanted to set aside some time to recall how to think about simple algorithms.
I was thinking If I should solve this problems in python or javascript because I am fluent in both of them.
But choose python.


### Methodology
Every solution is another function in `Solution` class.
When starting to solve problem, goal is to solve it fast and dirty at first iteration and this will
be functions that starts with `simple_` keyword.
After the solution is correct, I should iterate more to find better or different implementation. This will force me 
to think more about problem and to obtain better understanding.

### Automatic stats generation in README
At first, I started manually inserting each solved problems in README, but it was cumbersome and unpractical.
Then I figured that I could write some script that would to that for me and this script could be run with `Github actions`
every time I make new commit with new solution.
To solve this,I needed to put some metadata for every solution and
best approach would be to put it somewhere in file, so that file represent a problem and possible solution.
I used python doc strings and put all the relevant metadata at the beginning of each file.
This needed to be in format that script would know how to parse. I choose yaml and after string is extracted,
parsing is done with help of [grey-matter](https://github.com/jonschlinkert/gray-matter).
The script is done in Typescript and `Solution` interface looks like this in yaml at the beginning of each file.
```angular2html
---
title: Roman to integer
number: 13
difficulty: easy
tags: ['Hash table','Math','String']
url: https://leetcode.com/problems/roman-to-integer/
solved: true
---
```

When you ran script, it scans for files in folders and subfolders, and parses and collects this metadata.
It then processes this solution list for all relevant statistics, tags and other info. 
We then take content from `intro.md`, and strings we created from this solution statistics and write this in 
official `README.md` file.
This script is located at `./src/run.ts`, and this is corresponding Github action configuration.
It also makes new commit because `README` file is changed.
```yaml
name: write-stats
run-name: Writing stats in README
on: ['push']
jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          ref: ${{github.head_ref}}
      - uses: actions/setup-node@v3
        with:
          node-version: '14'
      - run: yarn
      - run: yarn start
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: Automatic commit - write stats to README
```




### Problems solved

:white_circle: Easy: 12

:large_blue_circle: Medium: 11

:red_circle: Hard: 1

__Total__: 24

### Solutions

1. :large_blue_circle: [Container With Most Master](./leetCode/11_container_with_most_water.py)
2. :white_circle: [Best Time To Buy And Sell Stock](./leetCode/121_best_time_to_buy_and_sell_stock.py)
3. :large_blue_circle: [Integer To Roman](./leetCode/12_integer_to_roman.py)
4. :white_circle: [Single Number](./leetCode/136_single_number.py)
5. :white_circle: [Roman To Integer](./leetCode/13_roman_to_integer.py)
6. :large_blue_circle: [Two Sum II - Input Array Is Sorted](./leetCode/167_two_sum_ii.py)
7. :white_circle: [Majority Element](./leetCode/169_majority_element.py)
8. :white_circle: [Two Sum](./leetCode/1_two_sum.py)
9. :white_circle: [Valid Parentheses](./leetCode/20_valid_parentheses.py)
10. :white_circle: [Merge Two Sorted Lists](./leetCode/21_merge_two_sorted_lists.py)
11. :white_circle: [Remove Duplicates From Sorted Array](./leetCode/26_remove_duplicates_sorted_array.py)
12. :large_blue_circle: [Add Two Numbers](./leetCode/2_add_two_numbers.py)
13. :white_circle: [Search Insert Position](./leetCode/35_search_insert_position.py)
14. :large_blue_circle: [Longest Substring Without Repeating Characters](./leetCode/3_longest_substring_without_repeating_characters.py)
15. :large_blue_circle: [Rotate Image](./leetCode/48_rotate_image.py)
16. :large_blue_circle: [Maximum Subarray](./leetCode/53_maximum_subarray.py)
17. :large_blue_circle: [Spiral Matrix](./leetCode/54_spiral_matrix.py)
18. :large_blue_circle: [Longest Palindromic Substring](./leetCode/5_longest_palindromic_substring.py)
19. :large_blue_circle: [Search A 2D Matrix](./leetCode/74_search_2d_matrix.py)
20. :white_circle: [Palindrome Number](./leetCode/9_palindrome_number.py)
21. :large_blue_circle: [Sort List](./leetCode/linked-list/148_sort_list.py)
22. :white_circle: [Palindrome Linked List](./leetCode/linked-list/234_palindrome_linked_list.py)
23. :red_circle: [Merge K Sorted Lists](./leetCode/linked-list/23_merge_k_sorted_lists.py)
24. :white_circle: [Middle Of The Linked List](./leetCode/linked-list/876_middle_of_the_linked_list.py)

### Tags by count

1. **Array**: 12
2. **Two Pointers**: 6
3. **Linked List**: 6
4. **Hash Table**: 5
5. **Math**: 5
6. **String**: 5
7. **Dynamic Programming**: 3
8. **Binary Search**: 3
9. **Divide And Conquer**: 3
10. **Recursion**: 3
11. **Matrix**: 3
12. **Sorting**: 2
13. **Stack**: 2
14. **Merge Sort**: 2
15. **Greedy**: 1
16. **Bit Manipulation**: 1
17. **Counting**: 1
18. **Sliding Window**: 1
19. **Simulation**: 1
20. **Divider And Conquer**: 1
21. **Heap (Priority Queue)**: 1
