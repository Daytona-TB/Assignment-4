def most_popular_airport(file_path, month):
    def parse_date(date_str):
        return date_str.split("-")

    def extract_month(date_str):
        return parse_date(date_str)[1]

    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except IOError:
        return f"Error: An I/O error occurred while trying to read the file '{file_path}'."

    destination_counts = {}
    for line in data:
        fields = line.strip().split(",")
        if len(fields) < 9:
            continue

        try:
            flight_month = extract_month(fields[8])
        except IndexError:
            return "Error: Unexpected data format in the CSV file."

        if flight_month == month:
            destination = fields[3]  # Destination City, State
            if destination in destination_counts:
                destination_counts[destination] += 1
            else:
                destination_counts[destination] = 1

    if not destination_counts:
        return "Error: No data found for the specified month."

    most_popular = max(destination_counts, key=destination_counts.get, default=None)

    return most_popular

def main():
    # Example usage:
    file_path = "Airports2.csv"
    month = "07"  # July
    print(most_popular_airport(file_path, month))

if __name__ == "__main__":
    main()
