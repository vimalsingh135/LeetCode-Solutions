class Solution(object):
    def reverseWords(self, s):
        result = ""
        
        # Pointer starting from end
        i = len(s) - 1
        
        # Traverse from right to left
        while i >= 0:
            # Skip spaces
            while i >= 0 and s[i] == " ":
                i -= 1
            
            # If pointer out of bounds, break
            if i < 0:
                break
            
            # Mark end of word
            end = i
            
            # Move left until space or start
            while i >= 0 and s[i] != " ":
                i -= 1
            
            # Extract the word
            word = s[i + 1:end + 1]
            
            # Add space if result is not empty
            if result != "":
                result += " "
            
            # Append word
            result += word
        
        return result

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))
        