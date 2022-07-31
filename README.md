Project:
<figure class="video_container">
    <iframe src="../static/bandicam 2022-07-31 17-52-21-751.mp4" frameborder="0" allowfullscreen="true"><iframe>
</figure>
## Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately.
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
source venv/Scripts/activate
```
if their is error like **scripts is enable in this system** then you need to follow the following steps
<br>
### HOW TO ENABLE SCRIPTS ?

1. Open PowerShell (if you are running PowerShell on Windows Vista, right-click your PowerShell icon and select
Run as administrator. If you don’t do this, you will not be able to enable script support).

2. Check the current script execution policy by using the ``` Get-ExecutionPolicy ``` comand copy and 
paste in PowerSell and press Enter on your keyboard. PowerShell will return a value of ``` Restricted ```.

3. To change the script execution policy, use the ``` Set-ExecutionPolicy unrestricted ``` comand and press 
Enter on your keyboard. 

3. To ensure that the script execution policy has been changed, use the " Get-ExecutionPolicy " comand 
again. PowerShell should return a value of ``` Unrestricted ```.
<br>
Then install the project dependencies with All the required library are mentioned in requirements.txt
We can use requirements.txt to install library using command

```
pip install -r requirements.txt
```
this will install all the library mentioned.

Now you can run the project with this command

```
python manage.py runserver
```

**Note** if you want payments to work you will need to enter your own Stripe API keys into the `.env` file in the settings files.







