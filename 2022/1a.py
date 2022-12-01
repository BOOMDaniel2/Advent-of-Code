with open('1.in','r') as fin:
    people = fin.read()

print(
    max( # Get the max value
    [
        sum(map(int, person.split())) # Split each person into ints at \n and sum
        for person in people.split("\n\n") # Split into people at \n\n
        ]
    ))