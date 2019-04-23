from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Chaz B.',
        'title': 'Blog Post #1',
        'content': 'Cool stuff in this post.',
        'date_posted': 'April 23rd, 2019'
    },
    {
        'author': 'Jane Do',
        'title': 'Blog Post #2',
        'content': 'Cool stuff in 2nd post.',
        'date_posted': 'April 24th, 2019'
    }
]


@app.route('/')
def base_route():
    return '<h1>Hello, from Flask</h1>'


@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
