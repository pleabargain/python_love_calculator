#love calculator

#take input of two names
# count for instance of 
# TRUE
# LOVE

lover_one = input("type your full name: ")
print(f"you entered {lover_one}")
#convert to lower case
lc_lover_one = lover_one.lower()
print (f"Lower case is: {lc_lover_one}")


lover_two = input("type your lover's full name: ")
print(f"you entered {lover_two}")

#convert to lower case
lc_lover_two = lover_two.lower()
print (f"lower case of your lover's name: {lc_lover_two}")

T = lc_lover_one.count("t")
T2 = lc_lover_two.count("t")



R = lc_lover_one.count("r")
R2 = lc_lover_two.count("r")

U = lc_lover_one.count("u")
U2 = lc_lover_two.count("u")


E = lc_lover_one.count("e")
E2 = lc_lover_two.count("e")


L = lc_lover_one.count("l")
L2 = lc_lover_two.count("l")


O = lc_lover_one.count("o")
O2 = lc_lover_two.count("o")

V = lc_lover_one.count("v")
V2 = lc_lover_two.count("v")

print(f"T appears in your name {T} times: ")
print(f"T appears {T2} in your lover's name: ")

print(f"R appears in your name {R} times: ")
print(f"R appears {R2} in your lover's name: ")

print(f"U appears in your name {U} times: ")
print(f"U appears {U2} in your lover's name: ")

print(f"E appears in your name {E} times: ")
print(f"E appears {E2} in your lover's name: ")

count_t = T + T2
count_r = R + R2
count_u = U + U2
count_e = E + E2

count_true = count_t+count_r+count_u+count_e
print(f"count true is: ",count_t+count_r+count_u+count_e)

print(f"L appears in your name {L} times: ")
print(f"L appears {L2} in your lover's name: ")

print(f"O appears in your name {O} times: ")
print(f"O appears {O2} in your lover's name: ")

print(f"V appears in your name {V} times: ")
print(f"V appears {V2} in your lover's name: ")

print(f"E appears in your name {E} times: ")
print(f"E appears {E2} in your lover's name: ")

count_l = L+L2
count_o = O+O2
count_v = V+V2
count_e = E + E2
count_love = count_l+count_o+count_v+count_e
print(f"count love:  {count_love}")
# total_t = lc_lover_one.count("t")+lc_lover_two.count("t")
print(f"Your score is:{count_true}{count_love}")
score = int(str(count_true) +str( count_love))
print(f"This is your love score: {score}")

if (score<=10) or (score>=90):
    print(f"You {lover_one} are awesome together with {lover_two}")
elif (score>=30) and (score<=70):
    print(f"You {lover_one} are ok together with {lover_two}")
else:
    print(f"Get out of town! You {lover_one} and {lover_two} are way too awesome!")