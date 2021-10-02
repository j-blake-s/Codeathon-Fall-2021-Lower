author: Lex

# __Shift Sift__

## <b>Situation</b>
You work for a very important industrial pound cake manufacturer. Your job is to operate a large sifting machine that shifts flour from right to left. As this is "pound" cake, your dough can be represented a discrete integers (pound cake is hard!). You first sum all of the flour in your basin. Then you shake the basin to the right, pushing the rightmost bit of flour off to processing. Then you again sum the flour that remains in the basin (which no longer has the rightmost flour bit). You then shift left, removing the leftmost bit and summing what remains. Continue until there is only one bit of flour remaining. Each sum adds to a total sum, which you report back to the pound cake president.

Below is an example:


Example: 
Input: [1,2,3]

    [1,2,3] -> sum = 6
     [1,2]  -> sum = 3
      [2]   -> sum = 2

Output: final sum: 6 + 3 + 2 = 11

Example:
input: [1,2,3,4,5]

    [1,2,3,4,5] 
     [1,2,3,4]
      [2,3,4]
       [2,3]
        [3]

Output:
    Sum is: 42


