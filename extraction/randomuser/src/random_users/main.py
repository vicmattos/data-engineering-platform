from randomuser import RandomUser


def main():
    # Generate a list of 10 random users
    user_list = RandomUser.generate_users(10)

    for user in user_list:
        print(user.get_full_name())

if __name__ == "__main__":
    main()
