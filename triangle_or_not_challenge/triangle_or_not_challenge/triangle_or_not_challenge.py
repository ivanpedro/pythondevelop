
"""
Mary boutght three flowers from a flower market. Each flower has a differnt number of petals,
and each petal has some inger written on it . She wants to sum the numbers
written on the petals of each fo the fhree flowers and then determine whether her three sums 
correspond to the side lengths of a non-degenerate triangle
(i.e, a triangle in which each side has non-zero length.
For example, the respective petal sums 3,4  and 5 correspond to the side length) of a valid triangle,
but the sums 1,2 and 6 do not.

Complete the triangle or not function in the editor below. it has the following parameters:
1. An arra;y of p integers, firstflower, donoting the integers writteng on the fisrs flower's petals.
2. An array of q integers, secundFlower, denoting the integers writteng on the second flower's petals.
3. An array of r integers, thirdFlower, denoting the integers written on the third flower's petals.

Input Format:

The first line contains an integer, p, denoting the number of petals in firsFloeer.
Each line i of the p subsequent lines( where <= i < p) contains an integer describin firsFloweri.
The next line contains an iteger, q, denoting the number of petals in secondflower.
Each line i of the q sebsequent lines (where 0 <= i < q) contains an integer describing secondFloweri.
The next line contains an integer, r, denoting the number of petals in thirdFlower.
Each line i of the r subequent lines( wher 0<= i < r) contains a string describin ThirdFloweri.

Contraints:

3 <= p,q,r <= 10^5
1 <= firstFloweri <= 10^3 (where 0 <= i < p)
1 <= secondFloweri <= 10^3 (wher 0 <= i < q)
1 <= thirdFloweri <= 10^3 (where 0 <= i < r)

Output Format:

return the string Yes if th three petal sums correspond to the side lengths of a
non-degenerate triangle; otherwise, return No.

"""