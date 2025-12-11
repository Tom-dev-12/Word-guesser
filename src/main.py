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
        session["message"] = ""
        return redirect("/game_screen")
        
        
@app.route("/medium", methods = ["POST"])
def medium():
        
        session["word"] = random.choice(medium_words)
        session["answer"] = ['-'] * len(session["word"])
        session["found"] = False
        session["letters_guessed"] = []
        session["lives"] = 9
        session["message"] = ""
        return redirect("/game_screen")
        
       
@app.route("/hard", methods = ["POST"])
def hard():
        session["word"] = random.choice(hard_words)
        session["answer"] = ['-'] * len(session["word"])
        session["found"] = False
        session["letters_guessed"] = []
        session["lives"] = 9
        session["message"] = ""
        return redirect("/game_screen")



@app.route("/game_screen")
def game_screen():
      return render_template(
        "game.html",
        answer=" ".join(session["answer"]),
        lives=session["lives"],
        guessed=session["letters_guessed"],
        message=session["message"]
    )

@app.route("/enter", methods = ["POST"])
def play():
    
    word = session["word"]
    lives = session["lives"]
    letters_guessed = session["letters_guessed"]
    answer = session["answer"]
    message = ""

   
    guess = request.form["users_guess"].lower()

    if guess == word:
          return render_template("win.html", word = session["word"])

    if guess in word:
          for i, letter in enumerate(word):
                if letter == guess:
                      answer[i] = guess
      
    if guess in word:
          for i, letter in enumerate(word):
                if letter != guess:
                      lives -= 1

    
    if guess in letters_guessed:
          message = "You've already guessed that letter"
    else:
          letters_guessed.append(guess)

    session["answer"] = answer
    session["lives"] = lives
    session["letters_guessed"]  = letters_guessed
    session["message"] = message
    session["word"] = word


    

    if '-' not in answer:
          return render_template("win.html", word = session["word"])
    
    if lives <= 0:
          return render_template("lose.html", word = session["word"])
    
    return redirect("/game_screen")


if __name__ == "__main__":
        app.run(debug=True)




    
