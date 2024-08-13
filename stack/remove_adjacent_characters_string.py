from string import ascii_lowercase
class Solution:
    
    """
    Time complexity : O(N), where N is a string length.
    Space complexity : O(N-D) where D is a total length for all duplicates.
    
    """
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]: 
                output.pop()
            else: 
                output.append(ch)
        return ''.join(output)
    


    """
    Time complexity : 
    O(N ^2), where N is a string length. Here we have an onion: while -> for -> replace. while is executed not more than 

    N/2 times, for is always run 26 times, and replace has 
    O(N) run time in average. In total that results in 
    𝑂(𝑁2×26×𝑁)O( 2N​ ×26×N) = O(N^2 ).

    Space complexity : 
    O(N). The hashset of duplicates has the constant length 26, but the replace function actually creates a copy of the string and thus uses 
    
    """
    
    def removeDuplicates(self, S: str) -> str:
        # generate 26 possible duplicates
        duplicates = {2 * ch for ch in ascii_lowercase}
        
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            for d in duplicates:
                S = S.replace(d, '')
                
        return S