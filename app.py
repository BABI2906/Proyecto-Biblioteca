from flask import Flask, render_template, request, redirect, url_flor, flash
from library import library
from models import Book, Member

app = Flask(__name__)
app.secret_key = "dev-key"

lin = library()

def seed_if_empty():
    if not lib.books and not lib.members:
        lib.add_book("Bajo la misma estrella", "Andcres Manuel Lopez Obrador", 2010)
        lib.add_book("1986", "Benito Juarez", 2015)
        lib.add_book("Don Quijote", "Adolf Hittler", 1939)
        lib.add_book("Mobydick", "Keanu Reeves", 2020)
        
        lib.add_member("Pepitita Juarez")
        lib.add_member("Rocio DTA")
        lib.add_member("Ibai")
        lib.add_member("Auron Play")
        





if __name__ == "__main__":
    app.run(debug=True)
    