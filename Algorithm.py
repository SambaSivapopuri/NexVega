class User:
    def __init__(self, user_id,name,email):
        self.user_id = user_id
        self.name=name
        self.email=email
        self.friends = set()

    def add_friend(self, friend_id):
        self.friends.add(friend_id)

def suggest_friends(user_id, user_data):
    if user_id not in user_data:
        return []
    direct_friends = user_data[user_id].friends
    potential_friends = set()
    for friend in direct_friends:
        potential_friends.update(user_data[friend].friends)
    potential_friends -= direct_friends
    potential_friends.discard(user_id)
    return list(potential_friends)

