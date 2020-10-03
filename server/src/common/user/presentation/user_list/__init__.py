import flask.views


class UserListPage(flask.views.MethodView):
    def get(self):
        return "users"
