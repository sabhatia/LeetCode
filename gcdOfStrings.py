str1 = 'aa'
str2 = 'a'

def gcdOfStrings(str1: str, str2: str) -> str:
    
    if len(str1) > len(str2):
        short_str = str2
        long_str = str1
    else:
        short_str = str1
        long_str = str2

    gcd_candidate = short_str
    for gcd_factor in range(1,len(short_str)+1):

        # Let's get the test string and length
        gcd_candidate_len = len(short_str)//gcd_factor
        gcd_candidate = short_str[:gcd_candidate_len]

        # If the length is not divisible into both strings, forget it
        if len(short_str) % gcd_candidate_len != 0 or \
        len(long_str) % gcd_candidate_len != 0:
            # moving on
            continue
        
        # Lengths match, do the strings match
        short_factor = len(short_str) // gcd_candidate_len
        long_factor = len(long_str) // gcd_candidate_len

        if (gcd_candidate*short_factor != short_str) or \
        (gcd_candidate*long_factor != long_str):
            # moving on
            continue

        # Ooh la la! Everything matched
        # And since we tried the longest option, this is the best match
        return gcd_candidate
        
    #end for

    return ''

if __name__ == '__main__':
    str1 = 'aa'
    str2 = 'a'

    print(f'GCD: {gcdOfStrings(str1, str2)}')