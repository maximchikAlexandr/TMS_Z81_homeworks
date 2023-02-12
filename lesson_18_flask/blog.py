from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from facade import PostFacade
from db import EngineDB

app = Flask(__name__)
app.config["SECRET_KEY"] = "12345"
engine_db = EngineDB()
post_facade = PostFacade(engine_db=engine_db)


@app.route("/", methods=["GET"])
def index():
    post_data = post_facade.get_all_posts()
    return render_template("index.html", posts=post_data)


@app.route("/posts/<int:post_id>", methods=["GET"])
def post(post_id):
    post_data = post_facade.get_post(post_id)
    if post_data is None:
        abort(404)
    return render_template("post.html", post=post_data)


@app.route("/<int:post_id>/edit/", methods=["POST", "GET"])
def edit(post_id):
    post_data = post_facade.get_post(post_id)
    if post_data is None:
        abort(404)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title or not content:
            flash("Title and content are both required")
        else:
            post_facade.update_post(id_=post_id,
                                    title=title, content=content)
            return redirect(url_for("index"))

    return render_template("edit.html", post=post_data)


@app.route("/<int:post_id>/delete", methods=["POST", "GET"])
def delete(post_id):
    if request.method == "POST":
        post_facade.remove_post(id_=post_id)
        flash(f"Post {post_id} was deleted")
    return redirect(url_for("index"))


@app.route("/create-post", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title or not content:
            flash("Title and content are both required")
        else:
            post_facade.create_post(title=title, content=content)
            return redirect(url_for("index"))
    return render_template("create.html")


if __name__ == "__main__":
    app.run()
