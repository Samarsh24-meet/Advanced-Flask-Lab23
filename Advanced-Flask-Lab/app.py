from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1G50YJw6brINH7RzO60IlGpfJOSWOBJBcJA&usqp=CAU"

user_bio = "Woooo Wooooooo a very cool description warning"

posts = {
    "https://www.tfront.com/images/product/icon/2605.jpg": "cool",
    "https://www.musikalessons.com/blog/wp-content/uploads/2017/01/jazz-piano.jpg": "very coollll!",
    "https://uploads-ssl.webflow.com/5dd64bd3a930f9d04abd1363/5de6d502d6d70c0ad49a060c_6.jpg": "Meet content cuz why not!",
    "https://global-uploads.webflow.com/5fe28feebcae602620061802/5fe5401840671a36cd1d47d5_5de6d5024dd1a74670173aed_1-p-1080.jpeg": "Our lovely TAs!"}

#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html',i = image_link, u = user_bio, p = posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
