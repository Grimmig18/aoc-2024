# Advent of Code 2024 - Day 6: Guard Gallivant

## Challenge Description

### Part One

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

#### Example Input:
```
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
```

The map shows:
- The guard's current position (`^`) and facing direction (up).
- Obstructions such as crates or desks (`#`).

The guard follows these patrol rules:
1. If there is an obstacle directly in front of them, turn right 90 degrees.
2. Otherwise, take a step forward.

#### Patrol Example:
Starting at position `(#..^.....)`, the guard moves:
- **Up** several times until an obstacle is encountered:
  ```
  ....#.....
  ....^....#
  ..........
  ..#.......
  .......#..
  ..........
  .#........
  ........#.
  #.........
  ......#...
  ```
- **Right** at the first obstacle and continues forward:
  ```
  ....#.....
  ........>#
  ..........
  ..#.......
  .......#..
  ..........
  .#........
  ........#.
  #.........
  ......#...
  ```
- **Down** after encountering another obstacle:
  ```
  ....#.....
  .........#
  ..........
  ..#.......
  .......#..
  ..........
  .#......v.
  ........#.
  #.........
  ......#...
  ```

Eventually, the guard leaves the map. Including their starting position, the positions visited by the guard before leaving are marked with `X`:

```
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
```

In this example, the guard visits **41 distinct positions**.

**Task:** Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?

**Puzzle Answer (Part One):** 4374

---

### Part Two

The Historians realize the guard's patrol area is simply too large for them to safely search. However, adding a single obstruction might stop the guard in a loop, allowing the lab to be searched without risk.

#### Loop Example:
To minimize paradox risk, a new obstruction must:
- Cause the guard to get stuck in a loop.
- Be placed in a way that the guard won’t notice.

Possible positions for the new obstruction are marked as `O` in six configurations:

#### Example Configurations:
1. **Near the starting position:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ....|..#|.
   ....|...|.
   .#.O^---+.
   ........#.
   #.........
   ......#...
   ```

2. **Bottom-right quadrant:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ......O.#.
   #.........
   ......#...
   ```

3. **Next to the standing desk:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   .+----+O#.
   #+----+...
   ......#...
   ```

4. **Bottom-left corner:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ..|...|.#.
   #O+---+...
   ......#...
   ```

5. **Shifted bottom-left corner:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   ....|.|.#.
   #..O+-+...
   ......#...
   ```

6. **Next to the universal solvent tank:**
   ```
   ....#.....
   ....+---+#
   ....|...|.
   ..#.|...|.
   ..+-+-+#|.
   ..|.|.|.|.
   .#+-^-+-+.
   .+----++#.
   #+----++..
   ......#O..
   ```

In this example, there are **6 positions** where an obstruction can cause the guard to loop.

**Task:** How many different positions could you choose for this obstruction to trap the guard in a loop?

**Puzzle Answer (Part Two):** 1705

---

## Puzzle Answers

- **Part One:** 4374  
- **Part Two:** 1705  

---

## Notes

This challenge involves simulating patrol behavior on a grid and analyzing paths. Part Two introduces a design problem to identify positions that create loops, requiring spatial reasoning and algorithmic simulation.