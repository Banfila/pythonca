import csv
import pandas as pd


# reads the csv file.
employeelist = pd.read_csv('employeelist.csv', encoding="unicode_escape")
# reads the email dictionary from the  csv file into the new list.
init_emails = employeelist['email'].tolist()
# the line below creates an empty list used to store the updated email.
new_emails = []
for email in init_emails:
    # the string replacement function used to replace the emails.
    new_emails.append(email.replace("@helpinghands.cm", "@handsinhands.org"))
    # the  two lines below are for retrieving the names and phone numbers from the list.
name = employeelist['name'].tolist()
phone = employeelist['phone'].tolist()
header = ['Name', 'Email', 'phone']
# converts the data to a dictionary to be added to the new csv list.
my_dict = {"Name": name, "Email": new_emails, "Phone": phone}
with open('updatedemployeelist.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(my_dict.keys())
    writer.writerows(zip(*my_dict.values()))
print("Operation completed")
#after running the code, the updated list will show up in the folder.

