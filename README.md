# Programming-Assignment-3

## PROBLEM 1: 
Using knowledge obtained from the experiment and demonstrations:

### **a. Load the corresponding .csv file into a data frame named cars using pandas**

![image](https://github.com/user-attachments/assets/11c4a9fb-c537-4bfa-96cd-016bd437c950)

  For this problem, I kept it simple and just used the _read_csv_ function of the pandas library and assign it to a dataframe named **cars**.
  
````
cars = pd.read_csv ('cars.csv')
cars
````

### **b. Display the first five and last five rows of the resulting cars.**

![image](https://github.com/user-attachments/assets/6a172422-2bcc-4039-9b7f-b1215254abe9)

  Upon the theme of keeping things simple, I used the _.head_ function of pandas. Although it automatically assigns a value of 5, I want it clearly indicated, hence I put it in the index. The advantage of such is if pandas updates its library and syntax, I can be sure that it still shows the first 5 rows. 

````
# Displaying the first five rows of the resulting cars
cars.head(5)
````
![image](https://github.com/user-attachments/assets/9fc07f96-6351-4fce-8232-68eb4ca44431)

This is the code for the last five rows, quite similar to the previous demonstration except that I used the _.tail_ function which gets the last digits of a table. 

````
# Displaying the first five rows of the resulting cars
cars.tail(5)

````


## PROBLEM 2: 
Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

### **a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.**

![image](https://github.com/user-attachments/assets/fe26e356-b660-45fe-9735-6029b6e671ae)

For this problem, I decided to use the _.iloc_ function of pandas instead of the _.loc_. This is due to the nature of what was asked, _"first five rows with odd-numbered columns"_, which made it difficult to use _.loc_ function which demanded labels as arguments. I carefully selected the arguments to put, where I indicated to take the first 5 rows in ``:5`` and get the odd collumns which I just manually typed ``[1,3,5,7,9]``. This makes things much simpler. 

````
# A) Displaying the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
cars.iloc[:5, [1,3,5,7,9]]

````

### **b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.**
![image](https://github.com/user-attachments/assets/a72c65f3-67c9-4fb2-86dc-8e3207c9004a)

Keeping things simple is the name of the game. This time, using the _.loc_ function is more ideal since the question is looking for a string condition. Using ``cars['Model'] == "Mazda RX4"``, I searched the Model collumn for an instance where Mazda RX4 is used. 

````
# B) Displaying the row that contains the 'Model' of 'Mazda RX'
cars.loc[cars['Model'] == "Mazda RX4"]

````

### **c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?**

![image](https://github.com/user-attachments/assets/50c9f4b3-708a-461f-9aa9-f351afb27ae3)

To answer the question of how many cylindres does Camaro Z28 have, I first used the _.loc_ function and searched the Model column for Camaro Z28. There I inputed an argument which tells _.loc_ to show the Model and cyl collumns, hence answering the question.

````
# C) How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
cars.loc[(cars['Model'] == 'Camaro Z28'), ['Model','cyl']]

````

### **d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.**

![image](https://github.com/user-attachments/assets/d71c955e-d33a-4b18-bd42-c146f981a914)

This is similar to what I did the previous question, except this ask for more rows to be added in the graph. For this, I stumble upon the function _.isin()_ which combines the three needed car and show them as a row. I then just added 'gear' to complete what was asked in the question. 

````
# D) Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
cars.loc[(cars['Model'].isin(["Mazda RX4 Wag","Ford Pantera L","Honda Civic"])), ['Model','cyl', 'gear'] ]
````

## Insights
   The problems were relatively easy and require only a few functions. Thus, by doing things more simple, we make the job less difficult and more quick to solve. 
