with open('1.in','r') as fin:
    people = fin.read()

print(
    sum( # E Add together the last 3 people
        sorted( # C Sort the list
    [
        sum(map(int, person.split())) # B Split each person into ints at \n and sum
        for person in people.split("\n\n") # A Split into people at \n\n
        ]
    )[-3:] # D Get the last 3 people
    ))