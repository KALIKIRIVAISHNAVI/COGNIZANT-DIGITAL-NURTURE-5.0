import statistics

def analyze_sales():
    try:
        with open("sales.txt", "r") as file:
            sales = []

            for line in file:
                sales.append(float(line.strip()))

        mean_sales = statistics.mean(sales)
        median_sales = statistics.median(sales)

        print("Sales Statistics Summary")
        print(f"Total Records: {len(sales)}")
        print(f"Mean Sales: {mean_sales:.2f}")
        print(f"Median Sales: {median_sales:.2f}")

    except FileNotFoundError:
        print("Error: sales.txt file not found")

    except ValueError:
        print("Error: Invalid data in sales file")

analyze_sales()