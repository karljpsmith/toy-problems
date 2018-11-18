Rules: get the lowest score for reading the values from disk.
Disk.check() can't be used in your solution - it's only there to validate the reads to make sure 
your solution is actually returning the right values. 
Also, you can use a few variables for bookkeeping, but it's cheating to make your own arrays 
to accompany the caches. For instance, you can't have a second array with len() = 500 to store 
the index associated with a value. You'll need to be judicious with the space you have, just like in the real world!
