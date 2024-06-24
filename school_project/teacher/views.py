from django.shortcuts import render
import mysql.connector as sql

def teacherlogin(request):
    if request.method == "POST":
        # Connect to the database
        m = sql.connect(host="localhost", user="root", passwd="root", database='newlogin')
        cursor = m.cursor()
        
        # Get form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Debugging: Print the retrieved values
        print(f"Email: {email}, Password: {password}")
        
        # Prevent SQL Injection by using parameterized query
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(query, (email, password))
        result = cursor.fetchall()
        
        # Debugging: Print the result of the query
        print(f"Query Result: {result}")
        
        if not result:
            cursor.close()
            m.close()
            return render(request, 'error.html')
        else:
            query = "SELECT * FROM users"
        cursor.execute(query)
        data = cursor.fetchall()

        # Close database connection
        cursor.close()
        m.close()

        # Pass fetched data to the template for rendering
        context = {
            'data': data,
        }
        return render(request, "success.html", context)
    
    return render(request, 'student.html')



