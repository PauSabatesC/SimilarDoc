# SimilarDoc
Program to determine the similarity between two documents. Also pretends to has a small time complexity.  

The algorithm I've implemented to know the similarity is the proposed by G. Salton, A. Wong, and C. S. Yang (1975) in "A Vector Space Model for Automatic Indexing".

What basically it does is calculate the distance between arrays of tuples of words and frequency of this words. And with these arrays I calculate the angle between, so 90º means that the arrays has no words in common and 0º means they are identical, so the closest to 0º the value obtained, the similar those documents are.
