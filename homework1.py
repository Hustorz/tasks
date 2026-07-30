#1st task
from unittest import result


def task1():
    students_number = 10
    marks = []
    for i in range(students_number): 
        while True: 
            try:
                mark = float(input(f"Enter the mark for student {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    average_mark = sum(marks) / students_number
    for i in range(students_number):    
        if marks[i] < 60:
            letter_mark = 'F'
        elif marks[i] < 70:
            letter_mark = 'D'
        elif marks[i] < 80:
            letter_mark = 'C'
        elif marks[i] < 90:
            letter_mark = 'B'
        else:
            letter_mark = 'A'
        print(f"Student {i + 1}: Mark = {marks[i]}, Letter Grade = {letter_mark}")
    print(f"Average Mark: {average_mark}")
    print(f"Students passed: {sum(1 for mark in marks if mark >= 60)}") 


#task2()
def task2():
    while True:
        while True:
            raw_input = input("Enter the credit amount: ")
            try:
                amount = float(raw_input)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                continue
            if amount < 0:
                print("Please enter a non-negative amount.")
                continue
            break
        while True:
            raw_rate = input("Enter the interest rate (%): ")
            try:
                rate = float(raw_rate)
            except ValueError:
                print("Error: please enter a number.")
                continue
            if rate < 0:
                print("Error: the rate cannot be negative.")
                continue
            break
        while True:
            raw_months = input("Enter the term in months: ")
            try:
                months = int(raw_months)
            except ValueError:
                print("Error: please enter a whole number.")
                continue
            if months <= 0:
                print("Error: the term must be greater than 0.")
                continue
            break
        
        monthly_rate = rate / 100 / 12
 
        if monthly_rate == 0:
            payment = amount / months
        else:
            payment = amount * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
 
        total_paid = payment * months
        overpayment = total_paid - amount
 
        print("\n--- Calculation Result ---")
        print(f"Monthly payment: {payment:.2f}")
        print(f"Total amount paid: {total_paid:.2f}")
        print(f"Overpayment: {overpayment:.2f}")
 
        answer = input("\nRepeat the calculation? (yes/no): ").strip().lower()
        if answer != "yes" and answer != "y":
            print("Exiting.")
            break

#task3()
def task3():
    orders = [
    {"product": "Laptop", "price": 1200, "qty": 2},
    {"product": "Mouse", "price": 25, "qty": 10},
    {"product": "Keyboard", "price": 80, "qty": 5},
    ]
 
    # Revenue per product (List Comprehension)
    revenue_list = [
        {"product": order["product"], "revenue": order["price"] * order["qty"]}
        for order in orders
    ]
 
    print("Revenue per product")
    for item in revenue_list:
        print(f"{item['product']}: {item['revenue']}")
 
    # Product with the maximum revenue
    best_product = revenue_list[0]
    for item in revenue_list:
        if item["revenue"] > best_product["revenue"]:
            best_product = item
 
    print(f"\n Top product by revenue: {best_product['product']} ({best_product['revenue']})")
 
    # Products sorted by revenue, descending
    sorted_by_revenue = sorted(revenue_list, key=lambda item: item["revenue"], reverse=True)
 
    print("\n Products sorted by revenue (descending)")
    for item in sorted_by_revenue:
        print(f"{item['product']}: {item['revenue']}")

#task4()
#task5()
def task5():
    data = [1,2,3,2,4,5,2,3,6,7,6,6,1]
    duplicates = []
    done = []
    for i in data:
        if i not in done:
            done.append(i)
        else:
            duplicates.append(i)
    print(duplicates)                


#task6()
def task6():
    data = [3, 1, 2, 3, 4, 1, 5, 2, 6]
 
    done = set()
    unique = []
    for item in data:
        if item not in done:
            done.add(item)
            unique.append(item)
 
    print(f"Original list: {data}")
    print(f"Without duplicates (order preserved): {unique}")

#task7()
def task7():
    data = [1, 2, 3, 2, 4, 1, 5, 2]

    max_count = 0
    most_common = None

    for x in data:
        count = data.count(x)
        if count > max_count:
            max_count = count
            most_common = x

    print(most_common)

#task8()
def task8():
    data = [1, 2, 3, 2, 4, 1, 5]

    counts = {}

    for x in data:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] += 1

    print(counts)

#task9() 
def task9():
    lst1 = [1, 2, 3, 4, 5, 6, 9]
    lst2 = [4, 3, 2, 1, 5, 5, 4]

    same = True


    if len(lst1) != len(lst2):
        same = False
    else:
        for x in lst1:
            if lst1.count(x) != lst2.count(x):
                same = False
                break

    print(same)    

#task10()
def task10():
    dict1 = {'a': 3, 'b': 190, 'c': 7}
    dict2 = {'a': 5, 'c': 9, 'd': 5}

    result = {}
    for key in dict1:
        result[key] = dict1[key]
    for key in dict2:
        if key in result:
            result[key] += dict2[key]   
        else:
            result[key] = dict2[key]    

    print(result)

#task11()
def task11():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    common = set1 & set2
    print(common)

#task12()
def task12():
    lists = [[1, 2], [1, 2, 3, 6, 7, 8], [100], [23, 43, 2, 0, 5]]

    longest = lists[0]      

    for lst in lists:
        if len(lst) > len(longest):
            longest = lst

    print(longest)

#task13()
def task13():
    lst = [1, 2, 3, 3, 5, 100, 1]

    dupl = False

    for x in lst:
        if lst.count(x) > 1:
            dupl = True
            break

    print(dupl)

#task14()
def task14():
    lst = [1, 2, 3, 4]
    s = 5

    pairs = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == s:
                pairs.append((lst[i], lst[j]))

    print(pairs)