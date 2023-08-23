import matplotlib.pyplot as plt

def main():
    # Data for the pie chart
    labels = ['Apples', 'Bananas', 'Oranges', 'Grapes']
    sizes = [30, 25, 20, 15]
    colors = ['red', 'yellow', 'orange', 'purple']
    
    # Create a pie chart
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    
    # Add a title
    plt.title("Fruit Distribution")
    
    # Display the chart
    plt.show()

if __name__ == "__main__":
    main()

