from decorators import log_activity


@log_activity
def admin_login(username):
    print(f"{username} logged into the zoo system.")


@log_activity
def view_actions(username, action):
    print(f"{username} is viewing action: {action}.")


@log_activity
def admin_logout(username):
    print(f"{username} logged out of the zoo system.")
