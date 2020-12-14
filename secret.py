import random


def split(num):
    p1 = random.randint(0, num-2)
    p2 = random.randint(0, num-p1-1)
    p3 = num-(p1+p2)
    return [p1, p2, p3]


class Party:
    def __init__(self, x, y, a, b, c):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.c = c

    def compute_d(self):
        return self.x-self.a

    def compute_e(self):
        return self.y-self.b

    def compute_z(self, d, e):
        return self.c+(self.x)*e+(self.y)*d


# irrelevant
x = split(int(input("enter x: ")))
y = split(int(input('enter y: ')))

# generating triplets
a_val = random.randint(1, 1000)
b_val = random.randint(1, 1000)

a = split(a_val)
b = split(b_val)
c = split(a_val*b_val)

# assigning values to random guys
RandomGuy1 = Party(x[0], y[0], a[0], b[0], c[0])
RandomGuy2 = Party(x[1], y[1], a[1], b[1], c[1])
RandomGuy3 = Party(x[2], y[2], a[2], b[2], c[2])

parties = [RandomGuy1, RandomGuy2, RandomGuy3]

# computing v1 and v2, taken as d and e for convenience
d = 0
e = 0

for i in parties:
    d = d+i.compute_d()
    e = e+i.compute_e()

# computing final z
z = 0

for party in parties:
    z = z+party.compute_z(d, e)

print(z-e*d)
