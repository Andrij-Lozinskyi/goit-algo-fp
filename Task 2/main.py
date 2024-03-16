import turtle
import math

def draw_pifagor_tree(t, branch_length, level):
    if level == 0:
        return
    
    t.forward(branch_length)
    
    t.right(45)
    draw_pifagor_tree(t, branch_length * math.sqrt(0.5), level - 1)
    
    t.left(90)
    draw_pifagor_tree(t, branch_length * math.sqrt(0.5), level - 1)
    
    t.right(45)
    t.backward(branch_length)

def main():
    window = turtle.Screen()
    window.title("Дерево Піфагора")
    
    t = turtle.Turtle()
    t.speed('fastest') 
    t.left(90) 

    recursion_level = int(input("Введіть рівень рекурсії: "))
    
    draw_pifagor_tree(t, 100, recursion_level)
    
    window.mainloop()

if __name__ == "__main__":
    main()