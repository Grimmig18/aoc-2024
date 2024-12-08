# Advent of Code 2024 - Day 5: Print Queue

## Challenge Description

### Part One

Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

The Elf must recognize you because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation `X|Y` means that if both page number `X` and page number `Y` are to be produced as part of an update, page number `X` must be printed at some point **before** page number `Y`.

The Elf provides you with the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

For example:

#### Ordering Rules:
```
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13
```

#### Updates:
```
75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
```

### Correctly Ordered Updates
The first update, `75,47,61,53,29`, is in the correct order:
- 75 is correctly first, as all other pages come after it.
- 47 is correctly second, as all other pages come after it.
- 61 is correctly in the middle, with 75 and 47 before it and 53 and 29 after it.
- 53 is correctly fourth, as it comes before 29.
- 29 is the last page.

Similarly, the second and third updates are also correctly ordered. However, the fourth, fifth, and sixth updates are not.

For the correctly-ordered updates:
```
75,47,61,53,29
97,61,53,29,13
75,29,13
```
The middle pages are `61`, `53`, and `29`. Adding these gives **143**.

**Task:** Determine which updates are already in the correct order. What do you get if you add up the middle page numbers from those correctly-ordered updates?

**Puzzle Answer (Part One):** 7074

---

### Part Two

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the correct order. For the above example:

#### Incorrectly Ordered Updates:
```
75,97,47,61,53 -> 97,75,47,61,53
61,13,29       -> 61,29,13
97,13,75,29,47 -> 97,75,47,29,13
```

For these fixed updates, the middle pages are `47`, `29`, and `47`. Adding these together produces **123**.

**Task:** Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?

**Puzzle Answer (Part Two):** 4828

---

## Puzzle Answers

- **Part One:** 7074  
- **Part Two:** 4828  

---

## Notes

This challenge required checking whether a sequence adhered to partial ordering rules and then calculating middle values for updates. Part Two added complexity by requiring the reordering of sequences based on the same rules, which tested algorithmic logic for topological sorting.