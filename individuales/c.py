#7.5 Problem 5: Word frequency counter (list + dict)

words = input ("Type a sentence: ").lower().split()
freq_dict = {}
most_common =""
max_freq = 0
if len (words) <= 0:
    print ("Please type something")
else: 
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else: 
          freq_dict [word] = 1
    for word, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            most_common = word
    print (f"Words list: {words}")
    print (f"Frequencies: {freq_dict}")       
    print (f"Most common word: {most_common}")
