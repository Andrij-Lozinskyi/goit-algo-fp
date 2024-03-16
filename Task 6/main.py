def greedy_algorithm(items, budget):
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    
    total_calories = 0
    selected_items = []
    
    for item in items_sorted:
        if budget - item[1]["cost"] >= 0:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
            selected_items.append(item[0])
    
    return selected_items, total_calories

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    
    for i in range(1, budget + 1):
        for item in items.values():
            if item["cost"] <= i:
                dp[i] = max(dp[i], dp[i - item["cost"]] + item["calories"])
    return dp[budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Greedy algorithm:")
print("Selected items:", selected_items_greedy)
print("Total calories:", total_calories_greedy)

total_calories_dp = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Total calories:", total_calories_dp)