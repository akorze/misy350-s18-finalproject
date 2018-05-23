from flask_script import Manager
from bookbase import app, db, Author, Book

manager = Manager(app)


# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    Crichton = Author(name='Michael Crichton', about='Science Fiction Author')
    Grisham = Author(name='John Grisham', about='Crime Thriller Author')
    Patterson = Author(name='James Patterson', about='Crime Thriller Author')
    book1 = Book(name='Prey', year=2002, description="Nano-bots", author=Crichton)
    book2 = Book(name='The Firm', year=1991, description="Legal Thriller", author=Grisham)
    book3 = Book(name='Step on a Crack', year=2007, description="Terror Thriller", author=Patterson)
    db.session.add(Crichton)
    db.session.add(Grisham)
    db.session.add(Patterson)
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
