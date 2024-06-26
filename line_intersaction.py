# Taking lines coordinates as input
no_of_lines = int(input("Enter no of lines : "))
print("Enter Coordinates as (x1, y1, x2, y2) : ")
lines = []
for _ in range(no_of_lines):
    p1, p2, q1, q2 = map(int, input().split())
    l1 = [p1, p2]
    l2 = [q1, q2]
    lines.append([l1, l2])
lines_m2 = lines

print("\n")
print(f'Lines : {lines}')
print("\n")

# Printing each Points of the lines
points = [point for line in lines for point in line]
print(f'Points : {points}')
print("\n")

# Finding the time lines or unique x coordinates
time_line = list(set(point[0] for point in points))
print(f'Time line is : {time_line}')
print("\n")

# Creating set of lines which is available at specific timeline, 
lines_by_timeline = {}
for x in time_line:
    # Check each line if it is present at this x-coordinate
    for line in lines:
        x1, x2 = line[0][0], line[1][0]
        y1, y2 = line[0][1], line[1][1]
        # Check if the x-coordinate falls within the line segment
        if( x1<=x and x2>=x ) or ( x1>=x and x2<=x ):
            # If the line is present at this x-coordinate, add it to the dictionary
            if x not in lines_by_timeline:
                lines_by_timeline[x] = []
            lines_by_timeline[x].append(line)

for key, lines in lines_by_timeline.items():
    print(f"For time line point : {key}")
    for line in lines:
        print(f"  line {line} is available there")
print("\n")

# Finding, storing and printing, y-coordinates for each line at all time lines.
data_structure = {}
for index, (x_intersect, lines) in enumerate(lines_by_timeline.items()):
    y_coordinate_dict = {}
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]
        slope = (y2-y1) / (x2-x1)
        b = y1-slope*x1
        y_coordinate = slope*x_intersect+b
        pt = {'p1': line[0], 'p2': line[1]}
        if x_intersect not in data_structure:
            data_structure[x_intersect] = []
        data_structure[x_intersect].append({'points': pt, 'y_coordinate': y_coordinate})

# Now sorting lines at all time line, by their y-coordinate, and printing it.
for x_intersect, entries in data_structure.items():
    sorted_entries = sorted(entries, key=lambda x: x['y_coordinate'])
    print(f"x_intersect: {x_intersect}")
    for entry in sorted_entries:
        print(f"  Points: {entry['points']}, y_coordinate: {entry['y_coordinate']}")
    data_structure[x_intersect] = sorted_entries
print("\n")

# From upper data where we have stored points and y-coordinate everything, Now we are extracting points(which will be in sorted manner now)
tmp = []
for x_intersect, entries in data_structure.items():
    point_stack = []
    for entry in entries:
        point_stack.append(entry['points'])
    tmp.append(point_stack)

# From the sorted points(at each time line), we are finding the the ones which are not ordered(intersection lines).
intersection_lines = []
for i in range(len(tmp)-1):
    # Get the list of points at the current and next time lines
    first_list = tmp[i].copy()
    second_list = tmp[i + 1].copy()

    # Find common points between the two time lines
    common_elements = []
    for item in first_list:
        if item in second_list:
            common_elements.append(item)
    
    # Remove points that are not common to both time lines
    first_list = [item for item in first_list if item in common_elements]
    second_list = [item for item in second_list if item in common_elements]
    
    # Iterate through each point pair and check for non-order
    for i in range(len(first_list)):
        # If the points are not in the same order in both time lines, they intersect
        if(first_list[i]!=second_list[i]):
            intersection_lines.append([first_list[i], second_list[i]])

# Now we got intersection lines in [intersection_lines], but it contains duplicate entries, so now we removing duplicates
def sort_and_convert(d):
    return tuple(sorted((k, tuple(v)) for k, v in d.items()))

sorted_pairs = []
for pair in intersection_lines:
    sorted_pair = []
    for dictionary in pair:
        # Sort and convert the dictionary using the defined function
        sorted_dictionary = sort_and_convert(dictionary)
        sorted_pair.append(sorted_dictionary)
    # Sort the list of sorted dictionaries
    sorted_pair.sort()
    sorted_pairs.append(sorted_pair)

# Remove duplicates by converting to set
unique_pairs = set()
for pair in sorted_pairs:
    unique_pairs.add(tuple(pair))

unique_intersection_lines = []
for pair in unique_pairs:
    unique_pair = []
    for item in pair:
        unique_item = {}
        for k, v in item:
            unique_item[k] = list(v)
        unique_pair.append(unique_item)
    unique_intersection_lines.append(unique_pair)

# Now we are printing the graph for given coordinates
import matplotlib.pyplot as plt
for line_ in lines_m2:
    x_values = [point[0] for point in line_]
    y_values = [point[1] for point in line_]
    plt.plot(x_values, y_values, marker='o')
    for i, (x, y) in enumerate(zip(x_values, y_values)):
        plt.annotate(f'({x}, {y})', (x, y), textcoords="offset points", xytext=(0,10), ha='center')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Lines Plot with Points')
plt.grid(True)
plt.show()

if unique_intersection_lines:
    for line in unique_intersection_lines:
        print(f"There's intersection between {line[0]} and {line[1]}")
else:
    print("There are no intersection points")
