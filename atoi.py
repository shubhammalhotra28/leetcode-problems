class Solution:
    def myAtoi(self, str: str) -> int:
        
        str = str.strip();
        
        output = 0;
        negative = False;
        
        if not str:
            return 0;
        if str[0]=='+':
            negative = False;
        elif str[0]=="-":
            negative = True;
        elif not str[0].isnumeric():
            return 0;
        else:
            output = ord(str[0])-ord("0");
            
        for i in range(1,len(str)):
            
            if str[i].isnumeric():
                output = output*10+(ord(str[i])-ord("0"));
                
                if negative and output>=2147483648:
                    return -2147483648;
                if not negative and output>=2147483648:
                    return 2147483647;
                
            else:
                break;
                
        
        if negative == False:
            return output;
        else:
            return -output;
        
        
        
