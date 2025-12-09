import random
from flask import Flask, render_template, redirect, request, session

with open("easy_words.txt", "r") as easy:
    easy_words = [line.strip() for line in easy]

with open("medium_words.txt", "r") as medium:
    medium_words =[line.strip() for line in medium]

with open("hard_words.txt", "r") as hard:
    hard_words = [line.strip() for line in hard]


app = Flask(__name__)
app.secret_key = "secret" 


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/easy", methods = ["POST"])
def easy():     
        session["word"] = random.choice(easy_words)
        session["answer"] = ['-'] * len(session["word"])
        session["found"] = False
        session["letters_guessed"] = []
        session["lives"] = 9
        return redirect("/")
        
        
@app.route("/medium", methods = ["POST"])
def medium():
        
        session["word"] = random.choice(medium_words)
        session["answer"] = ['-'] * len(session["word"])
        session["found"] = False
        session["letters_guessed"] = []
        session["lives"] = 9
        return redirect("/")
        
       
@app.route("/hard", methods = ["POST"])
def hard():
        session["word"] = random.choice(hard_words)
        session["answer"] = ['-'] * len(session["word"])
        session["found"] = False
        session["letters_guessed"] = []
        session["lives"] = 9
        return redirect("/")


@app.route("/game_screen")
def game_screen():
      return render_template("game.html")


@app.route("/enter", methods = ["POST"])
def play():
    
    word = session["word"]
    lives = session["lives"]
    letters_guessed = session["letters_guessed"]
    answer = session["answer"]

    message = ""

    guess = request.form["users_guess"].lower()

    if guess in word:
          for i, letter in enumerate(word):
                if letter == guess:
                      answer[i] = guess
                message = "correct"
    
    else:
          lives -= 1

    session["answer"] = answer
    session["lives"] = lives
    session["letters_guessed"]  = letters_guessed
    session["message"] = message


    if guess in letters_guessed:
          message = "You've already guessed that letter"
    else:
          letters_guessed.append(guess)

    if '-' not in answer:
          return render_template("win.html")
    
    if lives <= 0:
          return render_template("lose.html")
    
    return render_template("game.html",
                           answer=" ".join(answer),
                           lives=lives,
                           guessed=letters_guessed,
                           message=message)



if __name__ == "__main__":
        app.run(debug=True)




    
