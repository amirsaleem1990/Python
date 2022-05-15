# write into pickle file
pickle.dump(List, open("pickle.pkl", "wb"))

# read from pickle file and save it into variable
List = pickle.load(open("pickle.pkl", "rb"))
