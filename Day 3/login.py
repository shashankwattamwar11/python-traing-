def login_required(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return"access denied"
    return wrapper

@login_required
def dashboard(user):
        return f"Welcome to the dashboard!"

print(dashboard("admin"))  # Should print: Welcome to the dashboard!
print(dashboard("guest"))  # Should print: access denied