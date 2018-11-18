Rules: get the lowest score for reading the values from disk.
Disk.check() can't be used in your solution - it's only there to validate the reads to make sure 
your solution is actually returning the right values. 
Also, you can use a few variables for bookkeeping, but it's cheating to make your own arrays 
to accompany the caches. For instance, you can't have a second array with len() = 500 to store 
the index associated with a value. You'll need to be judicious with the space you have, just like in the real world!

LEADERBOARD FOR CACHE HOMEWORK:
1) Awadi: 1.1E7 / 10781633
2) Karl: 5.4E8 / 539,398,608 (8 bookkeeping variables, only using small cache)
3) Default score: 1E9 / 1,000,000,000 (0 bookkeeping variables)
