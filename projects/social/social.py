import random

# A set is a variant of a hash table, so the lookup time is constant.

# UNDERSTANDING
# graph- social network
# node- represents users/people
# edge- friendships that are bidirectional
# connected components- user's extended social network (friends of friends)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship.
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself.")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists.")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID.
        """
        self.last_id += 1  # Automatically increment the ID to assign the new user.
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments.

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph.
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users.
        for user in range(num_users):
            self.add_user(user)
            
        # Create friendships.
        # Create a list with all possible friendships.
        possible_friendships = []

        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, self.last_id + 1):
                possible_friendship = (user, friend)
                possible_friendships.append(possible_friendship)
        # Shuffle it randomly and only take as many as we need.
        random.shuffle(possible_friendships)
        total_friendships = num_users * avg_friendships // 2
        random_friendships = possible_friendships[:total_friendships]

        # Add those friendhsips.
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        return visited


# Brian's walk-through in lecture.

def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments.

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph.
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users.
        for user in range(num_users):
            self.add_user(f'User {i+1}')
            
        # Create friendships.
        target_friendships = (num_users + avg_friendships)
        total_friendships = 0
        collisions = 0
        while < total_friendships < target_friendships:
            # Create a random friendhsip.
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f'COLLISIONS: {collisions}')

def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument.

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set.

        # !!!! IMPLEMENT ME
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
