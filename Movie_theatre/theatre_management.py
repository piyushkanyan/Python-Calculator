movie_names = [
    "Avengers: Endgame",
    "Interstellar",
    "Inception",
    "The Dark Knight",
    "Spider-Man: No Way Home",
    "Oppenheimer",
    "Joker",
    "Titanic",
    "Avatar",
    "Avatar: The Way of Water",
    "Doctor Strange",
    "Iron Man",
    "Black Panther",
    "The Batman",
    "Mission Impossible",
    "Fast X",
    "John Wick 4",
    "Kung Fu Panda 4",
    "Inside Out 2",
    "Deadpool & Wolverine",
    "Dune Part Two",
    "The Lion King",
    "Frozen II",
    "Moana",
    "Toy Story 4",
    "3 Idiots",
    "Pk",
    "Dangal",
    "Kalki 2898 AD",
    "Bahubali",
    "Ramayana",
    "Dhurandhar"
]
movies_ID = [
    "MX01",
    "MX02",
    "MX03",
    "MX04",
    "MX05",
    "MX06",
    "MX07",
    "MX08",
    "MX09",
    "MX10",
    "MX11",
    "MX12",
    "MX13",
    "MX14",
    "MX15",
    "MX16",
    "MX17",
    "MX18",
    "MX19",
    "MX20",
    "MX21",
    "MX22",
    "MX23",
    "MX24",
    "MX25",
    "MX26",
    "MX27",
    "MX28",
    "MX29",
    "MX30",
    "MX31",
    "MX32",
]
movie_duration = [
    "3h 1m",
    "2h 49m",
    "2h 28m",
    "2h 32m",
    "2h 28m",
    "3h 0m",
    "2h 2m",
    "3h 15m",
    "2h 42m",
    "3h 12m",
    "1h 55m",
    "2h 6m",
    "2h 14m",
    "2h 56m",
    "1h 50m",
    "2h 21m",
    "2h 49m",
    "1h 34m",
    "1h 36m",
    "2h 8m",
    "2h 46m",
    "1h 58m",
    "1h 43m",
    "1h 47m",
    "1h 40m",
    "2h 50m",
    "2h 33m",
    "2h 41m",
    "3h 1m",
    "2h 39m",
    "3h 0m",
    "3h 34m"
]
ticket_prices = [
    250,300,400,340,420,550,220,340,540,330,
    430,560,230,220,430,520,530,560,660,330,
    110,100,300,400,500,200,600,340,540,240,
    270,280
    ]
ratings = [
    8.8, 9.4, 8.6, 9.1, 9.7, 8.9, 9.3, 8.7,
    9.5, 8.6, 9.0, 9.8, 8.7, 9.2, 8.9, 9.6,
    8.8, 9.3, 8.6, 9.1, 9.7, 8.9, 9.4, 8.7,
    9.5, 9.0, 8.8, 9.2, 9.6, 8.7, 9.9, 9.9
]
snacks = [
    "Popcorn",
    "Cheese Popcorn",
    "Caramel Popcorn",
    "Nachos",
    "French Fries",
    "Burger",
    "Pizza Slice",
    "Hot Dog",
    "Sandwich",
    "Garlic Bread",
    "Cold Drinks",
    "Coke",
    "Pepse",
    "Sprite",
    "Fanta",
    "Coffee",
    "Tea",
    "Hot Chocolate",
    "Milkshake",
    "Ice Cream",
    "Chocolate",
    "Cookies",
    "Brownie",
    "Donut",
    "Cup Noodles",
    "Water Bottle",
    "Orange Juice",
    "Mango Juice",
    "Candy",
    "Samosa"
]
snacks_prices = [
    150,180,200,220,180,
    250,300,270,220,240,
    120,100,100,100,100,
    150,80,180,220,120,
    80,100,150,120,90,
    40,120,130,60,50
]
Booking_ids = []
age_cart = []
customer_names_cart = []
Mobile_number_cart = []
Booking_history = []
Customer_cart = []
Feedback_cart = []
number_of_tickets_cart = []
seat_number_asking_cart = []

seat_number = [
    "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10",
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10",
    "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10"
]
# Genres align by index with movie_names.
genres = [
    "Action, Adventure, Sci-Fi",
    "Adventure, Drama, Sci-Fi",
    "Action, Sci-Fi, Thriller",
    "Action, Crime, Drama",
    "Action, Adventure, Sci-Fi",
    "Biography, Drama, History",
    "Crime, Drama, Thriller",
    "Drama, Romance",
    "Action, Adventure, Sci-Fi",
    "Action, Adventure, Sci-Fi",
    "Action, Adventure, Fantasy",
    "Action, Adventure, Sci-Fi",
    "Action, Adventure, Sci-Fi",
    "Action, Crime, Drama",
    "Action, Adventure, Thriller",
    "Action, Crime, Thriller",
    "Action, Crime, Thriller",
    "Adventure, Animation, Comedy",
    "Adventure, Animation, Comedy",
    "Action, Adventure, Comedy",
    "Adventure, Drama, Sci-Fi",
    "Adventure, Animation, Drama",
    "Adventure, Animation, Comedy",
    "Adventure, Animation, Comedy",
    "Adventure, Animation, Comedy",
    "Comedy, Drama",
    "Comedy, Drama, Sci-Fi",
    "Biography, Drama, Sport",
    "Action, Fantasy, Sci-Fi",
    "Action, Drama, Fantasy",
    "Fantasy, Mythology",
    "Action, Crime, Thriller",
]
Payment_method_cart = (
    "Cash",
    "UPI",
    "Credit Card",
    "Debit-Card",
    "Net-Banking"
)
debit_card_cart = []
upi_cart = []
credit_card_cart = []
net_banking_cart = []

