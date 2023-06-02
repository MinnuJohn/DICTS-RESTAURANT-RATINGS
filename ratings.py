"""Restaurant rating lister."""


# put your code here
def restaurant_ratings(filename):
    """Organize items in a dictionary and sort in alphabetical order+"""

    file = open(filename)
    dic_restaurant ={}
    for line in file:
        line=line.rstrip()
        words = line.split(':')
        restaurant_name = words[0]
        restaurant_rate = words[1]
        dic_restaurant[restaurant_name] = restaurant_rate
    
    #calling ouside functions    
    print_dictionary(dic_restaurant)
    ask_user(dic_restaurant)
    print_dictionary(dic_restaurant)

def print_dictionary(restaurant_dic):
    """function to print the sorted dictionary"""

    for name, rate in sorted(restaurant_dic.items()):
        print(f"{name} is rated at {rate}")

def ask_user(data_list):
    """function to ask user for a new restaurant name and user rating
      and add it to the dictionary """
    
    #get inputs restaurant name and rating
    name = input("Please provide restaurant name:\n")
    rating = int(input("What is your rating of the restaurant?\n"))

    #check if user entered valied rating(1-5) else ask to key in rateing again
    while rating not in range(1,6):
        rating = int(input("What is your rating of the restaurant?\n"))
    
    #add key and value to dictionary    
    data_list.update({name:rating})
   
        
