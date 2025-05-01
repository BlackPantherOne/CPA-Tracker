import os
import csv
import matplotlib.pyplot as plt

# Styling and Colors for Terminal Interface
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RESET = '\033[0m'

# Dummy Data for Analysis
data = [
    {'source': 'Google Ads', 'clicks': 1500, 'conversions': 300, 'cost': 100},
    {'source': 'Facebook', 'clicks': 1200, 'conversions': 200, 'cost': 80},
    {'source': 'Instagram', 'clicks': 1000, 'conversions': 150, 'cost': 50}
]

offer_payment = 10  # Example Offer Payment per Conversion

# Function to calculate conversion rate
def calculate_conversion_rate(clicks, conversions):
    if clicks == 0:
        return 0
    return (conversions / clicks) * 100

# Function to calculate ROI
def calculate_roi(conversions, offer_payment, cost):
    if cost == 0:
        return 0
    return ((conversions * offer_payment) - cost) / cost

# Function to generate report and show it in graphs
def generate_report(data):
    sources = [entry['source'] for entry in data]
    conversion_rates = [calculate_conversion_rate(entry['clicks'], entry['conversions']) for entry in data]
    rois = [calculate_roi(entry['conversions'], offer_payment, entry['cost']) for entry in data]

    # Plotting Conversion Rates
    plt.figure(figsize=(10, 5))
    plt.bar(sources, conversion_rates, color='green')
    plt.title("Conversion Rates by Source")
    plt.xlabel("Traffic Sources")
    plt.ylabel("Conversion Rate (%)")
    plt.show()

    # Plotting ROI
    plt.figure(figsize=(10, 5))
    plt.bar(sources, rois, color='blue')
    plt.title("ROI by Source")
    plt.xlabel("Traffic Sources")
    plt.ylabel("ROI")
    plt.show()

# Function to export the report to a CSV file
def export_report_to_csv(data):
    with open('traffic_report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Source', 'Clicks', 'Conversions', 'Conversion Rate (%)', 'ROI'])
        for entry in data:
            conversion_rate = calculate_conversion_rate(entry['clicks'], entry['conversions'])
            roi = calculate_roi(entry['conversions'], offer_payment, entry['cost'])
            writer.writerow([entry['source'], entry['clicks'], entry['conversions'], conversion_rate, roi])
    print(GREEN + "Report successfully exported to traffic_report.csv" + RESET)

# Function to clear saved results
def clear_results():
    open('traffic_report.csv', 'w').close()
    print(RED + "All saved results cleared!" + RESET)

# Main Menu
def display_menu():
    os.system("cls" if os.name == "nt" else "clear")
    print(CYAN + "=" * 60)
    print("   CPA Traffic Source Analysis Tool")
    print("      Designed for Professional Marketers")
    print("=" * 60 + RESET)
    print(f"""
[1] Start Traffic Source Analysis
[2] View Traffic Report (CSV)
[3] Export Traffic Report to CSV
[4] Clear Saved Report Data
[5] Exit
""")

# Main Function to run the program
def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            print(YELLOW + "\nStarting Traffic Source Analysis..." + RESET)
            generate_report(data)
        elif choice == '2':
            if os.path.exists("traffic_report.csv"):
                with open('traffic_report.csv', 'r') as file:
                    print(file.read())
            else:
                print(RED + "No report available. Please run the analysis first." + RESET)
        elif choice == '3':
            export_report_to_csv(data)
        elif choice == '4':
            clear_results()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print(RED + "Invalid selection. Please try again." + RESET)

if __name__ == "__main__":
    main()
