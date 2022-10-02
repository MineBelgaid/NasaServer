from flask import Flask, request
import json
import os
from pathlib import Path
import sys

#1. flask instance
app = Flask(__name__)

#2 model prediction function
#content and style are the paths for the content and style image respectively

def return_prediction(model,content,style,output):
		
    model.style_image(content, style,output)
    return "done"

#3 load the model
import style_transfer

#4Setting up the page of response
@app.route("/style_transfer_response", methods=['GET','POST'])
def send_reponse():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        imgs = request.json
        content = imgs['input']
        style = imgs['style']
        output = imgs['output']
        results= return_prediction(style_transfer,content,style,output)
        return results
    else:
      #you can change the path to a default path of images in case the response is empty it will show up
        content='./assets/asset1.jpg'
        style='./assets/Style5.jpg'
        output='./result/result.jpg'
        results= return_prediction(style_transfer,content,style,output)
        return results

#4Setting up the page of response
@app.route("/")
def home():
    return """
    <h1>Welcome to our humble server<h1>
    To see the result of our model make a post request in the url /style_transfer_reponse with the following fields :
    <li>content_image:'path of the image'
    <li>style_image:'path of the image'
    <p>The response for the style trasfer is a json with the format :<p>
    <li> {image:'based64 text'} (this needed to be converted to an image to be shown) 
    """
if __name__ == '__main__':
    app.run(debug=False ,port=5001)