class Solution:
    def intToRoman(self, num: int) -> str:
        value_roman={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        result = ''
        #while num <= 0
        for val in value_roman:
            sha = num // val
            if sha >= 0:
                num = num - val * sha
                result += value_roman[val] * sha

        return result