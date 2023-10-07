from flask import Flask, render_template
from test import get_profile_detail

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello, World!</p>"
    email_list = ["harshitkumar2000@gmail.com",'arpitbansal2304@gmail.com','kunaltaware210@gmail.com']
    email_list=['diptishgohane04@gmail.com',
    'arpitbansal2304@gmail.com',
    'madhurpatil73@gmail.com',
    'kunaltaware210@gmail.com ']
    details=get_profile_detail(email_list);  
    details = sorted(details, key=lambda x: x['institute_rank'])

    print(details)
    return render_template("index.html",details =details )

if __name__ == "__main__":
    app.run(debug=True)    