import random
import matplotlib.pyplot as plt

def simulate_dice_throws(throws):
    results = {i: 0 for i in range(2, 13)}  

    for _ in range(throws):
        throw = random.randint(1, 6) + random.randint(1, 6)  
        results[throw] += 1

    probabilities = {sum_: count / throws for sum_, count in results.items()}  

    return probabilities

probabilities = simulate_dice_throws(1000000)

print("Сума: Ймовірність")
for sum_, probability in probabilities.items():
    print(f"{sum_}: {probability:.4f}")

plt.bar(probabilities.keys(), probabilities.values(), color='blue')
plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум кидків двох кубиків')
plt.xticks(range(2, 13))
plt.show()