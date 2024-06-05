CREATE DATABASE IF NOT EXISTS TransportManagement;

USE TransportManagement;


CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    Model VARCHAR(255) NOT NULL,
    Capacity DECIMAL(10, 2) NOT NULL,
    Type VARCHAR(50) NOT NULL,
    Status VARCHAR(50) NOT NULL
);
SELECT * FROM  Vehicles;



CREATE TABLE Routes (
    RouteID INT AUTO_INCREMENT PRIMARY KEY,
    StartDestination VARCHAR(255) NOT NULL,
    EndDestination VARCHAR(255) NOT NULL,
    Distance DECIMAL(10, 2) NOT NULL
);
SELECT * FROM  Routes;


CREATE TABLE Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleID INT,
    RouteID INT,
    DepartureDate DATETIME NOT NULL,
    ArrivalDate DATETIME NOT NULL,
    Status VARCHAR(50) NOT NULL,
    TripType VARCHAR(50) DEFAULT 'Freight',
    MaxPassengers INT,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (RouteID) REFERENCES Routes(RouteID)
);
 SELECT * FROM  Trips;


CREATE TABLE Passengers (
    PassengerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    Gender VARCHAR(255) NOT NULL,
    Age INT NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(50) NOT NULL
);
SELECT * FROM  Pasengers;



CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    TripID INT,
    PassengerID INT,
    BookingDate DATETIME NOT NULL,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (TripID) REFERENCES Trips(TripID),
    FOREIGN KEY (PassengerID) REFERENCES Passengers(PassengerID)
);
SELECT * FROM  Bookings;


INSERT INTO Vehicles (Model, Capacity, Type, Status) VALUES
('Volvo XC90', 7.50, 'SUV', 'Active'),
('Ford Transit', 12.00, 'Van', 'Active'),
('Mercedes-Benz C-Class', 5.00, 'Sedan', 'Active'),
('Tesla Model S', 5.00, 'Sedan', 'Unactive'),
('BMW X5', 7.00, 'SUV', 'Active'),
('Audi Q7', 7.50, 'SUV', 'Active'),
('Honda Accord', 5.00, 'Sedan', 'Unactive'),
('Chevrolet Tahoe', 8.00, 'SUV', 'Active'),
('Toyota Camry', 5.00, 'Sedan', 'Active'),
('Nissan Altima', 5.00, 'Sedan', 'Unactive');


INSERT INTO Routes (StartDestination, EndDestination, Distance) VALUES
('New York', 'Los Angeles', 4500.00),
('San Francisco', 'Las Vegas', 650.00),
('Miami', 'Orlando', 350.00),
('Houston', 'Dallas', 385.00),
('Chicago', 'Detroit', 380.00),
('Atlanta', 'Charlotte', 245.00),
('Seattle', 'Portland', 280.00),
('Boston', 'New York', 340.00),
('Philadelphia', 'Washington D.C.', 225.00),
('Denver', 'Salt Lake City', 600.00);


INSERT INTO Trips (VehicleID, RouteID, DepartureDate, ArrivalDate, Status, TripType, MaxPassengers) VALUES
(1, 1, '2024-06-01 08:00:00', '2024-06-03 18:00:00', 'Scheduled', 'Passenger', 5),
(2, 2, '2024-06-02 09:00:00', '2024-06-02 17:00:00', 'Scheduled', 'Freight', 0),
(3, 3, '2024-06-03 10:00:00', '2024-06-03 14:00:00', 'Scheduled', 'Passenger', 4),
(4, 4, '2024-06-04 07:00:00', '2024-06-04 12:00:00', 'Scheduled', 'Freight', 0),
(5, 5, '2024-06-05 08:00:00', '2024-06-05 13:00:00', 'Scheduled', 'Passenger', 6),
(6, 6, '2024-06-06 09:00:00', '2024-06-06 11:00:00', 'Scheduled', 'Freight', 0),
(7, 7, '2024-06-07 08:00:00', '2024-06-07 12:00:00', 'Scheduled', 'Passenger', 4),
(8, 8, '2024-06-08 09:00:00', '2024-06-08 15:00:00', 'Scheduled', 'Freight', 0),
(9, 9, '2024-06-09 10:00:00', '2024-06-09 12:00:00', 'Scheduled', 'Passenger', 3),
(10, 10, '2024-06-10 07:00:00', '2024-06-10 13:00:00', 'Scheduled', 'Freight', 0);


INSERT INTO Passengers (FirstName, Gender, Age, Email, PhoneNumber) VALUES
('Amit Kumar', 'Male', 30, 'amit.kumar@example.com', '123-456-7890'),
('Priya Sharma', 'Female', 25, 'priya.sharma@example.com', '234-567-8901'),
('Rajesh Singh', 'Male', 28, 'rajesh.singh@example.com', '345-678-9012'),
('Anita Gupta', 'Female', 35, 'anita.gupta@example.com', '456-789-0123'),
('Vikram Rao', 'Male', 32, 'vikram.rao@example.com', '567-890-1234'),
('Sneha Patel', 'Female', 29, 'sneha.patel@example.com', '678-901-2345'),
('Arjun Mehta', 'Male', 27, 'arjun.mehta@example.com', '789-012-3456'),
('Lakshmi Iyer', 'Female', 31, 'lakshmi.iyer@example.com', '890-123-4567'),
('Karan Desai', 'Male', 26, 'karan.desai@example.com', '901-234-5678'),
('Neha Reddy', 'Female', 24, 'neha.reddy@example.com', '012-345-6789');



INSERT INTO Bookings (TripID, PassengerID, BookingDate, Status) VALUES
(1, 1, '2024-05-01 10:00:00', 'Confirmed'),
(1, 2, '2024-05-01 11:00:00', 'Confirmed'),
(1, 3, '2024-05-01 12:00:00', 'Confirmed'),
(3, 4, '2024-05-02 10:00:00', 'Notconfirmed'),
(3, 5, '2024-05-02 11:00:00', 'Confirmed'),
(5, 6, '2024-05-03 10:00:00', 'Confirmed'),
(7, 7, '2024-05-04 10:00:00', 'Confirmed'),
(7, 8, '2024-05-04 11:00:00', 'Notconfirmed'),
(9, 9, '2024-05-05 10:00:00', 'Confirmed'),
(9, 10, '2024-05-05 11:00:00', 'Confirmed');
