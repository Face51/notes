import random

# Define the questions and correct answers
questions = {
    # Basic SELECT Queries
    "How do you retrieve all columns from a table named 'employees'?": "SELECT * FROM employees;",
    "How do you select only the 'first_name' and 'last_name' columns from the 'employees' table?": "SELECT first_name, last_name FROM employees;",
    "How do you select all employees with their job titles from the 'employees' table?": "SELECT first_name, last_name, job_title FROM employees;",
    "How do you select the top 5 highest salaries from the 'employees' table?": "SELECT salary FROM employees ORDER BY salary DESC LIMIT 5;",
    "How do you retrieve all rows from the 'employees' table, but only the columns 'first_name', 'last_name', and 'salary'?": "SELECT first_name, last_name, salary FROM employees;",
    "How do you select all employees who are managers and sort them by their last names in ascending order?": "SELECT * FROM employees WHERE job_title = 'Manager' ORDER BY last_name ASC;",

    # Retrieving Distinct Values
    "How do you select distinct values from the 'department' column in the 'employees' table?": "SELECT DISTINCT department FROM employees;",
    "How do you find unique job titles from the 'employees' table?": "SELECT DISTINCT job_title FROM employees;",
    "How do you retrieve distinct combinations of 'department' and 'job_title' from the 'employees' table?": "SELECT DISTINCT department, job_title FROM employees;",
    "How do you select unique employee salaries from the 'employees' table?": "SELECT DISTINCT salary FROM employees;",

    # Using WHERE Clause
    "How do you filter the results to show only employees with a 'department' of 'Sales'?": "SELECT * FROM employees WHERE department = 'Sales';",
    "How do you find employees whose 'hire_date' is after January 1, 2020?": "SELECT * FROM employees WHERE hire_date > '2020-01-01';",
    "How do you select employees whose 'salary' is not equal to 60,000?": "SELECT * FROM employees WHERE salary <> 60000;",
    "How do you find employees whose 'first_name' is either 'John' or 'Jane'?": "SELECT * FROM employees WHERE first_name IN ('John', 'Jane');",

    # Filtering with Multiple Conditions
    "How do you select employees who have a 'salary' greater than 50,000 and work in the 'Sales' department?": "SELECT * FROM employees WHERE salary > 50000 AND department = 'Sales';",
    "How do you find employees who have a 'salary' less than 40,000 or who were hired before January 1, 2015?": "SELECT * FROM employees WHERE salary < 40000 OR hire_date < '2015-01-01';",
    "How do you find employees who have a 'salary' between 40,000 and 60,000 and work in either 'Sales' or 'HR'?": "SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000 AND department IN ('Sales', 'HR');",

    # Pattern Matching with LIKE
    "How do you find employees whose first name starts with 'J'?": "SELECT * FROM employees WHERE first_name LIKE 'J%';",
    "How do you find employees whose last name ends with 'son'?": "SELECT * FROM employees WHERE last_name LIKE '%son';",
    "How do you select employees whose first name contains 'ann'?": "SELECT * FROM employees WHERE first_name LIKE '%ann%';",

    # Filtering with IN and BETWEEN
    "How do you select employees who work in departments 'Sales' or 'HR'?": "SELECT * FROM employees WHERE department IN ('Sales', 'HR');",
    "How do you select employees who were hired between January 1, 2020 and December 31, 2020?": "SELECT * FROM employees WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31';",
    "How do you select employees with salaries within the range of 30,000 to 50,000?": "SELECT * FROM employees WHERE salary BETWEEN 30000 AND 50000;",

    # Sorting with ORDER BY
    "How do you sort the results of the 'employees' table by 'last_name' in ascending order?": "SELECT * FROM employees ORDER BY last_name ASC;",
    "How do you sort the results of the 'employees' table by 'salary' in descending order?": "SELECT * FROM employees ORDER BY salary DESC;",
    "How do you retrieve employees ordered by 'hire_date' in descending order and 'last_name' in ascending order?": "SELECT * FROM employees ORDER BY hire_date DESC, last_name ASC;",

    # Finding Averages and Summing Values
    "How do you find the average salary of employees in the 'employees' table?": "SELECT AVG(salary) FROM employees;",
    "How do you find the total salary of all employees in the 'employees' table?": "SELECT SUM(salary) FROM employees;",

    # Inserting New Records
    "How do you insert a new record into the 'employees' table with 'first_name' as 'John', 'last_name' as 'Doe', and 'salary' as 55000?": "INSERT INTO employees (first_name, last_name, salary) VALUES ('John', 'Doe', 55000);",
    "How do you insert multiple new records into the 'employees' table?": "INSERT INTO employees (first_name, last_name, salary) VALUES ('Alice', 'Smith', 50000), ('Bob', 'Johnson', 60000);",
    "How do you insert a new employee with all details including 'hire_date'?": "INSERT INTO employees (first_name, last_name, job_title, department, salary, hire_date) VALUES ('Sarah', 'Connor', 'Analyst', 'Finance', 70000, '2021-05-10');",
    "How do you insert a record while providing default values for some columns?": "INSERT INTO employees (first_name, last_name) VALUES ('Mark', 'Twain');",
    "How do you insert a new record for an employee with 'employee_id' auto-generated?": "INSERT INTO employees (first_name, last_name, job_title, department, salary) VALUES ('Laura', 'Ingalls', 'Developer', 'IT', 75000);",

    # Updating Existing Records
    "How do you update the 'job_title' of an employee with 'employee_id' 123 to 'Senior Developer'?": "UPDATE employees SET job_title = 'Senior Developer' WHERE employee_id = 123;",
    "How do you increase the salary of all employees by 5%?": "UPDATE employees SET salary = salary * 1.05;",
    "How do you update the department of all employees with 'job_title' 'Intern' to 'Temporary'?": "UPDATE employees SET department = 'Temporary' WHERE job_title = 'Intern';",
    "How do you set the 'salary' of all employees in the 'IT' department to 80,000?": "UPDATE employees SET salary = 80000 WHERE department = 'IT';",
    "How do you change the 'hire_date' of an employee with 'employee_id' 456 to '2023-01-01'?": "UPDATE employees SET hire_date = '2023-01-01' WHERE employee_id = 456;",

    # Deleting Records
    "How do you delete all employees from the 'employees' table who have a 'hire_date' before January 1, 2020?": "DELETE FROM employees WHERE hire_date < '2020-01-01';",
    "How do you delete employees from the 'employees' table who have a salary less than 30,000?": "DELETE FROM employees WHERE salary < 30000;",
    "How do you delete employees with 'job_title' 'Contractor'?": "DELETE FROM employees WHERE job_title = 'Contractor';",
    "How do you delete records of employees who have not updated their details in the last year?": "DELETE FROM employees WHERE last_updated < DATE_SUB(CURDATE(), INTERVAL 1 YEAR);",

    # Additional Basic SELECT Queries
    "How do you select employees who have a 'salary' between 40,000 and 60,000?": "SELECT * FROM employees WHERE salary BETWEEN 40000 AND 60000;",
    "How do you retrieve all employees sorted by 'hire_date' in ascending order?": "SELECT * FROM employees ORDER BY hire_date ASC;",
    "How do you find employees whose 'job_title' starts with 'Senior'?": "SELECT * FROM employees WHERE job_title LIKE 'Senior%';",

    # Additional Aggregation
    "How do you find the highest salary among employees?": "SELECT MAX(salary) FROM employees;",
    "How do you find the lowest salary among employees?": "SELECT MIN(salary) FROM employees;",
  #  "How do you find the total number of employees with a salary greater than 50,000?": "SELECT COUNT(*) FROM employees WHERE salary > 50000;",
    "How do you get the maximum salary for each department?": "SELECT department, MAX(salary) AS max_salary FROM employees GROUP BY department;",

    # ALTER TABLE COMMANDS
    "Add a new column 'birthdate' to the 'employees' table": "ALTER TABLE employees ADD birthdate DATE;",  # Adds a new column 'birthdate' with DATE type to the 'employees' table
    "Drop an existing column 'middle_name' from the 'employees' table": "ALTER TABLE employees DROP COLUMN middle_name;",  # Drops the 'middle_name' column from the 'employees' table
    "Modify the 'salary' column data type to DECIMAL(10, 2) in the 'employees' table": "ALTER TABLE employees MODIFY salary DECIMAL(10, 2);",  # Modifies the 'salary' column to have DECIMAL(10, 2) type in the 'employees' table
    "Rename the column 'emp_name' to 'employee_name' in the 'employees' table": "ALTER TABLE employees RENAME COLUMN emp_name TO employee_name;",  # Renames the column 'emp_name' to 'employee_name' in the 'employees' table
    "Add a default value 'active' to the 'status' column in the 'employees' table": "ALTER TABLE employees ALTER COLUMN status SET DEFAULT 'active';",  # Sets a default value 'active' for the 'status' column in the 'employees' table
    "Set the 'email' column to NOT NULL in the 'employees' table": "ALTER TABLE employees MODIFY email VARCHAR(255) NOT NULL;",  # Sets the 'email' column to NOT NULL in the 'employees' table
    "Drop the constraint 'emp_check' from the 'employees' table": "ALTER TABLE employees DROP CONSTRAINT emp_check;",  # Drops the constraint 'emp_check' from the 'employees' table
    "Add a constraint 'chk_age' to ensure 'age' is at least 18 in the 'employees' table": "ALTER TABLE employees ADD CONSTRAINT chk_age CHECK (age >= 18);",  # Adds a constraint 'chk_age' to ensure 'age' is at least 18 in the 'employees' table
    "Change the column 'phone_number' to 'phone' in the 'employees' table": "ALTER TABLE employees CHANGE COLUMN phone_number phone VARCHAR(15);",  # Changes the column name from 'phone_number' to 'phone' in the 'employees' table
    "Add a unique index to the 'email' column in the 'employees' table": "ALTER TABLE employees ADD UNIQUE (email);",  # Adds a unique index to the 'email' column in the 'employees' table
    "Add a new column 'hire_date' to the 'employees' table": "ALTER TABLE employees ADD hire_date DATE;",  # Adds a new column 'hire_date' with DATE type to the 'employees' table
    "Modify 'job_title' column to allow 100 characters in the 'employees' table": "ALTER TABLE employees MODIFY job_title VARCHAR(100);",  # Modifies 'job_title' column to allow 100 characters in the 'employees' table
    "Add a CHECK constraint to ensure 'salary' is positive in the 'employees' table": "ALTER TABLE employees ADD CONSTRAINT chk_salary CHECK (salary > 0);",  # Adds a CHECK constraint to ensure 'salary' is positive in the 'employees' table
    "Drop the column 'emergency_contact' from the 'employees' table": "ALTER TABLE employees DROP COLUMN emergency_contact;",  # Drops the 'emergency_contact' column from the 'employees' table
    "Change the data type of 'age' to INTEGER in the 'employees' table": "ALTER TABLE employees MODIFY age INTEGER;",  # Changes the data type of 'age' to INTEGER in the 'employees' table
    "Add an index to the 'last_name' column in the 'employees' table": "ALTER TABLE employees ADD INDEX idx_last_name (last_name);",  # Adds an index to the 'last_name' column in the 'employees' table

    # RENAME COMMANDS
    "Rename the 'employees' table to 'staff'": "RENAME TABLE employees TO staff;",  # Renames the 'employees' table to 'staff'
    "Rename the column 'address' to 'home_address' in the 'employees' table": "ALTER TABLE employees RENAME COLUMN address TO home_address;",  # Renames the column 'address' to 'home_address' in the 'employees' table
    "Rename the database from 'old_db' to 'new_db'": "RENAME DATABASE old_db TO new_db;",  # Renames the database from 'old_db' to 'new_db'
    "Rename the 'employees' table to 'workers' in MySQL": "RENAME TABLE employees TO workers;",  # Renames the 'employees' table to 'workers' in MySQL

    # ADD PRIMARY KEY
    "Add a primary key to the 'employee_id' column in the 'employees' table": "ALTER TABLE employees ADD PRIMARY KEY (employee_id);",  # Adds a primary key constraint to the 'employee_id' column in the 'employees' table
    "Add a primary key to the 'id' column in the 'departments' table": "ALTER TABLE departments ADD PRIMARY KEY (id);",  # Adds a primary key constraint to the 'id' column in the 'departments' table

    # UPDATE COMMANDS
    "Update the 'salary' to 60000 for the employee with ID 1": "UPDATE employees SET salary = 60000 WHERE employee_id = 1;",  # Updates the 'salary' to 60000 for the employee with ID 1
    "Update 'salary' to 65000 and 'position' to 'Senior Developer' for the employee with ID 2": "UPDATE employees SET salary = 65000, position = 'Senior Developer' WHERE employee_id = 2;",  # Updates 'salary' to 65000 and 'position' to 'Senior Developer' for the employee with ID 2
    "Update 'salary' to 70000 for employees in the 'IT' department using a join": "UPDATE employees e JOIN departments d ON e.department_id = d.department_id SET e.salary = 70000 WHERE d.department_name = 'IT';",  # Updates 'salary' to 70000 for employees in the 'IT' department using a join
    "Update 'salary' to the average salary for employees with department ID 3 using a subquery": "UPDATE employees SET salary = (SELECT AVG(salary) FROM employees) WHERE department_id = 3;",  # Updates 'salary' to the average salary for employees with department ID 3 using a subquery
    "Update 'status' to 'inactive' where 'end_date' is less than the current date": "UPDATE employees SET status = 'inactive' WHERE end_date < CURDATE();",  # Updates 'status' to 'inactive' where 'end_date' is less than the current date
    "Increment 'salary' by 5% for employees with 'Excellent' performance rating": "UPDATE employees SET salary = salary * 1.05 WHERE performance_rating = 'Excellent';",  # Increments 'salary' by 5% for employees with 'Excellent' performance rating
    "Update 'email' to concatenate 'employee_name' with '@example.com' where 'email' is NULL": "UPDATE employees SET email = CONCAT(employee_name, '@example.com') WHERE email IS NULL;",  # Updates 'email' to concatenate 'employee_name' with '@example.com' where 'email' is NULL
    "Update 'status' based on 'age': 'Junior' if age < 30, 'Mid' if age between 30 and 50, 'Senior' otherwise": "UPDATE employees SET status = CASE WHEN age < 30 THEN 'Junior' WHEN age BETWEEN 30 AND 50 THEN 'Mid' ELSE 'Senior' END;",  # Updates 'status' based on 'age': 'Junior' if age < 30, 'Mid' if age between 30 and 50, 'Senior' otherwise
    "Update 'promotion_date' to the current date for the employee with ID 5": "UPDATE employees SET promotion_date = CURDATE() WHERE employee_id = 5;",  # Updates 'promotion_date' to the current date for the employee with ID 5
    "Update 'department_id' to 10 with a limit of 5 rows": "UPDATE employees SET department_id = 10 LIMIT 5;"  # Updates 'department_id' to 10 with a limit of 5 rows
}



# Randomize the order of questions and select 10 questions
questions_list = list(questions.items())
random.shuffle(questions_list)
selected_questions = questions_list[:10]

# Initialize score and total questions
score = 0
total_questions = len(selected_questions)

# Ask each question and check the answer
for question, correct_answer in selected_questions:
    user_answer = input(f"\n{question}\nYour answer: ").strip()
    if user_answer.lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is:\n{correct_answer}\n")

print(f"\nYour final score: {score} out of {total_questions}")
