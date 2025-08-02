import random

def has_duplicate_birthday(num_people: int, simulations: int = 10000) -> float:
    duplicate_count = 0

    for _ in range(simulations):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(birthdays) != len(set(birthdays)):
            duplicate_count += 1

    probability = duplicate_count / simulations
    return probability

if __name__ == "__main__":
    for group_size in range(5, 51, 5):
        prob = has_duplicate_birthday(group_size)
        print(f"{group_size:2d} people -> Probability of shared birthday ≈ {prob:.4f}")
