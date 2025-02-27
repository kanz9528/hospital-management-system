import pandas as pd
import matplotlib.pyplot as plt 
import mysql.connector
# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iron_Men",
    database="hospital"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Function to add a new patient

def add_patient(name, age, gender, disease):
    sql = "INSERT INTO patient (name, age, gender, disease) VALUES (%s, %s, %s, %s)"
    val = (name, age, gender, disease)
    cursor.execute(sql, val)
    db.commit()
    print("Patient added successfully!")
def add_doctor(name, specialization, fee):
    sql = "INSERT INTO doctor (name, specialization, fee) VALUES (%s, %s, %s)"
    val = (name, specialization, fee)
    cursor.execute(sql, val)
    db.commit()
    print("Doctor added successfully!")

# Function to schedule an appointment
def schedule_appointment(patient_id, doctor_id, date, time):
    sql = "INSERT INTO schedule_appointment (patient_id, doctor_id, date, time) VALUES (%s, %s, %s, %s)"
    val = (patient_id, doctor_id, date, time)
    cursor.execute(sql, val)
    db.commit()
    print("Appointment scheduled successfully!")


# Function to view all appointments 
def view_appointment():
    sql = "SELECT * FROM schedule_appointment"
    li = []
    cursor.execute(sql)
    appointments = cursor.fetchall()
    for appointment in appointments:
        print('patient_id:', appointment[0])
        print('doctor_id:', appointment[1])
        print('date:', appointment[2])
        print('time:', appointment[3])

        li.append([appointment[0], appointment[1], appointment[2], appointment[3]])
        print('\n\n')
    df = pd.DataFrame(li)
    df.columns = ['patient_id', 'doctor_id', 'date', 'time']
    df.to_csv('C:\\New folder\\hospital3.csv')
    plt.bar(df['patient_id'], df['time'])
    plt.xlabel('patient_id')
    plt.ylabel('time')
    plt.savefig('C:\\New folder\\graph3.jpg')
    plt.show()
    print(appointments)

# Function to view all patients 
def view_patient():
    sql = "SELECT * FROM patient"
    li = []
    cursor.execute(sql)
    patients = cursor.fetchall()
    for patient in patients:
        print('name:', patient[0])
        print('age:', patient[1])
        print('gender:', patient[2])
        print('disease:', patient[3])
        li.append([patient[0], patient[1], patient[2], patient[3]])
        print('\n\n')
    df = pd.DataFrame(li)
    df.columns = ['name', 'age', 'gender', 'disease']

    df.to_csv('C:\\New folder\\hospital1.csv')
    plt.bar(df['disease'], df['age'])
    plt.xlabel('disease')
    plt.ylabel('age')
    plt.savefig('C:\\New folder\\graph1.jpg')
    plt.show()
    print(patients)


# Function to view all doctors
def view_doctor():
    sql = "SELECT * FROM doctor"
    li = []
    cursor.execute(sql)
    doctors = cursor.fetchall()
    for doctor in doctors:
        print('name:', doctor[0])
        print('specialization:', doctor[1])
        print('fee:', doctor[2])
        li.append([doctor[0], doctor[1], doctor[2]])
        print('\n\n')

    df = pd.DataFrame(li)
    df.columns = ['name', 'specialization', 'fee']
    df.to_csv('C:\\New folder\\hospital2.csv')
    plt.bar(df['specialization'], df['fee'])
    plt.xlabel('specialization')
    plt.ylabel('fee')
    plt.savefig('C:\\New folder\\graph2.jpg')
    plt.show()
    print(doctors)



# Main menu
while True:
    print("\nHospital Management System")
    print("1. Add Patient")
    print("2. Add Doctor")
    print("3. Schedule Appointment")
    print("4. View Appointment")
    print("5. View Patient")
    print("6. View Doctor")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter patient_name: ")
        age = int(input("Enter patient_age: "))
        gender = input("Enter patient_gender: ")
        disease = input("Enter patient_disease:")
        add_patient(name, age, gender, disease)

    elif choice == 2:
        name = input("Enter doctor's name: ")
        specialization = input("Enter doctor's specialization:")
        fee = int(input("Enter doctor's fee:"))
        add_doctor(name, specialization, fee)

    elif choice == 3:
        patient_id = input("Enter patient's ID: ")
        doctor_id = input("Enter doctor's ID: ")
        date = input("Enter appointment date: ")
        time = input("Enter appointment time: ")
        schedule_appointment(patient_id, doctor_id, date, time)

    elif choice == 4: 
        view_appointment()

    elif choice == 5: 
        view_patient()

    elif choice == 6: 
        view_doctor()

    elif choice == 0: 
        print("Thank you for using the Hospital Management System")
        break

    else:
        print("Invalid choice. Please try again.")
