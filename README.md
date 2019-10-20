# SimilarDoc
Program to determine the similarity between two documents. Also pretends to have a really small time complexity.  

The algorithm I've implemented is similar to the proposed by G. Salton, A. Wong, and C. S. Yang (1975) in "A Vector Space Model for Automatic Indexing".

What it basically does is calculate the distance between arrays of tuples of words, and the frequency of this words. With these arrays, it calculates the angle between them. So 90º means that the arrays has no words in common and 0º means they are identical, so the closest to 0º the value obtained, the similar those documents are.
