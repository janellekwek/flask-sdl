from flask import Flask, render_template, url_for

app = Flask(__name__)


def get_file():
    with open("mytext.txt", "r") as file:
        text = ""
        content = file.readlines()
        for line in content:
            text = text + " " + line.rstrip()
    return text
def get_summary(text):
    num_letters = 0
    char_freq = {}
    for char in text:
        if char.isalpha():
            num_letters += 1
            if char.lower() not in char_freq:
                char_freq[char.lower()] = 1
            else:
                char_freq[char.lower()] += 1
    return num_letters, char_freq
            
@app.route("/")
def home():
    text = get_file()
    num_letters, char_freq = get_summary(text)
    return render_template("index.html", text=text, num_letters=num_letters, char_freq=char_freq)

@app.route("/<find_word>")
def appear(find_word):
    words = get_file().lower().split()
    word_count = 0
    for word in words:
        word = word.strip(",.!?\"'()[]{}<>:;")        
        if find_word.lower() in word:
            word_count += 1
    return render_template("word_count.html", word_count=word_count, find_word=find_word)

if __name__ == "__main__":
    app.run(debug=True, port=12345)
