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
    
    # Counting Rows
    "How do you count the number of employees in the 'employees' table?": "SELECT COUNT(*) FROM employees;",
    "How do you count the number of employees in each department from the 'employees' table?": "SELECT department, COUNT(*) AS number_of_employees FROM employees GROUP BY department;",
    
    # Finding Averages and Summing Values
    "How do you find the average salary of employees in the 'employees' table?": "SELECT AVG(salary) FROM employees;",
    "How do you find the total salary of all employees in the 'employees' table?": "SELECT SUM(salary) FROM employees;",
    
    # Using GROUP BY
    "How do you use GROUP BY to group employees by 'department' and get the average salary for each department?": "SELECT department, AVG(salary) AS avg_salary FROM employees GROUP BY department;",
    "How do you group employees by 'job_title' and count the number of employees in each job title?": "SELECT job_title, COUNT(*) AS number_of_employees FROM employees GROUP BY job_title;",
    
    # Using Subqueries
    "How do you use a subquery to find employees with a salary higher than the average salary?": "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);",
    "How do you use a correlated subquery to find employees who work in the same department as employee_id 123?": "SELECT * FROM employees e1 WHERE EXISTS (SELECT 1 FROM employees e2 WHERE e2.department = e1.department AND e2.employee_id = 123);",
    "How do you use a nested subquery to find departments where the average salary is above 60,000?": "SELECT department FROM employees WHERE (SELECT AVG(salary) FROM employees WHERE department = employees.department) > 60000 GROUP BY department;",
    
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
    "How do you find the total number of employees with a salary greater than 50,000?": "SELECT COUNT(*) FROM employees WHERE salary > 50000;",
    "How do you get the maximum salary for each department?": "SELECT department, MAX(salary) AS max_salary FROM employees GROUP BY department;",
    
    # Basic GROUP BY and Aggregation
    "How do you get the total number of employees hired each year?": "SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS number_of_employees FROM employees GROUP BY YEAR(hire_date);",
    "How do you get the average salary for each job title?": "SELECT job_title, AVG(salary) AS avg_salary FROM employees GROUP BY job_title;",
    "How do you get the total salary paid in each department?": "SELECT department, SUM(salary) AS total_salary FROM employees GROUP BY department;",
}

# Randomize the order of questions and select 20 questions
questions_list = list(questions.items())
random.shuffle(questions_list)
selected_questions = questions_list[:20]

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