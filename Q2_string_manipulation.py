import pandas as pd
import re

def process_employee_names():
    df = pd.read_csv('employee_master.csv')
    
    # Titles to remove
    titles = r'^(Dr\.|Mr\.|Ms\.|Mrs\.)\s*'
    
    df['Clean_Name'] = df['Employee_Name'].str.replace(titles, '', regex=True).str.strip()
    
    def split_name(name):
        parts = name.split()
        if len(parts) == 1:
            return parts[0], '', ''
        elif len(parts) == 2:
            return parts[0], '', parts[1]
        else:
            return parts[0], ' '.join(parts[1:-1]), parts[-1]
            
    # Apply splitting
    df[['First_Name', 'Middle_Initial', 'Last_Name']] = df['Clean_Name'].apply(lambda x: pd.Series(split_name(x)))
    
    # Generate Username: firstinitial.lastname (all lowercase)
    df['Base_Username'] = df['First_Name'].str[0].str.lower() + df['Last_Name'].str.lower()
    
    # Handle duplicates
    usernames = []
    username_counts = {}
    duplicates_handled = 0
    
    for uname in df['Base_Username']:
        if uname in username_counts:
            # Duplicate found
            username_counts[uname] += 1
            new_uname = f"{uname}{username_counts[uname]}"
            usernames.append(new_uname)
            duplicates_handled += 1
        else:
            username_counts[uname] = 1
            usernames.append(uname)
            
    df['Username'] = usernames
    
    # Display the final DataFrame with the first 8 rows
    print("Final DataFrame (First 8 Rows):")
    print(df[['Employee_Name', 'First_Name', 'Middle_Initial', 'Last_Name', 'Username']].head(8))
    print(f"\nTotal number of duplicate usernames handled: {duplicates_handled}")

if __name__ == "__main__":
    process_employee_names()
