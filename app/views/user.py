from flask import render_template, request
from app.models.user import User, _create, _update, _destroy


class views:
    def index():
        return render_template('user/index.html')

    def new():
        return render_template('user/new.html')

    def create():
        username = request.form['username']
        email = request.form['email']
        _create(username, email)
        return 'User creation successful'

    def show(id):
        user = User.query.filter_by(id=id).first()
        return render_template('user/show.html', user=user)

    def edit(id, url_update, url_delete):
        user = User.query.filter_by(id=id).first()
        return render_template('user/edit.html', user=user, url_update=url_update, url_delete=url_delete)

    def update(id):
        email = request.form['email']
        _update(id, email)
        return "User update successful"

    def destroy(id):
        _destroy(id)
        return "User deleted!"
