# Algorithms and solutions for coding interview questions

After earning my MSc in Mathematics, I started working on practical things. So I never had time to look at these algorithms questions that you are expected to know on coding interviews in software companies.
I finally wanted to set aside some time to recall how to think about simple algorithms. I choose python as my language of choice.

### Methodology
Every solution is another function in `Solution` class.
When starting to solve problems, the goal is to solve them fast and dirty at the first iteration, and these will be functions that start with `simple_` keyword.
After validating the solution, I should iterate more to find a better or different implementation. This will force me 
to think more about problem and to obtain a better understanding.


### Automatic stats generation in README
At first, I started manually inserting each solved problem in README, but it was cumbersome and impractical.
Then I figured that I could write some script that would do, and this script would be run with `Github actions` every time I make a commit with new solution.
To solve this, I needed to put some metadata for every solution and
best approach is to add it in file so that file represents a problem and possible solution.
I used python doc strings and put all the relevant metadata at the beginning of each file.
This needed to be in a format that script would know how to parse. I choose YAML and after a string is extracted,
parsing is done with the help of [grey-matter](https://github.com/jonschlinkert/gray-matter).
The script is done in Typescript and `Solution` interface is defined like this.


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

When you run the script, it scans for files in folders and subfolders, parses and collects the solution's metadata. It then processes this solution list for all relevant statistics, tags, and other info. 
We then take content from `intro.md`, and strings we created from this solution statistics and write this in 
the official `README.md` file.
This script is located at `./src/run.ts`, and this is the corresponding Github action configuration.
It also makes new commit because `README` file is changed.
.
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

:white_circle: Easy: 13

:large_blue_circle: Medium: 13

:red_circle: Hard: 2

__Total__: 28

### Solutions

1. :large_blue_circle: [Container With Most Master](./leetCode/11_container_with_most_water.py)
2. :white_circle: [Best Time To Buy And Sell Stock](./leetCode/121_best_time_to_buy_and_sell_stock.py)
3. :large_blue_circle: [Integer To Roman](./leetCode/12_integer_to_roman.py)
4. :white_circle: [Single Number](./leetCode/136_single_number.py)
5. :white_circle: [Roman To Integer](./leetCode/13_roman_to_integer.py)
6. :white_circle: [Longest Common Prefix](./leetCode/14_longest_common_predix.py)
7. :large_blue_circle: [Two Sum II - Input Array Is Sorted](./leetCode/167_two_sum_ii.py)
8. :white_circle: [Majority Element](./leetCode/169_majority_element.py)
9. :white_circle: [Two Sum](./leetCode/1_two_sum.py)
10. :white_circle: [Valid Parentheses](./leetCode/20_valid_parentheses.py)
11. :white_circle: [Merge Two Sorted Lists](./leetCode/21_merge_two_sorted_lists.py)
12. :large_blue_circle: [Generate Parentheses](./leetCode/22_generate_parentheses.py)
13. :white_circle: [Remove Duplicates From Sorted Array](./leetCode/26_remove_duplicates_sorted_array.py)
14. :large_blue_circle: [Add Two Numbers](./leetCode/2_add_two_numbers.py)
15. :red_circle: [Longest Valid Parentheses](./leetCode/32_longest_valid_parentheses.py)
16. :white_circle: [Search Insert Position](./leetCode/35_search_insert_position.py)
17. :large_blue_circle: [Longest Substring Without Repeating Characters](./leetCode/3_longest_substring_without_repeating_characters.py)
18. :large_blue_circle: [Rotate Image](./leetCode/48_rotate_image.py)
19. :large_blue_circle: [Maximum Subarray](./leetCode/53_maximum_subarray.py)
20. :large_blue_circle: [Spiral Matrix](./leetCode/54_spiral_matrix.py)
21. :large_blue_circle: [Longest Palindromic Substring](./leetCode/5_longest_palindromic_substring.py)
22. :large_blue_circle: [Search A 2D Matrix](./leetCode/74_search_2d_matrix.py)
23. :large_blue_circle: [Subsets](./leetCode/78_subsets.py)
24. :white_circle: [Palindrome Number](./leetCode/9_palindrome_number.py)
25. :large_blue_circle: [Sort List](./leetCode/linked-list/148_sort_list.py)
26. :white_circle: [Palindrome Linked List](./leetCode/linked-list/234_palindrome_linked_list.py)
27. :red_circle: [Merge K Sorted Lists](./leetCode/linked-list/23_merge_k_sorted_lists.py)
28. :white_circle: [Middle Of The Linked List](./leetCode/linked-list/876_middle_of_the_linked_list.py)

### Tags by count

1. **Array**: 13
2. **String**: 8
3. **Two Pointers**: 6
4. **Linked List**: 6
5. **Dynamic Programming**: 5
6. **Hash Table**: 5
7. **Math**: 5
8. **Binary Search**: 3
9. **Divide And Conquer**: 3
10. **Stack**: 3
11. **Recursion**: 3
12. **Matrix**: 3
13. **Bit Manipulation**: 2
14. **Sorting**: 2
15. **Backtracking**: 2
16. **Merge Sort**: 2
17. **Greedy**: 1
18. **Counting**: 1
19. **Sliding Window**: 1
20. **Simulation**: 1
21. **Divider And Conquer**: 1
22. **Heap (Priority Queue)**: 1
