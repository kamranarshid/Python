#break, continue and pass
moviesList = ['JungleBook', 'Inter stella', "Titanic", "Baby"]
for movies in moviesList:
    print(movies)
    if movies == 'Titanic':
        print("My favourite movie is " + movies)
        break

#continue
Dishes = ["Pasta", "Burger","Salad", "spicy Curry", "Chicken & Chicken", "Spicy Noodles"]
for dish in Dishes:
    if "spicy" in dish:
        print("Skipping:", dish)
        continue
    print("Eating:", dish)

#pass
tasks = ["clean the room", "skip"]
for task in tasks:
    if task == "skip":
        pass
    else:
        print(task)