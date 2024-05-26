CREATE DATABASE EMS;
USE EMS;


-- Create the Employee table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    JobTitle VARCHAR(50),
    Department VARCHAR(50),
    Email VARCHAR(100)
);

-- Create the Client table
CREATE TABLE Client (
    ClientID INT PRIMARY KEY,
    ClientName VARCHAR(100),
    ContactPerson VARCHAR(100),
    ContactEmail VARCHAR(100),
    ContactPhone VARCHAR(15)
);

-- Create the Project table
CREATE TABLE Project (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100),
    ClientID INT,
    EmployeeID INT,
    StartDate DATE,
    EndDate DATE,
    FOREIGN KEY (ClientID) REFERENCES Client(ClientID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Create the Time_Report table
CREATE TABLE Time_Report (
    TimeReportID INT PRIMARY KEY,
    EmployeeID INT,
    ProjectID INT,
    DateWorked DATE,
    HoursWorked DECIMAL(5,2),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (ProjectID) REFERENCES Project(ProjectID)
);

-- Insert data into Employee table
INSERT INTO Employee (EmployeeID, FirstName, LastName, JobTitle, Department, Email)
VALUES 
(1, 'Aseem', 'Rafiq', 'Data Engineer', 'Engineering', 'aseemrafique@gmail.com'),
(2, 'Ali', 'Usama', 'Project Manager', 'Management', 'ali.usama@gmail.com'),
(3, 'Ahmad', 'Ali', 'QA Engineer', 'Quality Assurance', 'ahmad.ali@gmail.com');

-- Insert data into Client table
INSERT INTO Client (ClientID, ClientName, ContactPerson, ContactEmail, ContactPhone)
VALUES 
(1, 'Tech Solutions', 'Samuel Eden', 'samuel.eden@techsolutions.com', '123-456-7890'),
(2, 'Business Corp', 'Steve Harrington', 'steveharrington@businesscorp.com', '234-567-8901');

-- Insert data into Project table
INSERT INTO Project (ProjectID, ProjectName, ClientID, EmployeeID, StartDate, EndDate)
VALUES 
(1, 'Website Development', 1, 1, '2024-01-01', '2024-06-30'),
(2, 'Mobile App', 1, 2, '2024-02-01', '2024-07-31'),
(3, 'System Upgrade', 2, 3, '2024-03-01', '2024-08-31');

-- Insert data into Time_Report table
INSERT INTO Time_Report (TimeReportID, EmployeeID, ProjectID, DateWorked, HoursWorked)
VALUES 
(1, 1, 1, '2024-01-02', 8.0),
(2, 1, 1, '2024-01-03', 7.5),
(3, 2, 2, '2024-02-02', 8.0),
(4, 2, 2, '2024-02-03', 8.0),
(5, 3, 3, '2024-03-05', 7.0),
(6, 3, 3, '2024-03-06', 8.0);


--CRUD OPERATIONS

--Insert a new Employee
INSERT INTO Employee (EmployeeID, FirstName, LastName, JobTitle, Department, Email)
VALUES (4, 'Zohaib', 'Naveed', 'Data Analyst', 'Analytics', 'zohaib.naveed@gmail.com');


--Insert a new Client
INSERT INTO Client (ClientID, ClientName, ContactPerson, ContactEmail, ContactPhone)
VALUES (3, 'Innovative Solutions', 'Charlie Parker', 'charlie.parker@innovativesolutions.com', '345-678-9012');


--Insert a new Project
INSERT INTO Project (ProjectID, ProjectName, ClientID, EmployeeID, StartDate, EndDate)
VALUES (4, 'AI Research', 3, 4, '2024-04-01', '2024-12-31');


--Insert a new time report
INSERT INTO Time_Report (TimeReportID, EmployeeID, ProjectID, DateWorked, HoursWorked)
VALUES (7, 4, 4, '2024-04-02', 8.0);


--Read Operations
SELECT * FROM Employee;

SELECT * FROM Project WHERE EmployeeID = 1;

SELECT * FROM Time_Report WHERE ProjectID = 1;

--Select all Projects along with Client details
SELECT 
    p.ProjectID, 
    p.ProjectName, 
    c.ClientName, 
    c.ContactPerson, 
    p.StartDate, 
    p.EndDate 
FROM Project AS p
INNER JOIN Client AS c 
ON p.ClientID = c.ClientID;


--Update operations
UPDATE Employee
SET JobTitle = 'Senior Software Engineer'
WHERE EmployeeID = 1;


UPDATE Client
SET ContactEmail = 'alice.j.newemail@techsolutions.com', ContactPhone = '987-654-3210'
WHERE ClientID = 1;


UPDATE Project
SET EndDate = '2024-07-15'
WHERE ProjectID = 1;


UPDATE Time_Report
SET HoursWorked = 7.5
WHERE TimeReportID = 1;


--Delete Operations
DELETE FROM Employee
WHERE EmployeeID = 4;

DELETE FROM Client
WHERE ClientID = 3;

DELETE FROM Project
WHERE ProjectID = 4;

DELETE FROM Time_Report
WHERE TimeReportID = 7;


