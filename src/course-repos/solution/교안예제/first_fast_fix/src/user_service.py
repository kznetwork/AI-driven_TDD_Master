def greeting(db, user_id):
    return f"{db.get_name(user_id)}!"
