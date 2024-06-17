from config import app, api
from models import Post, Comment
from flask_restful import Resource
from flask import request, make_response, jsonify

# create routes here:

@app.route('/sorted_posts', methods = ["GET"])
def sortedPosts():
  posts = Post.query.all()
  posts_dict = [post.to_dict() for post in posts]
  sorted_posts = sorted(posts_dict, key=lambda x: x['title'])
  return make_response(sorted_posts , 200)


@app.route('/posts_by_author/<author_name>')
def posts_by_author(author_name):
  posts = Post.query.all()
  posts_dict = [post.to_dict() for post in posts]
  authors_posts = [post for post in posts_dict if post['author'] == author_name]
  return make_response(authors_posts, 200)

@app.route('/posts_ordered_by_comments')
def posts_ordered_by_comments():
  posts = Post.query.all()
  posts_dict = [post.to_dict() for post in posts]
  sorted_posts = sorted(posts_dict, key=lambda x: len(x['comments']), reverse=True)
  return make_response(sorted_posts, 200)


@app.route('/most_popular_commenter')
def most_popular_commenter():
  commenters = []
  posts = Post.query.all()
  posts_dict = [post.to_dict() for post in posts]
  for post in posts_dict:
    for comment in post['comments']:
      commenters.append(comment["commenter"])

  most_commenter = {'commenter': ''}

  return make_response(commenters, 200)








if __name__ == "__main__":
  app.run(port=5555, debug=True)
