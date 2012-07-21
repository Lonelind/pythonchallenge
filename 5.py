import pickle

file = open("banner.p")

p = pickle.load(file)

for elt in p :
    print "".join([e[1] * e[0] for e in elt])
