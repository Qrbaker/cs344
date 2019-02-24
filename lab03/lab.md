# Lab 03 Responses #
Quentin Baker

## Exercise 3.1 ##
1.  Everything instantly solves the "solved" puzzle (shocker!). AC-3 solves the easy puzzle almost instantly. 
    Backtracking solves the easy puzzle after about 30 seconds. Both Depth-first search and Min-conflicts failed on 
    easy. Beyond the easy puzzle, nothing was solving the puzzle, at least not in a timely manner.
2.  
    *   With `select_unassigned_variable` changed, backtracking search performed *worse*. I let it run for about 5 
        minutes on easy on my computer without a result.
    *   With inference set to `forward_checking`, backtracking solved the easy sudoku puzzle nearly instantly, and the
        harder puzzle after a a couple of minutes.
    
    A combination of `mrv` and `forward_checking` was able to solve all levels of sudoku puzzles quickly. This makes
    sense, because minimum conflicts is a heuristic that eliminates lots of other unlikely paths, while forward checking
    can combine with this heuristic to proactively prune paths that will not lead to a solution.
 
## Exercise 3.2 ##
1.  This problem was not solvable at all by DFS due to a bug in the code. AC-3 wasn't able to solve it as well, because
    some solutions require queens to be in inconsistent relation to each other. Backtracking was able to solve quickly up
    to about 20 queens, and minimum conflicts was by far the best performer, reaching solution sets of over 3,000 queens!
2. `mrv` Allows backtracking to increase its effectiveness up to about 150 queens, and `mrv` plus `forward_checking`
    increases it to 300. Forward checking on its own was not appreciably better than default.
3.  Minimum conflicts requires a near O(1) amount of steps, as it greedily assigns as many initial positions as it can,
    then relaxes the remaining into a successful position. Given that the board grows with the amount of queens, this
    means about the same amount of non-greedily solved peaces will need to be relaxed on a given board. The oft-cited
    example on Wikipedia is roughly 50 steps needed for *a million queens*.
    