membership_type_cart = (
    "None",
    "Silver",
    "Gold",
    "Platinum"
)
show_timings = (
    "09:00 AM",
    "11:30 AM",
    "02:00 PM",
    "04:30 PM",
    "07:00 PM",
    "09:30 PM",
    "11:45 PM"
)


print("===================================================================")
print("                    SMART MOVIE THEATRE SYSTEM                     ")
print("===================================================================")
print()
print("---------------------------CUSTOMER MENU---------------------------")
print()
print("1. View All Movies")
print("2. Search Movie")
print("3. Book Movie Ticket")
print("4. Cancel Booking")
print("5. View My Booking")
print("6. View Booking History")
print()
print("----------------------------SNACKS MENU----------------------------")
print()
print("7. View Snacks Menu")
print("8. Add Snacks to Cart")
print("9. Remove Snacks")
print("10. View Cart")
print("11. Clear Cart")
print()
print("--------------------------MEMBERSHIP MENU--------------------------")
print()
print("12. View Membership Plans")
print("13. Buy Membership")
print("14. Check Membership Status")
print()
print("---------------------------FEEDBACK MENU---------------------------")
print()
print("15. Rate A Movie")
print("16. Give Theatre Feedback")
print("17. View Movie Ratings")
print()
print("---------------------------PAYMENT MENU----------------------------")
print()
print("18. Checkout")
print("19. Select Payment Method")
print("20. Print Receipt")
print()
print("----------------------------ADMIN MENU-----------------------------")
print()
print("21. Add New Movie")
print("22. Remove Movie")
print("23. Update Ticket Price")
print("24. Update Movie Rating")
print("25. Add Show Timing")
print("26. Remove Show Timing")
print("27. View Theatre Report")
print()
print("-------------------------------EXIT---------------------------------")
print()
print("28. Exit")
print()

while True:
    choice = int(input("Please Enter your choice: "))
    if choice == 1:
        print()
        print("------------------------------------- You choose 1 option (View All Movies) ----------------------------------------")
        print()
        print("="* 120)
        print(f"{"Movie ID":<13}{"Movie Name":<28}{"Genre":<35}{"Duration Time":<18}{"Price":<12}{"Rating"}")
        print("="* 120)
        for i in range(len(movie_names)):
            print(f"{movies_ID[i]:<13}{movie_names[i]:<28}{genres[i]:<35}{movie_duration[i]:<18}{ticket_prices[i]:<12}{ratings[i]}")
    elif choice == 2:
        while True:
            search_movie = input("Enter the movie name you want to search (q to quit): ").title().strip()
            print()
            if search_movie in movie_names:
                exist_movie_name = movie_names.index(search_movie)
                print("="* 120)
                print(f"{"Movie ID":<13}{"Movie Name":<28}{"Genre":<35}{"Duration Time":<18}{"Price":<12}{"Rating"}")
                print("="* 120)
                print(f"{movies_ID[exist_movie_name]:<13}{movie_names[exist_movie_name]:<28}{genres[exist_movie_name]:<35}{movie_duration[exist_movie_name]:<18}{ticket_prices[exist_movie_name]:<12}{ratings[exist_movie_name]}")
                break
            elif search_movie == "Q":
                break
            else:
                print(f"This movie {search_movie} is not available")
    elif choice == 3:
        while True:
            purchasing_movie_id = input("Enter the Movie ID to buy (q to stop): ").upper().strip()
            if purchasing_movie_id in movies_ID:
                while True:
                    seat_number_asking = input("Type the seat number you want (Type s to show seats): ").upper()
                    if seat_number_asking.upper().strip() == "S":
                        print("="*55)
                        for seats in seat_number:
                            print(f"{seats:<5}",end="")
                            if seats.endswith("10"):
                                print()
                        print("="*55)
                    else:
                        print(f"{seat_number_asking} is available and added to cart")
                        seat_number_asking_cart.append(seat_number_asking)
                        how_much_tickets = int(input("Enter the tickets you want to buy: "))
                        if how_much_tickets == 1:
                            print("Added to cart successfully")
                            number_of_tickets_cart.append(how_much_tickets)
                        else:
                            print("Added to cart successfully")
                            number_of_tickets_cart.append(how_much_tickets)
                        break
                break   
            
              
            elif purchasing_movie_id.lower().strip() =="q":
                break
            else:
                print(f"Invalid Movie {purchasing_movie_id} ID")
        customer_names = input("Enter you name: Mr/Mrs ").title().strip()
        customer_names_cart.append(customer_names)

        age = int(input("Enter your age: "))
        age_cart.append(age)
       
        mobile_number = int(input("Enter you mobile number: +91 "))
        if mobile_number > 10 and mobile_number < 10:
            print("The number cannot be greater and less than 10")
            mobile_number = int(input("Enter you mobile number: +91 "))
            Mobile_number_cart.append(mobile_number)
        else:
            Mobile_number_cart.append(mobile_number)
        print()
        print("---------PAYMENT METHODS---------")
        for i in range(len(Payment_method_cart)):
            print(f"{i}. {Payment_method_cart[i]}")
        print("----------------------------------")
        payment_method = int(input("Choose the Payment Method (0-4): "))
        if payment_method == 0:
            print()


