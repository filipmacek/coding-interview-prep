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


