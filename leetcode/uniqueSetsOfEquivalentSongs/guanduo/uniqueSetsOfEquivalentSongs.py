"""
Given a list of matching/equivalent song pairs and a list of unique songs, create unique sets of equivalent songs

Input:
[[1,2],[2,3],[5,6],[4,6],[2,7],[3,8],[9,10]]
unique songs: [1,2,3,4,5,6,7,8,9,10]
Output: [[1,2,3,7,8],[4,5,6],[9,10]]

"""

"""
Use union find to solve. Since the first song is not 0, use two hash tables to track parent/child
and total groups.

"""

class Solution:
            
    def uniqueSets(self,uniqueSongs,pairs):
        class unionFindSet:

            def __init__(self,uniqueSongs):
                self.parent = {i:i for i in uniqueSongs}        #parent hash to track disjoint-set relationship
                self.children = {i:[i] for i in uniqueSongs}    #children hash to track total number of unions (set)
                
            def find(self,song):                                #return the parent of the union
                if song not in self.parent: return None
                while 1:                                        #keep going to the parent
                    parent = self.parent[song]
                    if parent == song: return parent
                    song = parent
                    
            def union(self,song1,song2):                        #union two songs into single set. Update children hash
                if self.find(song1) == self.find(song2): return #same set. nothing is required
                parent1 = self.find(song1)
                parent2 = self.find(song2)
                self.parent[parent2] = parent1                  #union the two sets.
                self.children[parent1].extend(self.children[parent2])  #combine the two sets
                del self.children[parent2]                      #delete the older set
        disjointSet = unionFindSet(uniqueSongs)
        for i,j in pairs:
            disjointSet.union(i,j)                              #union all pairs
        return [list(x) for x in disjointSet.children.values()] #just return all existing sets after unioning all pairs

if __name__ == '__main__':

    uniq = [1,2,3,4,5,6,7,8,9,10]
    pairs = [[1,2],[2,3],[5,6],[4,6],[2,7],[3,8],[9,10]]

    sol = Solution()
    print(sol.uniqueSets(uniq,pairs))

