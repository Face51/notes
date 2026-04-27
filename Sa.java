
class Student {
    String name;
    int rollNo;
    float marks;

    Student(String n, int r, float m) {
        name = n;
        rollNo = r;
        marks = m;
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("Roll No: " + rollNo);
        System.out.println("Marks: " + marks);
    }
}

public class Main {
    public static void main(String[] args) {
        Student s1 = new Student("Arindam", 1, 85.5f);
        s1.display();
    }
}








class Rectangle {
    double length, width;

    Rectangle(double l, double w) {
        length = l;
        width = w;
    }

    double area() {
        return length * width;
    }

    double perimeter() {
        return 2 * (length + width);
    }
}

public class Main {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(5, 3);

        System.out.println("Area = " + r.area());
        System.out.println("Perimeter = " + r.perimeter());
    }
}














class BankAccount {
    int accountNumber;
    double balance;

    BankAccount(int accNo, double bal) {
        accountNumber = accNo;
        balance = bal;
    }

    void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    void withdraw(double amount) {
        if (amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance");
        }
    }

    void display() {
        System.out.println("Account No: " + accountNumber);
        System.out.println("Balance: " + balance);
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount b = new BankAccount(101, 1000);

        b.deposit(500);
        b.withdraw(200);
        b.display();
    }
}













class Employee {
    String name;
    double salary;

    Employee(String n, double s) {
        name = n;
        salary = s;
    }

    void display() {
        if (salary > 10000) {
            System.out.println("Name: " + name);
            System.out.println("Salary: " + salary);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Employee e1 = new Employee("Rahul", 50000);
        Employee e2 = new Employee("Amit", 8000);

        e1.display();
        e2.display();
    }
}









