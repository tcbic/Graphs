from room import Room
from player import Player
from world import World
from util import Queue

import random
from ast import literal_eval

# NOTES

# FILL THE TRAVERSAL PATH WITH DIRECTIONS THAT WHEN WALKED
# IN ORDER WILL VISIT EVERY ROOM IN THE MAP AT LEAST ONCE.

# A simple traversal will just visit all of the nodes,
# but we want a list of directions.
# A simple traversal doesn't backtrack the way we want.

# You can run a traversal until you reach a dead end, but then
# you have to turn around and go back to an unexplored room.

# Think about building your own graph to keep track of where we 
# have and haven't explored. Tells us where we have to backtrack to.

##########
##########

# Create a Graph class.

reverse_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


class WorldGraph:

    """Represent a graph as a dictionary of nodes/vertices (i.e. rooms) 
        mapping labels to edges."""
    # When we instantiate the graph class we get an empty 
    # dictionary. (ADJACENCY LIST REPRESENTATION)
    def __init__(self):
        self.rooms = {}
    # How do we add a room to the graph?
    def add_room(self, room):
        """Add a room to the graph."""
        # The value is an empty set because so far this room 
        # doesn't have any connections.
        possible_directions = room.get_exits()
        self.rooms[room.id] = {direction : '?' for direction in possible_directions}
    
    # Getting one room connected to another room.
    def add_edge(self, start_room, next_room, direction):
        
        # First check if both rooms are in self.rooms...
        if start_room.id in self.rooms and next_room.id in self.rooms:
            # This will ultimately update an unexplored room.
            self.rooms[start_room.id][direction] = next_room.id
            self.rooms[next_room.id][reverse_directions[direction]] = start_room.id
        else:
            raise IndexError("Room doesn't exist.")   

    # Show the directions a player can go from a room.
    # Think about what we would want to return and the 
    # data structure we would want this in.
    def get_neighbors(self, room_id):
        """Get all the neighbors of the room."""
        # Return the values in a set.
        return set(self.rooms[room_id].values())
    
    def bfs(self, start_room):
        # Create a queue.
        queue = Queue()

        # Create a set for visited rooms.
        visited = set()

        # Add a path to the start room id to the queue.
        queue.enqueue([start_room.id])          

        # While the queue isn't empty...
        while queue.size() > 0:
            
            # Dequeue the next room's path.
            current_path = queue.dequeue()
            # Current node is the last room in the path.
            current_node = current_path[-1]

            if current_node not in visited:
                # If the current_node unexplored...
                if current_node == '?':
                # What's the thing we are trying to do?
                # Find the unexplored directions.
                # DO THE THING
                    directions = []
                    for i in range(1, len(current_path[:-1])):
                        for move in traversal_graph.rooms[current_path[i-1]]:
                            if traversal_graph.rooms[current_path[i-1]][move] == current_path[i]:
                                directions.append(move)
                
                    return directions
            
                # If it isn't in visited, add it to visited.
                
                visited.add(current_node)                
            
                # For each neighbor...
                neighbors = self.get_neighbors(current_node)
                for neighbor in neighbors:
                    path_copy = list(current_path)
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)

##########
##########

# Load world.
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary.
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map.
world.print_rooms()

#######################
#########START#########
#######################

# Create a Player instance.
player = Player(world.starting_room)

# Fill this out with directions to walk.
# traversal_path = ['n', 'n']
traversal_path = []

# Create a WorldGraph instance.
traversal_graph = WorldGraph()

# Add the current room to the graph.
traversal_graph.add_room(player.current_room)

def traverse_world():    

    while len(traversal_graph.rooms) < len(room_graph):
        # Define the player's current room.
        current_room = player.current_room
        # Grab the possible exits of the current room.
        possible_exits = current_room.get_exits()
        # Get the player's current id.
        current_room_id = current_room.id
        
        # Create a list of the unexplored directions/exits.
        
        unexplored_dir = [dir for dir in possible_exits if (traversal_graph.rooms[current_room.id][dir] == '?')]
        # print(unexplored_dir)
        
        if current_room_id not in traversal_graph.rooms:
            # Add the current room to the graph. 
            traversal_graph.add_room(current_room)        

        # If unvisited rooms exist from the current room...
        if len(unexplored_dir) > 0:
            # Make a random selection from the list of unexplored directions.
            
            random_dir = random.choice(unexplored_dir)

            # Move the player in the random direction.
            player.travel(random_dir)

            # Add the direction to the traversal path.
            traversal_path.append(random_dir)

            # Save the next room id.
            next_room = player.current_room            
            
            next_room_id = next_room.id            

            # Is the new room already in the graph?
            if next_room_id not in traversal_graph.rooms:
                # Add the room the the graph.
                traversal_graph.add_room(next_room)

            # Add an edge between the current and next rooms.
            traversal_graph.add_edge(current_room, next_room, random_dir)
        
        # No unvisited exits in the current room.
        else:
            dir_move = traversal_graph.bfs(current_room)

            if len(dir_move) > 0:
                for dir in dir_move:
                    player.travel(dir)
                    traversal_path.append(dir)

traverse_world() 


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")