import Algorithm
def test_cases():
    user_data = {
        1: Algorithm.User(1,"siva","siv@gmail.com"),
        2: Algorithm.User(2,"samba","samba@gmail.com"),
        3: Algorithm.User(3,"venkey","venkey@gmail.com"),
        4: Algorithm.User(4,"venu","venu@gmail.com"),
        5: Algorithm.User(5,"ravi","ravi@gmail.com")
    }

    # Add friendships
    user_data[1].add_friend(5)
    user_data[1].add_friend(3)
    user_data[2].add_friend(1)
    user_data[2].add_friend(1)
    user_data[3].add_friend(1)
    user_data[3].add_friend(1)
    user_data[4].add_friend(2)
    user_data[4].add_friend(3)
    user_data[4].add_friend(5)
    user_data[5].add_friend(4)
    assert set(Algorithm.suggest_friends(1, user_data)) == {4},"Test case 1 Faild"
    print("Test case 1 passed.")
    assert set(Algorithm.suggest_friends(2, user_data)) == {3, 5},"Test case 2 Faild"
    print("Test case 2 passed.")
    assert set(Algorithm.suggest_friends(3, user_data)) == {5},"Test case 3 Faild"
    print("Test case 3 passed.")
    assert set(Algorithm.suggest_friends(4, user_data)) == {1},"Test case 4 Faild"
    print("Test case 4 passed.")
    assert set(Algorithm.suggest_friends(5, user_data)) == {2, 3},"Test case 5 Faild"
    print("Test case 5 passed.")
test_cases()