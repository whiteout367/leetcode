class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest 
        substring
        without repeating characters

        Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        문자열을 반복문으로 돌리면서 저장
        
        시간 내에 못품(연습)
        """
        str_list = []
        max_length = 0
        
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
                
            str_list.append(x)
            print(str_list) 
            max_length = max(max_length, len(str_list))
            
        return max_length