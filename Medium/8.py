class Solution:
    def myAtoi(self, s: str) -> int:
        """
        1. 문자열 공백 제거
        2. -, + 확인
        3. 문자열을 하나씩 읽는데, 그 값이 int형일 때만
        4. 범위 확인
        5. 변환
        """
        INT_MIN=-(2**31)
        INT_MAX=(2**31)-1
        
        s=s.strip()
        
        first=None
        for character in s:
            if not first:
                if character.isdigit() or character in {'-','+'}: 
                    first=character 
                else: 
                    break
            else: 
                if character.isdigit():
                    first+=character
                else: 
                    break
        
        if not first or first in {'-','+'}:
            first=0
        elif int(first)<INT_MIN:
            first=INT_MIN
        elif int(first)>INT_MAX:
            first=INT_MAX
            
        return int(first)
        

