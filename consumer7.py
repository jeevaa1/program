# Sample data


# Check whether the consumer number is available in the database


# Modify a consumer number

# Append a new consumer


# Sort the consumer based on number


# Remove a consumer


# Remove all consumers


# Delete the tuple


def app():
    consumer_db = (
    ('001', '1234567890'),
    ('002', '2345678901'),
    ('003', '3456789012'),
    ('004', '4567890123'),
    ('005', '5678901234')
)
    print("""
1. Check whether the consumer number is avalable in the database. 
2. Modify a consumer number
3. Append  a new consumer
4. Sort the consumer based on number
5. Remove a consumer 
6. Remove all the consumer
7. Delete the tuple.
""")
    op = int(input("Enter your options: "))

    if op == 1:
        search_consumer = str(input("Enter consumer number: "))
        for consumer in consumer_db:
            if consumer[0] == search_consumer:
                print("Consumer found:", consumer)
                app()
        else:
            print("Consumer not found")
            app()

    elif op == 2:
        modify_consumer = str(input("Enter consumer number: "))
        new_consumer_number = str(input("Enter new consumer number: "))
        new_consumer_db = []
        for consumer in consumer_db:
            if consumer[0] == modify_consumer:
                new_consumer_db.append((new_consumer_number, consumer[1]))
            else:
                new_consumer_db.append(consumer)
        consumer_db = tuple(new_consumer_db)
        print("Consumer database after modification:", consumer_db)
        app()

    elif op == 3:
        cons_num = str(input("Enter consumer number: "))
        mobile = str(input("Enter consumer mobile number: "))
        new_consumer = (cons_num, mobile)
        consumer_db += (new_consumer,)
        print("Consumer database after appending:", consumer_db)
        app()

    elif op == 4:
        sorted_db = sorted(consumer_db, key=lambda x: x[0])
        print("Sorted consumer database:", sorted_db)
        app()

    elif op == 5:
        remove_consumer = str(input("Enter consumer number to remove: "))
        new_consumer_db = []
        for consumer in consumer_db:
            if consumer[0] != remove_consumer:
                new_consumer_db.append(consumer)
        consumer_db = tuple(new_consumer_db)
        print("Consumer database after removing:", consumer_db)
        app()

    elif op == 6:
        consumer_db = ()
        print("Consumer database after removing all consumers:", consumer_db)
        app()

    elif op == 7:
        del consumer_db
        print("Consumer database deleted.")
        app()

    else:
        print("Invalid options selected")
        app()


app()
        
        
        

        
        
