from flask import Flask, render_template,url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

# @app.route('/')
# def hello_world():
#     print(url_for('static', filename='favicon.ico'))
#     return render_template('./index.html')
    
# @app.route('/<username>/<int:post_id>')
# def hello_world_username(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)

# @app.route('/about')
# def about():
#     return render_template('./about.html')

# @app.route('/blog')
# def blog():
#     return 'These are my thoughts on blogs!'

# # @app.route('/favicon.ico')
# # def blog():
# #     return 'These are my thoughts on blogs!'

 
# @app.route('/blog/2020/dogs')
# def dog():
#     return 'This is my dog!'

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data["email"], data["subject"], data["message"]])

@app.route('/')
def my_home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template('./'+page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'something went wrong!'


# @app.route('/about.html')
# def about():
#     return render_template('./about.html')

# @app.route('/works.html')
# def work():
#     return render_template('./works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('./contact.html')