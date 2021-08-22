# 👫🏽 Stable-Matching Problem
A CLI Python tool to implement the famous Gale-Shapley Algorithm to solve the Stable Matching problem.

## The Problem:
In mathematics, economics, and computer science, the stable matching algorithm seeks to solve the problem of finding a stable match between two sets of equal size given a list of preferences for each element.
 
 We can define "matching" and "stable" by the following definitions.
 - Matching: Mapping from the elements of one set to the elements of another set
 - Stable: No element **A** of the first set that prefers an element **B** of the second set over its current partner such that element **B** prefers element **A** over its current partner.

## The Gale–Shapley Algorithm:
Also known as the deferred acceptance algorithm or propose-and-reject algorithm, is an algorithm for finding a solution to the stable matching problem.
It takes polynomial time, and the time is linear in the size of the input to the algorithm. 
It is a truthful mechanism from the point of view of the proposing participants, for whom the solution will always be optimal.

NOTE: I learnt the algorithm with the men and women being considered as two different sets for matching. 
For simplicity of implementation, I have continued with the same. However, I support diversity of all kinds <3

### Psuedocode:
```
algorithm stable_matching is
    Initialize m ∈ M and w ∈ W to free
    while ∃ free man m who has a woman w to propose to do
        w := first woman on m's list to whom m has not yet proposed
        if ∃ some pair (m', w) then
            if w prefers m to m' then
                m' becomes free
                (m, w) become engaged
            end if
        else
            (m, w) become engaged
        end if
    repeat
```
## To Run
```
python main.py
```

## Usage
Users can input:
1. Number of members that they wish to have in each set
2. Names of members within each set
3. Preference ranking for members within each set

The interface provides a stable match as an output

## Interface

Calculation logs after each member's preferences have been input
<img src="https://github.com/amritaravishankar/stable-matching/blob/master/CLI%20.png" width="500">

Source: Wikipedia
