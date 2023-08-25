from flask import Flask, jsonify, render_template
import praw

app = Flask(__name__)

reddit = praw.Reddit(client_id='V5JLMAFOn4iMpepxRhzkDw',
                     client_secret='17NcWfsZPhcuM_DNzJa3Hu1HtiYDAQ',
                     user_agent='ThreadsInsight by /u/nijgururaj45')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_articles', methods=['GET'])
def fetch_articles():
    subreddit = reddit.subreddit('learnpython')
    threads = subreddit.new(limit=10)

    articles = []
    for thread in threads:
        article = {
            'title': thread.title,
            'author': thread.author.name,
            'created_utc': thread.created_utc,
            'url': thread.url
        }
        articles.append(article)

    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
