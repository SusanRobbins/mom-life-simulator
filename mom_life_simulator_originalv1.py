"""
Mom Life Simulator
Simulates a day in the life of a mom with toddlers based on time of day.
Author: Susan, Tired Mom #73289472 
"""
def mom_life_simulator():
    while True:
        time_of_day = input("What time of day is it? (morning/afternoon/evening or 'q' to quit): ").lower()

        if time_of_day == "morning":
            print("Morning, toddler wants to break out paints before coffee.")
            print("Your brain is still asleep and processing your dream about paint all over the house.")
        elif time_of_day == "afternoon":
            print("It's afternoon, but you've been up for 8 hours and feel like you've fought through 5 wars on two bites of crackers.")
            print("Drink your cold coffee, it's better than nothing.")
        elif time_of_day == "evening":
            print("Captain Mom's Log: It's the toddler witching hours. Screen time or they wrestle each other until they are so hyped up that they can't sleep.")
            print("Bedtime is near, but so is cleaning and trying to train your brain.")
        elif time_of_day == "q":
            print("Quitting the simulation. Remember, you are a warrior in the battle of motherhood.")
            break
        else:
            print("You are a spec of stardust in the universe, bending to the chaos of the toddler ether.")

mom_life_simulator()