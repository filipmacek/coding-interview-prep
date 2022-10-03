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


