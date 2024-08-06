// python

from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'Functionality_Badges.html')

if __name__ == '__main__':
    app.run(debug=True)


// html

<a href="https://GitHub.com/amanaknows/intelligent-things/calculate_mean">
    <img src="https://img.shields.io/badge/Basic%20Data%20Processing-Mean%20Calculation-blue" alt="Basic Data Processing">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/read_file">
    <img src="https://img.shields.io/badge/File%20Operations-Read%20File-green" alt="File Operations">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/get_weather?city=London">
    <img src="https://img.shields.io/badge/API%20Request-Weather%20Info-yellow" alt="API Request">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/get_users">
    <img src="https://img.shields.io/badge/Data%20Storage-Users%20List-orange" alt="Data Storage">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/scrape_title?url=https://www.example.com">
    <img src="https://img.shields.io/badge/Web%20Scraping-Page%20Title-red" alt="Web Scraping">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/greet_person?name=John&age=30">
    <img src="https://img.shields.io/badge/Basic%20Class-Person%20Greeting-purple" alt="Basic Class">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/divide_numbers?a=10&b=0">
    <img src="https://img.shields.io/badge/Error%20Handling-Divide%20Numbers-pink" alt="Error Handling">
</a>
<a href="https://GitHub.com/amanaknows/intelligent-things/filter_even_numbers?numbers=[1,2,3,4,5,6]">
    <img src="https://img.shields.io/badge/Data%20Filtering-Even%20Numbers-lightblue" alt="Data Filtering">

    
// ending python snippet for our ai 
from flask import Flask, render_template_string, request
import gettext
import os

# Set up gettext
locale_dir = 'locales'
lang = request.args.get('lang', 'en')  # Get language from URL query parameter or default to 'en'
translation = gettext.translation('messages', localedir=locale_dir, languages=[lang], fallback=True)
_ = translation.gettext

app = Flask(__name__)

@app.route('/')
def index():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="{lang}">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{_('Declunking')}</title>
    </head>
    <body>
        <h1>{_('Functionality Badges')}</h1>
        <a href="https://GitHub.com/amanaknows/intelligent-things/calculate_mean">
            <img src="https://img.shields.io/badge/{_('Basic%20Data%20Processing')}-{_('Mean%20Calculation')}-blue" alt="{_('Basic Data Processing')}">
        </a>
        <a href="https://GitHub.com/amanaknows/intelligent-things/read_file">
            <img src="https://img.shields.io/badge/{_('File%20Operations')}-{_('Read%20File')}-green" alt="{_('
