from tkinter import *
from tkinter import messagebox
import statistics as stats
import tkinter as tk
import math

# -------------Main Screen------------- #
screen = Tk()
screen.title("Calculator")


# -------------------------------------FUNCTIONS--------------------------------------------#
# ******************************Ditoy maikabil dagitay functions*****************************#
def calcu1():
    def calculate_stats():
        data = entry_data.get()
        data = data.split(',')
        data = [float(x.strip()) for x in data]
        if data:
            mean = stats.mean(data)
            median = stats.median(data)
            mode = stats.mode(data)
            stdev = stats.stdev(data)
            variance = stats.variance(data)

            messagebox.showinfo("Descriptive Statistics",
                                f"Mean: {mean}\nMedian: {median}\nMode: {mode}\nStandard Deviation: {stdev}\nVariance: {variance}")
        else:
            messagebox.showerror("Error", "Please enter valid data.")

    c = Toplevel(screen)
    c.title("Descriptive Statistics Calculator")

    Label(c, text="Calculator 1", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)

    label_data = Label(c, text="Enter Numbers with comma: ")
    label_data.grid(row=1, column=0, sticky=W, padx=10, pady=10)
    entry_data = Entry(c)
    entry_data.grid(row=1, column=1, padx=10, pady=10)

    
    btn_calculate = Button(c, text="Calculate", command=calculate_stats)
    btn_calculate.grid(row=2, columnspan=2, padx=10, pady=10)
    c.mainloop()


 
def calcu2():
    def calculate_frequency_table():
        data = input_text.get("1.0", tk.END).split()  # Split input by whitespace
        data = list(map(int, data))  # Convert input to integers

        if len(data) == 0:
            messagebox.showerror("Error", "Please enter some data.")
            return

        frequency_table = frequency_distribution(data)

        # Update the result text box with the frequency table
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Element\tFrequency\tCumulative Frequency\tRelative Frequency\tCumulative Relative Frequency\n")
        for row in frequency_table:
            result_text.insert(tk.END, f"{row['element']}\t{row['frequency']}\t\t{row['cumulative_frequency']}\t\t\t{row['relative_frequency']}\t\t\t{row['cumulative_relative_frequency']}\n")

    def frequency_distribution(data):

        # Count the frequency of each element
        freq_dict = {}
        total_elements = len(data)
        for element in data:
            if element in freq_dict:
                freq_dict[element] += 1
            else:
                freq_dict[element] = 1

        # Sort the dictionary by keys for a consistent order
        sorted_freq_dict = dict(sorted(freq_dict.items()))

        # Calculate cumulative frequency and relative frequency
        cumulative_freq = 0
        frequency_table = []
        for element, frequency in sorted_freq_dict.items():
            cumulative_freq += frequency
            relative_freq = frequency / total_elements
            cumulative_relative_freq = cumulative_freq / total_elements
            frequency_table.append({
                'element': element,
                'frequency': frequency,
                'cumulative_frequency': cumulative_freq,
                'relative_frequency': relative_freq,
                'cumulative_relative_frequency': cumulative_relative_freq
            })

        return frequency_table

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Frequency Distribution Calculator")

    # Create input label and text box
    input_label = tk.Label(window, text="Enter data (separated by whitespace):")
    input_label.pack()
    input_text = tk.Text(window, height=5)
    input_text.pack()

    # Create calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate_frequency_table)
    calculate_button.pack()

    # Create result text box
    result_text = tk.Text(window, height=10)
    result_text.pack()

    window.mainloop()
    
    
    
def calcu3():
    def calculate_permutations():
    
        n = int(entry_n.get())
        r = int(entry_r.get())
        result = math.factorial(n) // math.factorial(n - r)
        result_label.config(text=f"Permutations (nPr): {result}")

    def calculate_combinations():
    
        n = int(entry_n.get())
        r = int(entry_r.get())
        result = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
        result_label.config(text=f"Combinations (nCr): {result}")

    # Create the main window
    root = tk.Tk()
    root.title("Permutations and Combinations Calculator")

    # Create input labels and entry fields
    label_n = tk.Label(root, text="Total number of items (n):")
    label_n.grid(row=0, column=0, padx=10, pady=10)
    entry_n = tk.Entry(root)
    entry_n.grid(row=0, column=1, padx=10, pady=10)

    label_r = tk.Label(root, text="Number of items to choose (r):")
    label_r.grid(row=1, column=0, padx=10, pady=10)
    entry_r = tk.Entry(root)
    entry_r.grid(row=1, column=1, padx=10, pady=10)

    # Create buttons to calculate permutations and combinations
    button_permutations = tk.Button(root, text="Calculate Permutations (nPr)", command=calculate_permutations)
    button_permutations.grid(row=2, column=0, padx=10, pady=10)

    button_combinations = tk.Button(root, text="Calculate Combinations (nCr)", command=calculate_combinations)
    button_combinations.grid(row=2, column=1, padx=10, pady=10)

    # Create label to display results
    result_label = tk.Label(root, text="")
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


def calcu4():
    # Function to calculate probability
    def calculate_probability():
        total_outcomes = int(total_outcomes_entry.get())
        favorable_outcomes = int(favorable_outcomes_entry.get())

        # Check for valid inputs
        if total_outcomes <= 0 or favorable_outcomes < 0 or favorable_outcomes > total_outcomes:
            result_label.configure(text='Invalid input. Please enter valid values.')
            return

        # Calculate probability
        probability = favorable_outcomes / total_outcomes
        result_label.configure(text='Probability: {:.4f}'.format(probability))

    # Create a GUI window
    root = tk.Tk()
    root.title('Probability Calculator')

    # Create input fields for total outcomes and favorable outcomes
    total_outcomes_label = tk.Label(root, text='Total Outcomes:')
    total_outcomes_label.pack()
    total_outcomes_entry = tk.Entry(root)
    total_outcomes_entry.pack()

    favorable_outcomes_label = tk.Label(root, text='Favorable Outcomes:')
    favorable_outcomes_label.pack()
    favorable_outcomes_entry = tk.Entry(root)
    favorable_outcomes_entry.pack()

    # Create a button to calculate the probability
    calculate_button = tk.Button(root, text='Calculate Probability', command=calculate_probability)
    calculate_button.pack()

    # Create a label to display the result
    result_label = tk.Label(root, text='')
    result_label.pack()

    root.mainloop()


def calcu5():
    c = Toplevel(screen)
    c.title("Calculator 5")

    Label(c, text="Calculator 5", font=('Calibri', 14)).grid(row=0, sticky=N, pady=10)


# --------------------------------LABELS IN MAIN SCREEN----------------------------------------#
Label(screen, text="CALCULATOR", font=('Calibri', 25)).grid(row=0, sticky=N, pady=10)

# --------------------------------------------BUTTONS IN MAIN SCREEN--------------------------------------------------#
Button(screen, text="Descriptive Statistics", font=('Calibri', 20), width=30, command=calcu1).grid(row=1, sticky=N, pady=10)
Button(screen, text="Frequency Distribution Table", font=('Calibri', 20), width=30, command=calcu2).grid(row=2, sticky=N, pady=10)
Button(screen, text="Permutations and Combinations", font=('Calibri', 20), width=30, command=calcu3).grid(row=3, sticky=N, pady=10)
Button(screen, text="Probability", font=('Calibri', 20), width=30, command=calcu4).grid(row=4, sticky=N, pady=10)
Button(screen, text="Awan pay yt", font=('Calibri', 20), width=30, command=calcu5).grid(row=5, sticky=N, pady=10)



#-------------------------------------------------------------------------------------------------------------------------------------------#
screen.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------#
