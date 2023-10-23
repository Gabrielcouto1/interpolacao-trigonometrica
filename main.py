import subprocess
import numpy as np
import matplotlib.pyplot as plt
import re
import tkinter as tk
from tkinter import simpledialog

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Use simpledialog to get input from popup windows
    num_points = simpledialog.askinteger("Input", "Número de pontos:")
    spacing = simpledialog.askfloat("Input", f"Espaçamento dos pontos [2pi/{num_points}]:")
    numbers = []

    for i in range(num_points):
        number = simpledialog.askfloat("Input", f"Insira o valor de y para x={i}")
        numbers.append(number)

    command = f"./c_main_trig_interpolation {num_points} {spacing}"
    for number in numbers:
        command += f" {number}"

    result = subprocess.run(command, stdout=subprocess.PIPE, shell=True, text=True)

    if result.returncode != 0:
        print("Error running the C program.")
        exit(1)

    output = result.stdout.strip()
    output = str(output)

    with open('output.txt', 'w') as file:
        file.write("Pontos \n\nx | y \n")

        i=0

        for value in numbers:
            file.write(f"{i}\t|{value}\n")
            i+=spacing

        file.write("\nFunção trigonométrica interpolada:\n")
        file.write(output)

    output = output.replace("f(x) = ", "")
    print(output)

    output = re.sub(r'cos\(', 'np.cos(', output)
    output = re.sub(r'sin\(', 'np.sin(', output)
    output = re.sub(r'pi', 'np.pi', output)

    def custom_function(x):
        return eval(output)

    x = np.linspace(0, spacing*num_points, 10000)  
    y = custom_function(x)
    x_numbers = np.arange(0, num_points * spacing, spacing)

    plt.figure(figsize=(8, 4))
    plt.scatter(x_numbers, numbers, label='Pontos', color='red', marker='o')
    plt.plot(x, y, label='Função', color='blue')
    plt.title('Resultado da interpolação trigonométrica')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.savefig("trig_function_plot.png")

    plt.close()

if __name__ == "__main__":
    main()
