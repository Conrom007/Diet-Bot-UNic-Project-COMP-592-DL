import mysql.connector
def Data_Update(user_ID,food, quantity, calories, protein ,carbs, fat, sugar, sodium): 
    mydb = mysql.connector.connect( host="localhost", user="root",  
    passwd="root", database="dietbot") 
    mycursor = mydb.cursor() 
               #QUERIES:
               
    #query to use outside of function along with function content when adding tables to a database
    #query= "CREATE TABLE user_diet_log (ID VARCHAR(255), dates DATE, food VARCHAR(255), protein VARCHAR(255), carbs VARCHAR(255), fat VARCHAR(255) , meal VARCHAR(255)) "
    #query to use inside function when updating
    query = 'INSERT INTO user_diet_log (usr_ID,food, quantity, calories, protein ,carbs, fat, sugar, sodium) VALUES ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}");'.format(user_ID, food, quantity, calories, protein ,carbs, fat, sugar, sodium) 
    mycursor.execute(query) 
    mydb.commit()
    
    print(mycursor.rowcount, "record inserted")
 
def Total_Calories(user_ID,Date_Needed,Meal):
    mydb = mysql.connector.connect( host="localhost", user="root",  
    passwd="root", database="dietbot") 
    mycursor = mydb.cursor()
    #query = 'SELECT SUM(calories); FROM user_diet_log; WHERE usr_ID = {user_ID} AND date = {Date_Needed}; HAVING meal = {Meal};'.format(user_ID,Date_Needed,Meal)
    query = 'SELECT SUM(calories) FROM user_diet_log WHERE usr_ID = "0b0b32cc60c14756809bc4c1e648cc2d" AND Dates  IS NULL AND meal IS NULL'
    mycursor.execute(query) 
    result = mycursor.fetchone()
    
    print(mycursor.rowcount, "Data retrieved")
    print(result)
    

Total_Calories('0b0b32cc60c14756809bc4c1e648cc2d',0,0)

    
"""
user_ID = 'Test_ID_0'
food = 'Test_food_0'
quantity =  '100g'
calories =  '290'
protein =  '25'
carbs = '25'
fat = '10'
sugar = '25'
sodium = '0.3'
Data_Update(user_ID,food, quantity, calories, protein ,carbs, fat, sugar, sodium)
"""