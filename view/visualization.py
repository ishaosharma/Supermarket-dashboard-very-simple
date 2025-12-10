#view/: Contains code for data visualization.
import matplotlib.pyplot as plt

def plot_bar(labels, values, title, xlabel, ylabel):
    plt.figure(figsize=(10,6))
    plt.bar(labels, values, color='skyblue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def plot_pie(labels, values, title):
    plt.figure(figsize=(7,7))
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.tight_layout()
    return plt
