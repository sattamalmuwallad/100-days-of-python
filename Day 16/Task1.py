from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define column names
table.field_names = ["Name", "Age", "Country"]

# Add some rows
table.add_row(["Sattam", 21, "Saudi Arabia"])
table.add_row(["Alice", 25, "UK"])
table.add_row(["Bob", 23, "USA"])

# Print the table
print(table)
