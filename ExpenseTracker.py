def max_column(lst,length):
    idx = 0
    for j in lst:
        if len(j)>length[idx]:
            length[idx] = len(j)
        idx+=1
    return length

def add():
    date = input("Enter the date DD/MM/YYYY :: ").strip()
    while True: 
        try: 
            amt = float(input("Enter Amount: "))
            if amt <= 0:
                print("Amount must be greater than 0.")
                continue
            break 
        except ValueError: 
            print("Invalid amount! Please enter a number.")

    print("Expense categories are :\n")
    categories = ["Food","Transport","Entertainment","Others"]
    print(f"{'Food':<14} (1)\n{'Transport':<14} (2)\n{'Entertainment':<14} (3)\n{'Others':<14} (4)\n") 
    category = int(input("Choose any one of the above category ::"))
    while True:
        if category < 1 or category >4:
            print("-"*5,"Invalid Choice. Please enter valid choice","-"*5,"\n")
            category = int(input("Choose any one of the above category ::"))
        else:
            break
    note = input("Enter Note (if not press enter) :: ")
    row = f"{date},{amt},{categories[category-1]},{note}\n"
    with open("data.txt","a") as f:
        f.write(row)

def display(rows):
    while True:
        ch = input("Do you want to filter expenses by category. (y,n) :: ").lower().strip()
        categories = ["Food","Transport","Entertainment","Others"]
        if ch == "y":
            print("\nExpense categories are :\n")
            print(f"{'Food':<14} (1)\n{'Transport':<14} (2)\n{'Entertainment':<14} (3)\n{'Others':<14} (4)\n") 
            category = int(input("Choose any one of the above category :: "))
            while True:
                if category < 1 or category >4:
                    print("-"*5,"Invalid Choice. Please enter valid choice","-"*5,"\n")
                    category = int(input("Choose any one of the above category ::"))
                else:
                    break
            break
        elif ch == "n":
            category = None
            break
        else:
            print("-"*5,"Invalid Choice. Please enter valid choice","-"*5,"\n")

    length = [4, 6, 8, 4]
    flag = False
    for row in rows:
        lst = row[:-1].split(",")
        if category == None:
            length = max_column(lst,length)
        else:
            if lst[2] == categories[category-1]:
                flag = True
                length = max_column(lst,length)
        
    header = True
    total = 0
    for row in rows:
        lst = row[:-1].split(",")
        if category is None:
            print(f"|{lst[0]:<{length[0]}} | {lst[1]:<{length[1]}} | {lst[2]:<{length[2]}} | {lst[3]:<{length[3]}} |")
            if not header:
                total+=float(lst[1])    
        else:
            if flag:
                if lst[2] == categories[category-1] or lst[2]=="Category":
                    print(f"|{lst[0]:<{length[0]}} | {lst[1]:<{length[1]}} | {lst[2]:<{length[2]}} | {lst[3]:<{length[3]}} |")
                    if not header:
                        total+=float(lst[1])
            else:
                print("Category is not present in the Expenses")
                break
        header = False
    print("\nTotal Expense is ",total)
def view():
    try:
        with open("data.txt", "r") as f:
            rows = f.readlines()
            rows.insert(0,"Date,Amount,Category,Note\n")
            display(rows)

    except FileNotFoundError:
        print("Error: The text file 'data.txt' does not exist yet. \nCreating one")
        with open("data.txt", "w") as f:
            pass
        print("Empty file created successfully.")

while True:
        print(f"\n{'CLI Expense Tracker':-^50}\n")
        print("1. Add an expense.")
        print("2. View all expenses.")
        print("3. Exit\n")
        ch = int(input("Enter Choice: ")) 
        if ch == 1:
            print(f"{'Adding Expense':-^50}\n")
            add()
        elif ch == 2:
            print(f"{'Past Expenses':-^50}\n")
            view()
        elif ch == 3:
            print(f"{'Thank You':-^50}\n")
            break
        else:
            print("Invalid input! Please enter a number.\n") 