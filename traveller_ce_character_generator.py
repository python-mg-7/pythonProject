import random

def two_d6():
    return random.randint(1,6) + random.randint(1,6)

survival_req = 5
commission_req = 4
promotion_req = 10
reenlist_req = 4

def two_d6():
    return random.randint(1,6) + random.randint(1,6)

strength = two_d6()
endurance = two_d6()
dexterity = two_d6()
intelligence = two_d6()
education = two_d6()
social_standing = two_d6()

print(  str(strength)  + "," + str(endurance)  + "," + str(dexterity) + "," + str(intelligence) + "," + str(education) + "," + str(social_standing))

alive = True
retired = False
officer = False
terms = 0
rank = 0

while( terms < 7 and alive and not(retired)) :
    survival_roll = two_d6()
    if intelligence >= 7: survival_roll += 2
    print("survival roll " + str(survival_roll))
    if (survival_roll >= survival_req):
        is_dead = False
        terms += 1
        if (not(officer) ):
            commission_roll = two_d6()
            if intelligence >= 6: commission_roll += 1
            print("commisssion roll " + str(commission_roll))
            if ( commission_roll > commission_req):
                officer = True
                rank += 1
        if (officer):
            promotion_roll = two_d6()
            if intelligence >= 9: promotion_roll += 1
            print("promotiion roll " + str(promotion_roll))
            if (promotion_roll > promotion_req):
                rank += 1
        reenlistment_roll = two_d6()
        print("re_enlistement_roll " + str(reenlistment_roll))
        if(not(reenlistment_roll > reenlist_req )):
            retired = True
    else:
        alive = False

print("-----------------------")
print("alive: " + str(alive))
print("terms " + str(terms))
print("rank: " + str(rank))


