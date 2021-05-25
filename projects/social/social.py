import random
from util import Queue


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
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")

        # Create friendships
        # Generate ALL possible friendships
        # avoid duplicate friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, len(self.users.keys()) + 1):
                possible_friendships.append((user_id, friend_id))

        # Randomly select x friendships
        # the formula for X is num_users * avg_friendships // 2
        # shuffle the array and pick x elements from the front
        random.shuffle(possible_friendships)
        num_friendships = num_users * avg_friendships // 2
        for i in range(0, num_friendships):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = Queue()
        queue.enqueue([user_id])

        while queue.size() > 0:
            current_path = queue.dequeue()
            current_user_id = current_path[-1]

            if current_user_id not in visited:
                visited[current_user_id] = current_path

                for friend_id in self.friendships[current_user_id]:
                    new_path = current_path.copy()
                    new_path.append(friend_id)
                    queue.enqueue(new_path)

        return visited


"""
Part 3
1. To create 100 users with an average of 10 friends each, add_friendship() would 
    need to be called 50 times, because each friendship goes two ways, which means
    both the users would have one friend after just one call of add_friendship(). 
    Thus, it takes half the number of average friends times the total number of users.
2. On average, with 1000 users with an average of 5 friends, each user will have
    98.6 percent of the total users in their network. 
    On average these same users have 3.5 degrees of separation from others in their
    connection network. (1 degree of separation being a friend's friend)
"""

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(5, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
