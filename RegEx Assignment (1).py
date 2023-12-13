#!/usr/bin/env python
# coding: utf-8

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[1]:


import re


# In[5]:


pat = r"\s|,|\."
str = "Python Exercises, PHP exercises."
x = re.sub(pat,":",str)
print(x)


# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[234]:


import pandas as pd
df = pd.DataFrame({'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']})
pat = r",|\.|!|XXXX|:|;|\d+"
dfupdated = df.replace(to_replace = pat,value = "",regex = True)
print(dfupdated)


# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[16]:


str = "This string has few four letter words like 0523 as well"
pat = re.compile(r"\b\w{4,100}")
res = pat.findall(str)
print(res)


# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[17]:


str = "This string has few four letter words like 0523 as well"
pat = re.compile(r"\b\w{3,100}")
res = pat.findall(str)
print(res)


# Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output:
# example.com
# hr@fliprobo.com
# github.com
# Hello Data Science World
# Data Scientist
# 

# In[174]:


Sample_Text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"] 
pat = r"\s\("
list1 = []
for i in Sample_Text:
    res = re.sub(pat,"",i)
    if res:
        list1.append(res)
prog = re.compile(r"\)")
for j in list1:
    bis = prog.sub("",j)
    print(bis)


# Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
# Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
# Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
# Note- Store given sample text in the text file and then to remove the parenthesis area from the text.
# 

# In[30]:


pat = "\s\([^)]*\)"
samp_text = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"] 
list1 = []
for i in samp_text:
    matches = re.sub(pat,"",i)
    if matches:
        list1.append(matches)
print(list1)


# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[45]:


pat = "[A-Z][a-z]*"
samp_text =  "ImportanceOfRegularExpressionsInPython"
res = re.findall(pat,samp_text)
print(res)


# Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[265]:


str = "RegularExpression1IsAn2ImportantTopic3InPython"
def space(input_string):
    pat = re.compile(r"[0-9][A-Z][a-z]*[A-Z][a-z]*")
    res = " ".join(pat.findall(str))
    return res
result = space(str)
print("RegularExpression "+result)


# Question 9- Create a function in python to insert spaces between words starting with capital letters or with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython
# 

# In[253]:


str = "RegularExpression1IsAn2ImportantTopic3InPython"
def space(input_string):
    pat = re.compile(r"([A-Z][a-z]{1,10}[A-Z][a-z]*|[0-9]+)")
    res = " ".join(pat.findall(str))
    return res
result = space(str)
print(result)


# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[276]:


import pandas as pd
url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)
print(df.head())


# Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[277]:


pat = "\w+"
str = "_215 a string which contains 123"
res = re.findall(pat,str)
print(res)


# Question 12- Write a Python program where a string will start with a specific number. 

# In[279]:


pat = "^\d"
str = "215 is my 777 lucky number"
res = re.findall(pat,str)
print(res)


# Question 13- Write a Python program to remove leading zeros from an IP address

# In[100]:


pat = "[0]+"
str ="00000000.192.1680.01"
res = re.sub(pat,"",str)
print(res)


# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[114]:


pat = "\s[A-Z][a-z].+\s\d+[a-z].\s\d+"
str =  "On August 15th 1947 that India was declared independent June 19 2025 from British colonialism, and the reins of control were handed over to the leaders of the Country"
res = re.findall(pat,str)
print(res)


# Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 

# In[117]:


pat = "fox"
str = "The quick brown fox jumps over the lazy dog."
res = re.search(pat,str)
print(res)
pat = "dog"
str = "The quick brown fox jumps over the lazy dog."
res = re.search(pat,str)
print(res)
pat = "horse"
str = "The quick brown fox jumps over the lazy dog."
res = re.search(pat,str)
print(res)


# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 

# In[118]:


pat = "fox"
str = "The quick brown fox jumps over the lazy dog."
res = re.search(pat,str)
print(res)


# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'.

# In[119]:


pat = "exercises"
str = "Python exercises, PHP exercises, C# exercises"
res = re.findall(pat,str)
print(res)


# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[ ]:





# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

# In[181]:


from datetime import date

date_old = "2023-12-12"

date_obj = datetime.strptime(date_old, "%Y-%m-%d")

date_new = date_obj.strftime("%d-%m-%Y")

print(date_new)


# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']

# In[199]:


prog = re.compile(r"\d{1,3}\.\d{1,2}\b")
str = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
res = prog.findall(str)
print(res)


# Question 21- Write a Python program to separate and print the numbers and their position of a given string.

# In[226]:


str = "Maneesh856Jaiswal6521Kumar740"
pat = "(\d+)"
if(res = re.findall(pat,str)
print(res)



# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950

# In[ ]:





# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python

# In[272]:


str = "RegularExpressionIsAnImportantTopicInPython"
def space(input_string):
    pat = re.compile(r"[A-Z][a-z]+")
    res = " ".join(pat.findall(str))
    return res
result = space(str)
print(result)


# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters

# In[273]:


pat = "[A-Z][a-z]+"
str = "This Is A Check for 777 Value"
res = re.findall(pat,str)
print(res)


# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world

# In[200]:


pat = r"\b(\w+)(?: \1\b)+"
str = "Hello hello world world"
res = re.sub(pat,r'\1',str)
print(res)


# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[98]:


pat = r"\w$"
str = "This is to test whether it will detect the last WorD"
res = re.search(pat,str)
print(res)


# Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']

# In[154]:


pat = r"#\w+"
str = """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <U+00A0><U+00BD><U+00B1><U+0089> "acquired funds" No wo"""
res = re.findall(pat,str)
print(res)


# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party leaders

# In[139]:


pat = r"\<U\+[\w]+>"
str = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"
res = re.sub(pat,"",str)
print(res)


# Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Note- Store this sample text in the file and then extract dates.

# In[127]:


pat = r"\b\d{1,2}-\d{1,2}-\d{4}\b"
str = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999"
res = re.findall(pat,str)
print(res)


# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.

# In[125]:


pat = r"\b\w{2,4}\b"
samp_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
res = re.sub(pat,"",samp_text)
print(res)

