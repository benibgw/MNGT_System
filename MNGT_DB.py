import sqlite3

MNGT_DB = sqlite3.connect('MNGT_DB.db')

cursor = MNGT_DB.cursor()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS accessList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            accessCode INTEGER NOT NULL,
            accessKey TEXT NOT NULL,
            accessLevel TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            cpf TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            address TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employeeList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            cpf TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            position TEXT NOT NULL,
            salary REAL NOT NULL,
            address TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS productList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS salesList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            total_price REAL NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clientList(id),
            FOREIGN KEY (employee_id) REFERENCES employeeList(id),
            FOREIGN KEY (product_id) REFERENCES productList(id)
    )
''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS serviceList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            service_type TEXT NOT NULL,
            service_price REAL NOT NULL,
            service_date TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clientList(id),
            FOREIGN KEY (employee_id) REFERENCES employeeList(id)
    )
''')

def create_access(accessCode, accessKey, accessLevel):
    cursor.execute('''
        INSERT INTO accessList (accessCode, accessKey, accessLevel)
        VALUES (:accessCode, :accessKey, :accessLevel)''',
        {'accessCode': accessCode, 'accessKey': accessKey, 'accessLevel': accessLevel})
    MNGT_DB.commit()

def register_client(name, age, cpf, email, phone, address):
    cursor.execute('''
        INSERT INTO clientList (name, age, cpf, email, phone, address)
        VALUES (:name, :age, :cpf, :email, :phone, :address)''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone, 'address': address})
    MNGT_DB.commit()
    
def register_employee(name, age, cpf, email, phone, position, salary, address):
    cursor.execute('''
        INSERT INTO employeeList (name, age, cpf, email, phone, position, salary, address)
        VALUES (:name, :age, :cpf, :email, :phone, :position, :salary, :address)''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone,
         'position': position, 'salary': salary, 'address': address})
    MNGT_DB.commit()
    
def register_product(name, price, quantity):
    cursor.execute('''
        INSERT INTO productList (name, price, quantity)
        VALUES (:name, :price, :quantity)''',
        {'name': name, 'price': price, 'quantity': quantity})
    MNGT_DB.commit()
    
def register_sale(client_id, employee_id, product_id, quantity, total_price, date):
    cursor.execute('''
        INSERT INTO salesList (client_id, employee_id, product_id, quantity, total_price, date)
        VALUES (:client_id, :employee_id, :product_id, :quantity, :total_price, :date)''',
        {'client_id': client_id, 'employee_id': employee_id, 'product_id': product_id,
         'quantity': quantity, 'total_price': total_price, 'date': date})
    MNGT_DB.commit()
    
def register_service(client_id, employee_id, service_type, service_price, service_date):
    cursor.execute('''
        INSERT INTO serviceList (client_id, employee_id, service_type, service_price, service_date)
        VALUES (:client_id, :employee_id, :service_type, :service_price, :service_date)''',
        {'client_id': client_id, 'employee_id': employee_id,
         'service_type': service_type, 'service_price': service_price,
         'service_date': service_date})
    MNGT_DB.commit()
    
def edit_access(accessCode, accessKey, accessLevel, id):
    cursor.execute('''
        UPDATE accessList
        SET accessCode = :accessCode,
            accessKey = :accessKey,
            accessLevel = :accessLevel
        WHERE id = :id''',
        {'accessCode': accessCode, 'accessKey': accessKey, 'accessLevel': accessLevel, 'id': id})
    MNGT_DB.commit()
    
def edit_client(name, age, cpf, email, phone, address, id):
    cursor.execute('''
        UPDATE clientList
        SET name = :name,
            age = :age,
            cpf = :cpf,
            email = :email,
            phone = :phone,
            address = :address
        WHERE id = :id''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone, 'address': address, 'id': id})
    MNGT_DB.commit()
    
def edit_employee(name, age, cpf, email, phone, position, salary, address, id):
    cursor.execute('''
        UPDATE employeeList
        SET name = :name,
            age = :age,
            cpf = :cpf,
            email = :email,
            phone = :phone,
            position = :position,
            salary = :salary,
            address = :address
        WHERE id = :id''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone,
         'position': position, 'salary': salary, 'address': address, 'id': id})
    MNGT_DB.commit()
    
def edit_product(name, price, quantity, id):
    cursor.execute('''
        UPDATE productList
        SET name = :name,
            price = :price,
            quantity = :quantity
        WHERE id = :id''',
        {'name': name, 'price': price, 'quantity': quantity, 'id': id})
    MNGT_DB.commit()
    
def edit_sale(client_id, employee_id, product_id, quantity, total_price, date, id):
    cursor.execute('''
        UPDATE salesList
        SET client_id = :client_id,
            employee_id = :employee_id,
            product_id = :product_id,
            quantity = :quantity,
            total_price = :total_price,
            date = :date
        WHERE id = :id''',
        {'client_id': client_id, 'employee_id': employee_id, 'product_id': product_id,
         'quantity': quantity, 'total_price': total_price, 'date': date, 'id': id})
    MNGT_DB.commit()
    
def edit_service(client_id, employee_id, service_type, service_price, service_date, id):
    cursor.execute('''
        UPDATE serviceList
        SET client_id = :client_id,
            employee_id = :employee_id,
            service_type = :service_type,
            service_price = :service_price,
            service_date = :service_date
        WHERE id = :id''',
        {'client_id': client_id, 'employee_id': employee_id,
         'service_type': service_type, 'service_price': service_price,
         'service_date': service_date, 'id': id})
    MNGT_DB.commit()
    
def delete_access(id):
    cursor.execute('''
        DELETE FROM accessList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()
    
def delete_client(id):
    cursor.execute('''
        DELETE FROM clientList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()
    
def delete_employee(id):
    cursor.execute('''
        DELETE FROM employeeList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()

def delete_product(id):
    cursor.execute('''
        DELETE FROM productList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()
    
def delete_sale(id):
    cursor.execute('''
        DELETE FROM salesList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()
    
def delete_service(id):
    cursor.execute('''
        DELETE FROM serviceList
        WHERE id = :id''',
        {'id': id})
    MNGT_DB.commit()
    
def get_all_acccess():
    cursor.execute('SELECT * FROM accessList')
    return cursor.fetchall()

def get_all_clients():
    cursor.execute('SELECT * FROM clientList')
    return cursor.fetchall()

def get_all_employees():
    cursor.execute('SELECT * FROM employeeList')
    return cursor.fetchall()

def get_all_products():
    cursor.execute('SELECT * FROM productList')
    return cursor.fetchall()

def get_all_sales():
    cursor.execute('SELECT * FROM salesList')
    return cursor.fetchall()

def get_all_services():
    cursor.execute('SELECT * FROM serviceList')
    return cursor.fetchall()

def check_access(accessCode, accessKey):
    cursor.execute('''
        SELECT * FROM accessList
        WHERE accessCode = :accessCode AND accessKey = :accessKey''',
        {'accessCode': accessCode, 'accessKey': accessKey})
    return cursor.fetchone()

MNGT_DB.commit()
