

def word_count(text): #Each function has a role this one counts characters
    count = 0
    for i in text:
        count+=1
    print(f"Word Count: {count}")

def find_longest_word(text): # This function finds the longest word
    longest_word = ""
    split_word = text.split()
    for word in split_word:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
    

  
def count_substring(text, substring):# This function finds the length of a given substring
    var = text.split()
    count  = var.count(substring)
    return count
def extract_unique_words(text):# This function finds the words in a list and removes the ones that occur more than once
    unique_words = text.split()
    for i in range(len(unique_words)):
        for j in range(i+1, len(unique_words)):
            if unique_words[i] == unique_words[j]:
                unique_words.remove(unique_words[j])
    print(unique_words)
        
      
      


if __name__ == "__main__":# Main file where most happens
    word = []
    unique_words = []
    

    print("Welcome to the Text processing test")
    user_input = input("Enter a text for analysis ->")
    print("You entered", user_input)
    print("Text analysis options: ")
    print("----------------------")
   
   
    


while True:# While loop to keep user choosing until they choose to exit 


    print("Choose an option or quit")
    print(" 1. Word Count\n 2. Longest Word\n 3. Count of Substring\n 4. Unique Words\n 5. Exit")
    num_input = int(input("-> "))

    #Branching is used below to process user input

    if num_input == 1:
        word_count(user_input)

    if num_input == 2:
       find_word = find_longest_word(user_input)
       print(find_word)

    if num_input == 3:
        substring_input = input("Enter a word to count")
        data = count_substring(user_input, substring_input)
        print(data)
        continue

    if num_input == 4:
        extract_unique_words(user_input)

    if num_input == 5:
        print("Thanks for playing, have a nice day!")
        print("Quitting...")
        break



