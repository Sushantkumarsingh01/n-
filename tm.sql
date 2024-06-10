
create database tm;
use tm;


-- Create Users table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Role VARCHAR(20) NOT NULL
);

-- Create Routes table
CREATE TABLE Routes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,
    RouteName VARCHAR(100) NOT NULL,
    StartLocation VARCHAR(100) NOT NULL,
    EndLocation VARCHAR(100) NOT NULL
);

-- Create Trips table
CREATE TABLE Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleID INT NOT NULL,
    RouteID INT NOT NULL,
    DepartureDate DATE NOT NULL,
    ArrivalDate DATE NOT NULL,
    TripType VARCHAR(50) NOT NULL,
    MaxPassengers INT NOT NULL,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (RouteID) REFERENCES Routes(RouteID)
);

-- Create Bookings table
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    TripID INT NOT NULL,
    PassengerID INT NOT NULL,
    BookingDate DATE NOT NULL,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (TripID) REFERENCES Trips(TripID),
    FOREIGN KEY (PassengerID) REFERENCES Users(UserID)
);

-- Create Drivers table
CREATE TABLE Drivers (
    DriverID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    LicenseNumber VARCHAR(50) NOT NULL,
    PhoneNumber VARCHAR(20),
    Status VARCHAR(50) NOT NULL
);

INSERT INTO Users (FirstName, LastName, PhoneNumber, Email, Username, Password, Role)
VALUES 
('John', 'Doe', '1234567890', 'john.doe@example.com', 'johndoe', 'password123', 'customer'),
('Alice', 'Smith', '0987654321', 'alice.smith@example.com', 'alicesmith', 'password123', 'customer'),
('Bob', 'Johnson', '5555555555', 'bob.johnson@example.com', 'bobjohnson', 'password123', 'customer'),
('Carol', 'Williams', '4444444444', 'carol.williams@example.com', 'carolwilliams', 'password123', 'customer'),
('David', 'Brown', '3333333333', 'david.brown@example.com', 'davidbrown', 'password123', 'customer'),
('Eve', 'Davis', '2222222222', 'eve.davis@example.com', 'evedavis', 'password123', 'customer'),
('Frank', 'Miller', '1111111111', 'frank.miller@example.com', 'frankmiller', 'password123', 'customer'),
('Grace', 'Wilson', '6666666666', 'grace.wilson@example.com', 'gracewilson', 'password123', 'customer'),
('Henry', 'Moore', '7777777777', 'henry.moore@example.com', 'henrymoore', 'password123', 'admin'),
('Ivy', 'Taylor', '8888888888', 'ivy.taylor@example.com', 'ivytaylor', 'password123', 'admin');



INSERT INTO Routes (RouteName, StartLocation, EndLocation)
VALUES 
('Route 1', 'City A', 'City B'),
('Route 2', 'City B', 'City C'),
('Route 3', 'City C', 'City D'),
('Route 4', 'City D', 'City E'),
('Route 5', 'City E', 'City F'),
('Route 6', 'City F', 'City G'),
('Route 7', 'City G', 'City H'),
('Route 8', 'City H', 'City I'),
('Route 9', 'City I', 'City J'),
('Route 10', 'City J', 'City K');



INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, TripType, MaxPassengers, Status)
VALUES 
(1, 1, '2024-07-01', '2024-07-02', 'Passenger', 50, 'Scheduled'),
(2, 2, '2024-07-03', '2024-07-04', 'Freight', 20, 'Scheduled'),
(3, 3, '2024-07-05', '2024-07-06', 'Passenger', 40, 'Scheduled'),
(4, 4, '2024-07-07', '2024-07-08', 'Freight', 25, 'Scheduled'),
(5, 5, '2024-07-09', '2024-07-10', 'Passenger', 30, 'Scheduled'),
(6, 6, '2024-07-11', '2024-07-12', 'Freight', 15, 'Scheduled'),
(7, 7, '2024-07-13', '2024-07-14', 'Passenger', 35, 'Scheduled'),
(8, 8, '2024-07-15', '2024-07-16', 'Freight', 10, 'Scheduled'),
(9, 9, '2024-07-17', '2024-07-18', 'Passenger', 45, 'Scheduled'),
(10, 10, '2024-07-19', '2024-07-20', 'Freight', 50, 'Scheduled');


INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status)
VALUES 
(1, 1, '2024-06-01', 'Booked'),
(2, 2, '2024-06-02', 'Booked'),
(3, 3, '2024-06-03', 'Booked'),
(4, 4, '2024-06-04', 'Booked'),
(5, 5, '2024-06-05', 'Booked'),
(6, 6, '2024-06-06', 'Booked'),
(7, 7, '2024-06-07', 'Booked'),
(8, 8, '2024-06-08', 'Booked'),
(9, 9, '2024-06-09', 'Booked'),
(10, 10, '2024-06-10', 'Booked');


INSERT INTO Drivers (FirstName, LastName, LicenseNumber, PhoneNumber, Status)
VALUES 
('Jane', 'Smith', 'AB123456', '0987654321', 'Available'),
('Tom', 'Brown', 'CD789012', '0987654322', 'Available'),
('Jerry', 'Wilson', 'EF345678', '0987654323', 'Available'),
('Mike', 'Taylor', 'GH901234', '0987654324', 'Available'),
('Alice', 'Anderson', 'IJ567890', '0987654325', 'Available'),
('Bob', 'Thompson', 'KL123456', '0987654326', 'Available'),
('Charlie', 'Martinez', 'MN789012', '0987654327', 'Available'),
('David', 'Hernandez', 'OP345678', '0987654328', 'Available'),
('Eve', 'Lopez', 'QR901234', '0987654329', 'Available'),
('Frank', 'Gonzalez', 'ST567890', '0987654330', 'Available');





