![Python](https://img.shields.io/badge/Python-3.x-blue)

![License](https://img.shields.io/badge/License-MIT-green)

![Project Status](https://img.shields.io/badge/Status-In%20Progress-yellow)


# 🚆 Railway Ticket Booking System

A comprehensive **Python-based Railway Ticket Booking System** that simulates the complete train reservation process. The application allows users to create accounts, log in, book train tickets, select coaches and seats, calculate fares, view booking history, and cancel reservations. Passenger and ticket information is stored using file handling, making the system a practical example of a real-world reservation application built with core Python concepts.

---

## 📖 Project Overview

This project is designed to replicate the basic functionality of an online railway reservation system through a simple console-based interface. Users can register themselves, access their accounts, search and select trains, choose travel routes and coaches, reserve seats, and manage their bookings.

The project demonstrates the use of:

* Modular Programming
* Functions and Modules
* Conditional Statements
* Loops
* File Handling
* Data Storage and Retrieval
* User Authentication
* Menu-Driven Programming

---

## ✨ Features

### 👤 User Management

* Create New Account
* Secure Login System
* User Credential Storage

### 🚆 Ticket Booking

* View Available Trains
* Select Train
* Choose Route
* Select Coach Type
* Choose Number of Seats
* Enter Passenger Details
* Travel Date Selection
* Automatic Fare Calculation
* Ticket Confirmation

### 📋 Booking Management

* View Booking History
* Cancel Existing Tickets
* Store Passenger Records
* Track Issued Tickets

### 💾 Data Persistence

* User credentials stored in files
* Passenger information saved permanently
* Ticket records maintained for future access

---

## 🛠️ Technologies Used

* Python 3
* File Handling
* Functions
* Modules
* Conditional Statements
* Loops
* Console-Based Interface

---

## 📂 Project Structure

```text
Railway Ticket Booking System
│
├── main.py                    # Main entry point
├── login.py                   # User login functionality
├── create_account.py          # New account creation
├── after_login.py             # Post-login menu options
│
├── trains_list.py             # Display available trains
├── select_train.py            # Train selection
├── route_selection.py         # Route selection logic
├── routelist.py               # Available routes data
│
├── coaches_list.py            # Available coach types
├── select_coach.py            # Coach selection
├── seats_input.py             # Seat quantity input
├── seat_availability.py       # Seat availability checker
│
├── passenger_details.py       # Passenger information
├── date.py                    # Journey date handling
├── payment_calculation.py     # Ticket fare calculation
├── booking_successful.py      # Booking confirmation
│
├── book_ticket.py             # Ticket booking workflow
├── booking_history.py         # Booking history management
├── cancel_ticket.py           # Ticket cancellation
├── exit.py                    # Program termination
│
├── users_cred.txt             # User credentials database
├── save_passengers.txt        # Passenger records
└── tickets_issued.txt         # Issued ticket records
```

---

## 🔄 Booking Workflow

```text
Create Account / Login
          │
          ▼
     Select Train
          │
          ▼
      Select Route
          │
          ▼
      Select Coach
          │
          ▼
    Check Availability
          │
          ▼
   Enter Passenger Details
          │
          ▼
     Calculate Fare
          │
          ▼
    Confirm Booking
          │
          ▼
      Save Ticket
```

---

## ▶️ How to Run

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to Project Directory

```bash
cd Railway-Ticket-Booking-System
```

### Run the Application

```bash
python main.py
```

---

## 📚 Learning Outcomes

Through this project, users can learn:

* Python Project Structure
* Modular Programming Techniques
* File Handling Operations
* Data Storage and Retrieval
* User Authentication Systems
* Real-World Application Development
* Reservation System Logic
* Menu-Driven Program Design

---

## 🚀 Future Enhancements

* PNR Number Generation
* Database Integration (SQLite/MySQL)
* Email Ticket Confirmation
* QR Code-Based Tickets
* Multiple Passenger Booking
* Waiting List Management
* Seat Preference Selection
* Real-Time Train Status Tracking
* GUI Version using Tkinter
* Web Application using Flask/Django
* Admin Dashboard
* Online Payment Gateway Integration
* Ticket Download in PDF Format
* SMS Notifications
* Railway API Integration

---

## 🎯 Purpose

This project was developed as a learning-focused application to understand how a railway reservation system works while practicing Python programming concepts through a real-world use case.

**🚆 Built with Python to simulate a complete Railway Reservation and Ticket Management System.**
