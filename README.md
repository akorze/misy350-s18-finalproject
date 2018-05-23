# misy350-s18-finalproject

### Alek Korzeniowski - MISY 350 - Spring 2018

I'm making a database to catalog a list of books, their respective authors, and a little about each book and author. I will have a book table with columns name, year released, and a description about each book. I will also have an author table with columns name and about. Each book can only have one author and one author can write many books, so there is a one-to-many relationship here.

### Database Design
Author ID |  Name | About
------------|---------------|-------------
1 | Michael Crichton | Science Fiction Author
2 | John Grisham | Crime Thriller Author
3 | James Patterson | Crime Thriller Author

Book ID | Name | Year | Description | Author
---------|-------|------|------------|---------
1 | Prey | 2002 | Nano-bots | Michael Crichton
2 | The Firm | 1991 | Legal Thriller | John Grisham
3 | Step on a Crack | 2007 | Terror Thriller | James Patterson

### Instructions

In order to run our website, you'll need to follow a few simple steps to get it up and running in your web browser of choice.

- **Windows Instructions**

    1. Go to my [repository on Github](https://github.com/akorze/misy350-s18-finalproject) and clone the repo so that you can store it locally.

    2. Open Powershell

    3. Type the following command to open the project directory:
            cd ./misy350-s18-finalproject/

    4. Type the following command to create Virtualenv so that we can setup a virtual environment:
            pip install virtualenv

    5. Create the venv folder:
            virtualenv venv

    6. Activate the virtual environment:
            venv/scripts/activate

    7. Install the requirements for the project:
            pip install -r requirements.txt

    8. Initialize the database:
            python manage.py deploy

    9. Run the server:
            python manage.py runserver -d

    10. View the website in your web browser by typing your IP address into the address bar.

- **Mac Instructions**
  1. Go to my [repository on Github](https://github.com/akorze/misy350-s18-finalproject) and clone the repo so that you can store it locally.

  2. Open the Command Line

  3. Type the following command to open the project directory:
          cd misy350-s18-finalproject

  4. Type the following command to create Virtualenv so that we can setup a virtual environment:
          sudo pip install virtualenv

  5. Create the venv folder:
          virtualenv venv

  6. Activate the virtual environment:
          venv/bin/activate

  7. Install the requirements for the project:
          pip install -r requirements.txt

  8. Initialize the database:
          python manage.py deploy

  9. Run the server:
          python manage.py runserver -d

  10. View the website in your web browser by typing your IP address into the address bar.
