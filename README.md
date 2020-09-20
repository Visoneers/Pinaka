

## Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with
```
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project
```
virtualenv venv
```
That will create a new folder `env` in your project directory. Next activate it with this command on windows:
```
venv/Scripts/activate
```
and on git:
```
source env/bin/active
```
if their is error like " scripts is enable in this system " then you need to follow the following steps

### HOW TO ENABLE SCRIPTS ?
Step 1: Open PowerShell (if you are running PowerShell on Windows Vista, right-click your PowerShell icon and select
Run as administrator. If you don’t do this, you will not be able to enable script support).
Step 2: Check the current script execution policy by using the ``` Get-ExecutionPolicy ``` comand copy and 
            paste in PowerSell and press Enter on your keyboard. PowerShell will return a value of ``` Restricted ```.
Step 3: To change the script execution policy, use the ``` Set-ExecutionPolicy unrestricted ``` comand and press 
            Enter on your keyboard. 
Step 4: To ensure that the script execution policy has been changed, use the ``` Get-ExecutionPolicy ``` comand 
            again. PowerShell should return a value of ``` Unrestricted ```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

**Note** if you want payments to work you will need to enter your own Stripe API keys into the `.env` file in the settings files.

## How to use virtual environment :  
install virtual environment
```
pip install virtualenv <name>
```

To setup virtual environment we need to run script (command) 
```
virtualenv <name>
``` 
and press enter this will create virtual environment 
To activate virtual environment Script 
```
./<virtual environment name >/Scripts/Activate
```
if their is error like  ** scripts is enable in this system  ** then you need to follow the following steps

## HOW TO ENABLE SCRIPTS ?
1.Step 1: Open PowerShell (if you are running PowerShell on Windows Vista, right-click your PowerShell icon and select
Run as administrator. If you don’t do this, you will not be able to enable script support).

2.Step 2: Check the current script execution policy by using the ``` Get-ExecutionPolicy ``` comand copy and 
paste in PowerSell and press Enter on your keyboard. PowerShell will return a value of ``` Restricted ```.

3.Step 3: To change the script execution policy, use the ``` Set-ExecutionPolicy unrestricted ``` comand and press 
Enter on your keyboard. 

3.Step 4: To ensure that the script execution policy has been changed, use the " Get-ExecutionPolicy " comand 
again. PowerShell should return a value of ``` Unrestricted ```.

<br>

# Libraries :
>> All the required library are mentioned in requirements.txt
>> We can use requirements.txt to install library using command 

```
pip install -r requirements.txt 
``` 
this will install all the library mentioned.




