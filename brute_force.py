def brute_force(text, pattern):
    text_length = len(text)  # The text which is to be
     # checked for the existence of the pattern
    pattern_length = len(pattern)  # The pattern to be determined in the text

    i = 0 # keeps track of the characters of the text
    j = 0 # keeps track of the characters of the pattern
    # looping variables are set to 0

    flag = False  # If the pattern doesn't appear at all,
    # then set this to false and execute the last if statement

    while i < text_length:  # iterating from the 0th index of text
        j = 0
        count = 0  # Count stores the length upto which the pattern and the text have matched

        while j < pattern_length:
            if (i + j < text_length and text[i + j] == pattern[j]):  # statement to check if a 
                # match has occoured or not

                # text[i + j] shifts the index of characters in the text
                # because of the loop i and j


                count += 1  # if the statement evaluates to true, then update count

            j += 1

        if (count == pattern_length):  # if total number of successful matches is equal
            # to count of the array
            print("\nPattern occours at index", i)

            repr_pattern = i + pattern_length
        
            print('\n', text[:i],'[',text[i : repr_pattern],']', text[repr_pattern:])  # print the starting index of the successful match

            flag = True  # Even if the matching occours once, set this flag to True

        i += 1 # increase the i counter 
        # marks the end of the while loop


    if (not flag):  # If the pattern doesn't occours even once, this statement gets executed
        print("\nPattern is not at all present in the array")


brute_force("Today’s date is 12th November, 2022. 8:14:14 pm.", "Today’s d")  # function call
