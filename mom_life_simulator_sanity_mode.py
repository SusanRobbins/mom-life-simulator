"""
Mom Life Simulator: Sanity Mode
A humorous, text-based simulation of a day in the life of a mom with toddlers.
Author: Susan Robbins – Tired Mom #73289472
"""

def simulate_morning():
    print("\nMorning: Your toddler wants to break out paints before you've had coffee.")
    print("Your brain is still asleep and processing your dream about paint all over the house.\n")

def simulate_afternoon():
    print("\nAfternoon: You've been up for 8 hours and feel like you've fought through 5 wars on two bites of crackers.")
    print("Drink your cold coffee. It's better than nothing.\n")

def simulate_evening():
    print("\nEvening: Captain Mom's Log—toddler witching hour.")
    print("It's either screen time or WWE Smackdown until bedtime.")
    print("Cleaning awaits. So does the question: who even *are* you anymore?\n")

def show_exit_message():
    print("\nQuitting the simulation.")
    print("Remember: You are tired, but you still showed up.\n")

def handle_unknown_input():
    print("\nYou are a speck of stardust in the toddler ether, bending to chaos.\n")

def mom_life_simulator():
    sanity = 5
    print("Welcome to Mom Life Simulator: Sanity Mode")
    print("You start the day with 5 sanity points.")
    print("Type 'morning', 'afternoon', 'evening', or 'q' to quit.\n")

    while sanity > 0:
        time_of_day = input(f"Sanity: {sanity} | What part of the day are we surviving now? ").strip().lower()

        if time_of_day == "morning":
            simulate_morning()
        elif time_of_day == "afternoon":
            simulate_afternoon()
        elif time_of_day == "evening":
            simulate_evening()
        elif time_of_day == "q":
            show_exit_message()
            break
        else:
            handle_unknown_input()
            continue  # Don't penalize unknown input

        sanity -= 1

    if sanity == 0:
        print("Your sanity has left the building. Simulation over.\n")
        print("You did your best, and that's all that matters.")

if __name__ == "__main__":
    mom_life_simulator()
