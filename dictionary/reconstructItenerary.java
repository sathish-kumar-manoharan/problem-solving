/*
 * https://leetcode.com/problems/reconstruct-itinerary/
Time Complexity: The time complexity of the DFS algorithm is (O(V + E)), where (V) is the number of vertices (airports) and (E) is the number of edges (flights). This is because in the worst case, the algorithm explores each vertex and edge exactly once12.

Space Complexity: The space complexity of the DFS algorithm is (O(V)) in the worst case. This is due to the space required for the recursion stack when performing the DFS traversal12.

In your specific implementation:

Building the graph takes (O(E)) time, where (E) is the number of tickets.
Sorting the destinations for each origin takes (O(E \log E)) time.
The DFS traversal itself takes (O(V + E)) time.
Therefore, the overall time complexity of your findItinerary method is (O(E \log E + V + E)), which simplifies to (O(E \log E)) since (E \geq V) in a connected graph.

The space complexity remains (O(V)) due to the recursion stack used in the DFS traversal.
 */
class Solution {
    HashMap<String, LinkedList<String>> flightMap = new HashMap<>();
    LinkedList<String> result = null;
  
    public List<String> findItinerary(List<List<String>> tickets) {
             
      // Step 1). build the graph first
      for(List<String> ticket : tickets) {
        String origin = ticket.get(0);
        String dest = ticket.get(1);
          
        this.flightMap.putIfAbsent(origin, new LinkedList<String>());
        this.flightMap.get(origin).add(dest);
      }
  
      // Step 2). order the destinations
      this.flightMap.forEach((key, value) -> Collections.sort(value));
  
      this.result = new LinkedList<String>();
        
      // Step 3). post-order DFS
      this.dfs("JFK");
        
      return this.result;
    }
  
    protected void dfs(String origin) {
        
      // Visit all the outgoing edges first.
      if (this.flightMap.containsKey(origin)) {
        LinkedList<String> destList = this.flightMap.get(origin);
          
        while (!destList.isEmpty()) {
          // while we visit the edge, we trim it off from graph.        
          this.dfs(destList.removeFirst());
        }
      }
        
      // add the airport to the head of the itinerary
      this.result.addFirst(origin);
    }
  }