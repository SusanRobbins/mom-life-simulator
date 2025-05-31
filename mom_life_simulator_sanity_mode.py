"""
Mom Life Simulator: Sanity Mode
Simulates a day in the life of a mom with toddlers based on time of day, now featuring a sanity meter.
Author: Susan, Tired Mom #73289472 
"""
def mom_life_simulator():
    sanity = 5 # Sanity starts full (haha jk it's never full anymore) Scale: 0 (lost to the abyss) to 5 (hang in there kitty poster)
    
    while True:
        print(f"\nSanity Meter: {sanity}/5")
        time_of_day = input("What time of day is it? (morning/afternoon/evening or 'q' to quit): ").lower()

        if time_of_day == "morning":
            print("Morning, toddler wants to break out paints before coffee.")
            print("Your brain is still asleep, you're an npc. Sanity takes a hit.")
            sanity -= 1
            if sanity < 0:
                print("There's no hope. Find Blippi or Rachel.")
        elif time_of_day == "afternoon":
            print("It's afternoon, but you've been up for 8 hours on two crackers.")
            print("Drink your cold coffee, it's better than nothing. Don't even try to warm it up and leave the toddlers unattended.")
            sanity -= 1
        elif time_of_day == "evening":
            print("Captain Mom's Log: It's the toddler witching hours. Screen time or they wrestle each other until they are so hyped up that they can't sleep.")
            print("You survive... in theory.")
            sanity -= 2
        elif time_of_day == "q":
            print("Quitting the simulation. Remember, the candy you stashed beside the ambien. Use it.")
            break
        else:
            print("Husband says he has 8 minutes to give you a break, but it takes 2 minutes for the kids to detach and once you sit down on the toilet you fall asleep.")
            sanity -= 1
        if sanity <=0:
            print("\nSanity is gone, along with half of your toddler's socks.")
            print("You propose a game of pretend to put mommy to sleep, but you lay down and now are a bouncy castle. Also, they need more juice.")

mom_life_simulator()