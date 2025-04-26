import sqlite3

MNGT_DB = sqlite3.connect('MNGT_DB.db')

cursor = MNGT_DB.cursor()

cursor.execute('''
     CREATE TABLE IF NOT EXISTS acessList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            acessCode INTEGER NOT NULL,
            acessKey TEXT NOT NULL,
            acessLevel TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            cpf REAL NOT NULL,
            email TEXT NOT NULL,
            phone INTEGER NOT NULL,
            address TEXT NOT NULL
    )
''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS employeeList (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            cpf REAL NOT NULL,
            email TEXT NOT NULL,
            phone INTEGER NOT NULL,
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

def create_acess(acessCode, acessKey, acessLevel):
    cursor.execute('''
        INSERT INTO acessList (acessCode, acessKey, acessLevel)
        VALUES (:acessCode, :acessKey, :acessLevel)''',
        {'acessCode': acessCode, 'acessKey': acessKey, 'acessLevel': acessLevel})

def register_client(name, age, cpf, email, phone, address):
    cursor.execute('''
        INSERT INTO clientList (name, age, cpf, email, phone, address)
        VALUES (:name, :age, :cpf, :email, :phone, :address)''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone, 'address': address})
    
def register_employee(name, age, cpf, email, phone, position, salary, address):
    cursor.execute('''
        INSERT INTO employeeList (name, age, cpf, email, phone, position, salary, address)
        VALUES (:name, :age, :cpf, :email, :phone, :position, :salary, :address)''',
        {'name': name, 'age': age, 'cpf': cpf, 'email': email, 'phone': phone,
         'position': position, 'salary': salary, 'address': address})
    
def register_product(name, price, quantity):
    cursor.execute('''
        INSERT INTO productList (name, price, quantity)
        VALUES (:name, :price, :quantity)''',
        {'name': name, 'price': price, 'quantity': quantity})
    
def register_sale(client_id, employee_id, product_id, quantity, total_price, date):
    cursor.execute('''
        INSERT INTO salesList (client_id, employee_id, product_id, quantity, total_price, date)
        VALUES (:client_id, :employee_id, :product_id, :quantity, :total_price, :date)''',
        {'client_id': client_id, 'employee_id': employee_id, 'product_id': product_id,
         'quantity': quantity, 'total_price': total_price, 'date': date})
    
def register_service(client_id, employee_id, service_type, service_price, service_date):
    cursor.execute('''
        INSERT INTO serviceList (client_id, employee_id, service_type, service_price, service_date)
        VALUES (:client_id, :employee_id, :service_type, :service_price, :service_date)''',
        {'client_id': client_id, 'employee_id': employee_id,
         'service_type': service_type, 'service_price': service_price,
         'service_date': service_date})
    
def edit_acess(acessCode, acessKey, acessLevel, id):
    cursor.execute('''
        UPDATE acessList
        SET acessCode = :acessCode,
            acessKey = :acessKey,
            acessLevel = :acessLevel
        WHERE id = :id''',
        {'acessCode': acessCode, 'acessKey': acessKey, 'acessLevel': acessLevel, 'id': id})
    
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
    
def edit_product(name, price, quantity, id):
    cursor.execute('''
        UPDATE productList
        SET name = :name,
            price = :price,
            quantity = :quantity
        WHERE id = :id''',
        {'name': name, 'price': price, 'quantity': quantity, 'id': id})
    
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
    
def delete_acess(id):
    cursor.execute('''
        DELETE FROM acessList
        WHERE id = :id''',
        {'id': id})
    
def delete_client(id):
    cursor.execute('''
        DELETE FROM clientList
        WHERE id = :id''',
        {'id': id})
    
def delete_employee(id):
    cursor.execute('''
        DELETE FROM employeeList
        WHERE id = :id''',
        {'id': id})

def delete_product(id):
    cursor.execute('''
        DELETE FROM productList
        WHERE id = :id''',
        {'id': id})
    
def delete_sale(id):
    cursor.execute('''
        DELETE FROM salesList
        WHERE id = :id''',
        {'id': id})
    
def delete_service(id):
    cursor.execute('''
        DELETE FROM serviceList
        WHERE id = :id''',
        {'id': id})
    
def get_all_access():
    cursor.execute('SELECT * FROM acessList')
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

MNGT_DB.commit()
