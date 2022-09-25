import random
import pandas

service_rolls = {'Navy': {'Enlist': 8, 'Survive': 5, 'Commission': 10, 'Promotion': 8, 'Reenlistment': 6}, 'Marines': {'Enlist': 9, 'Survive': 6, 'Commission': 9, 'Promotion': 9, 'Reenlistment': 6},'Army': {'Enlist': 5,'Survive': 5, 'Commission': 5, 'Promotion': 6, 'Reenlistment': 7}, 'Scouts': {'Enlist': 7, 'Survive': 7, 'Reenlistment': 3}, 'Merchants': {'Enlist': 7, 'Survive': 5, 'Commission': 4, 'Promotion': 10, 'Reenlistment': 4}, 'Others': {'Enlist': 3, 'Survive': 5, 'Reenlistment': 5}}

personal_development = {'Navy': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'social_standing', 5: 'intelligence', 6: 'education' }, 'Marines': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'gambling', 5: 'brawling', 6: 'blade'}, 'Army': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'gambling', 5: 'brawling', 6: 'education'} , 'Scouts': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'gun', 5: 'intelligence', 6: 'education'} , 'Merchants': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'strength', 5: 'blade', 6: 'bribery'}, 'Others': {1 : 'strength', 2 : 'dexterity',3 : 'endurance', 4: 'blade', 5: 'brawling', 6: 'social_standing'}}

service_skills = {'Navy': {1 : 'ships_boat', 2 : 'vacc_suit',3 : 'forward_observer', 4: 'blade', 5: 'gun', 6: 'gunnery' }, 'Marines': {1 : 'atv', 2 : 'vacc_suit',3 : 'blade', 4: 'blade', 5: 'gun', 6: 'gun'}, 'Army': {1 : 'atv', 2 : 'air_raft',3 : 'forward_observer', 4: 'blade', 5: 'gun', 6: 'gun'} , 'Scouts': {1 : 'air_raft', 2 : 'vacc_suit',3 : 'navigation', 4: 'mechanic', 5: 'electronic', 6: 'J_o_T'} , 'Merchants': {1 : 'steward', 2 : 'vacc_suit',3 : 'strength', 4: 'gun', 5: 'electronic', 6: 'J_o_T'}, 'Others': {1 : 'forgery', 2 : 'gambling',3 : 'brawling', 4: 'blade', 5: 'gun', 6: 'bribery'}}

advanced_education =  {'Navy': {1 : 'vacc_suit', 2 : 'mechanic',3 : 'electronic', 4: 'engineering', 5: 'gunnery', 6: 'J_o_T' }, 'Marines': {1 : 'atv', 2 : 'mechanic',3 : 'electronic', 4: 'tactics', 5: 'blade', 6: 'gun'}, 'Army': {1 : 'atv', 2 : 'mechanic',3 : 'electronic', 4: 'tactics', 5: 'blade', 6: 'gun'} , 'Scouts': {1 : 'air_raft', 2 : 'mechanic',3 : 'electronic', 4: 'J_o_T', 5: 'gunnery', 6: 'medical'} , 'Merchants': {1 : 'streetwise', 2 : 'mechanic',3 : 'electronic', 4: 'navigation', 5: 'gunnery', 6: 'medical'}, 'Others': {1 : 'streetwise', 2 : 'mechanic', 3 : 'electronic', 4: 'gambling', 5: 'brawling', 6: 'forgery'}}

advanced_higher_education =  {'Navy': {1 : 'medical', 2 : 'navigation',3 : 'engineering', 4: 'computer', 5: 'pilot', 6: 'admin' }, 'Marines': {1 : 'medical', 2 : 'tactics',3 : 'tactics', 4: 'computer', 5: 'leadership', 6: 'admin'}, 'Army': {1 : 'medical', 2 : 'tactics',3 : 'tactics', 4: 'computer', 5: 'leadership', 6: 'admin'} , 'Scouts': {1 : 'medical', 2 : 'navigation',3 : 'engineering', 4: 'computer', 5: 'pilot', 6: 'J_o_T'} , 'Merchants': {1 : 'medical', 2 : 'navigation',3 : 'engineering', 4: 'computer', 5: 'pilot', 6: 'admin'}, 'Others': {1 : 'medical', 2 : 'forgery', 3: 'electronic', 4:  'computer', 5: 'streetwise', 6: 'J_o_T'}}

skills_tables = [personal_development, service_skills, advanced_education, advanced_higher_education ]

mustering_out_benefits_table =  {'Navy': {1 : 'Low_Psg', 2 : 'Intelligence +1', 3 : 'Education +2 ', 4: 'Blade', 5: 'Travellers', 6: 'High_Psg', 7: 'Social_Standing +2'  }, 'Marines': {1 : 'Low_Psg', 2 : 'Intelligence +2',3 : 'Education +1', 4: 'Blade', 5: 'Travellers', 6: 'High_Psg', 7: 'Social_Standing +2' }, 'Army': {1 : 'Low_Psg', 2 : 'Intelligence +1',3 : 'Education +2', 4: 'Gun', 5: 'High_Psg', 6: 'Mid_Psg', 7: 'Social_Standing +1' } , 'Scouts': {1 : 'Low_Psg', 2 : 'Intelligence +2',3 : 'Education +2', 4: 'Blade', 5: 'Gun', 6: 'Scout'}, 'Merchants': {1 : 'Low_Psg', 2 : 'Intelligence + 1', 3 : 'Education +1', 4: 'Gun', 5: 'Blade', 6: 'Low_Psg', 7: 'Merchant'  }, 'Others': {1 : 'Low_Psg', 2 : 'Intelligence +1', 3: 'Education +2', 4:  'Gun', 5: 'High_Psg', 6: '--'}}

def two_d6():
    return random.randint(1, 6) + random.randint(1, 6)

def one_d6():
    return random.randint(1, 6)

dm_data = (('enlist', 'Navy', 'intelligence', 8, 1), ('enlist', 'Navy', 'education', 9, 2), ('enlist', 'Marines', 'intelligence', 8, 1), ('enlist', 'Marines', 'strength', 8, 2) , ('enlist', 'Army', 'dexterity', 6, 1), ('enlist', 'Army', 'endurance', 5, 2), ('enlist', 'Scouts', 'intelligence', 6, 1), ('enlist', 'Scouts', 'strength', 8, 2), ('enlist', 'Merchants', 'strength', 7, 1), ('enlist', 'Merchants', 'intelligence', 6, 2))

class Character:
    def __init__(self, number):
        self.number = number
        self.alive = True
        self.enlisted = False
        self.first_choice = None
        self.service = None
        self.initial_service = None
        self.commissioned = False
        self.career = None
        self.terms = 0
        self.age = 18
        self.rank = 0
        self.skills = 0
        self.notional_skills_cap = 0
        self.attribute_increase = 0
        self.initial_strength = two_d6()
        self.initial_endurance = two_d6()
        self.initial_dexterity = two_d6()
        self.initial_intelligence = two_d6()
        self.initial_education = two_d6()
        self.initial_social_standing = two_d6()
        self.strength = self.initial_strength
        self.endurance = self.initial_endurance
        self.dexterity = self.initial_dexterity
        self.intelligence = self.initial_intelligence
        self.education = self.initial_education
        self.social_standing = self.initial_social_standing
        self.brawling = 0
        self.gun = 0
        self.blade = 0
        self.mechanic = 0
        self.engineering = 0
        self.electronic = 0
        self.computer = 0
        self.admin = 0
        self.medical = 0
        self.steward = 0
        self.atv = 0
        self.air_raft = 0
        self.ships_boat = 0
        self.pilot = 0
        self.navigation = 0
        self.gunnery = 0
        self.vacc_suit = 0
        self.leadership = 0
        self.tactics = 0
        self.forward_observer = 0
        self.streetwise = 0
        self.gambling = 0
        self.bribery = 0
        self.forgery = 0
        self.J_o_T = 0
        self.end_of_service_reason = None
        self.material_benefits = []
        self.cash_benefits_count = 0
        self.reason_a = 0
        self.reason_b = 0
        self.reason_c = 0
        self.reason_d = 0
        self.retirement_request_reason = 'None'
        self.reenlist_choice = True
        self.character_attributes = [['strength',  self.strength], ['endurance', self.endurance], ['dexterity', self.dexterity], ['intelligence', self.intelligence], ['education', self.education], ['social_standing', self.social_standing]]
        self.enlistment_roll_mod = 0

    def dice_modifier(self, roll_for, char_service):
        modifier = 0
        for a in self.character_attributes:
            for index, tup in enumerate(dm_data):
                if tup[0] == roll_for and tup[1] == char_service:
                    if a[0] == tup[2] and a[1] >= tup[3]:
                        modifier += tup[4]
        return modifier

    def career_arc(self):
        self.choose_career()
        self.term()
        self.mustering_out()

#    def career_decision(self):
#        career_list = ['Navy', 'Marines', 'Army', 'Scouts', 'Merchants', 'Others']
#        [print(x) for x in career_list

    def choose_career(self):
        self.first_choice = random.choice(('Navy', 'Marines', 'Army', 'Scouts', 'Merchants', 'Others'))
#       print("You have applied to join the " + choice)
        enlistment_roll = two_d6()
        enlistment_roll += self.dice_modifier('enlist', self.first_choice) # self.character_attributes # )
#       self.enlistment_roll_mod += self.dice_modifier('enlist',  self.first_choice) # self.character_attributes # )
#       enlistment_roll += self.dice_modifier('enlist', choice, self.character_attributes)
#       checksum.append(self.dice_modifier('enlist', choice, self.character_attributes))
#       self.enlistment_roll_mod += self.dice_modifier('enlist', choice, self.character_attributes)
#       if (choice == 'Army' and self.dexterity >= 6): enlistment_roll += 1
#       if (choice == 'Scouts' and self.intelligence >= 6): enlistment_roll += 1
#       if (choice == 'Merchants' and self.strength>= 7): enlistment_roll += 1
#       if (choice == 'Navy' and self.education >= 9): enlistment_roll += 2
#       if (choice == 'Marines' and self.strength >= 8): enlistment_roll += 2
#       if (choice == 'Army' and self.endurance >= 5): enlistment_roll += 2
#       if (choice == 'Scouts' and self.strength >= 8): enlistment_roll += 2
#       if (choice == 'Merchants' and self.intelligence >= 6): enlistment_roll += 2
        if enlistment_roll >= service_rolls[self.first_choice]['Enlist']:
            self.career = self.first_choice
            self.initial_service = "contract"
            self.service = self.initial_service
#           print("You have successfully enlisted in the " + self.career)
        else:
            # draft
            self.career = random.choice(('Navy', 'Marines', 'Army', 'Scouts', 'Merchants', 'Others'))
            self.initial_service = "draft"
            self.service = self.initial_service
#           print("you have been drafted into the " + self.career)

    def set_attr(self, attr, buff):
            new_val = getattr(self, attr) + buff
            setattr(self, attr, new_val)
#       print(str(attr) + " has improved by " + str(buff))

    def resolve_skills(self):
        if self.education >= 8:
            skill_table = random.choice(skills_tables[0:3])
        else:
            skill_table = random.choice(skills_tables[0:2])
        skill_roll = one_d6()
        attr = skill_table[self.career][skill_roll]
        char_attributes = ['strength', 'endurance', 'dexterity', 'intelligence', 'education', 'social_standing']
        if (attr in char_attributes ):
            self.attribute_increase += 1
        self.set_attr(attr, 1)

    def new_term(self):
        # survival roll
        self.survival_check(self)
        # commissioning
        # promotion
        # skills
        # ageing

    def survival_check(self):
        survival_roll = two_d6()
        if (self.career == 'Navy' and self.intelligence >= 7): survival_roll += 2
        if (self.career == 'Marines' and self.endurance >= 8): survival_roll += 2
        if (self.career == 'Army' and self.education >= 6): survival_roll += 2
        if (self.career == 'Scouts' and self.endurance >= 9): survival_roll += 2
        if (self.career == 'Merchants' and self.intelligence >= 7): survival_roll += 2
        if (self.career == 'Others' and self.intelligence >= 9): survival_roll += 2
        if (survival_roll >= service_rolls[self.career]['Survive']):
            self.alive = True

    def term(self):
        skills = 0
        if self.service == 'contract':
            skills += self.commission()
            skills += self.promotion()
            skills += 1
            self.notional_skills_cap +=1
            if self.terms == 0:
                skills += 1
                self.notional_skills_cap += 1
            if self.career == 'Army':
                self.gun += 1
                self.notional_skills_cap += 1
            if self.career == 'Marines':
                self.blade += 1
                self.notional_skills_cap += 1
            if self.career == 'Scouts':
                self.pilot += 1
                self.notional_skills_cap += 1
            for s in range(skills):
                self.resolve_skills()
                skills -= 1
            self.terms += 1
            self.age = 18 + self.terms * 4
            self.ageing_process()
            self.reenlistment()
        else:
            self.alive = False
            self.end_of_service_reason = "Death in Service"
#           print("sadly you didn't make it")

    def filterA(self):
        # ageing becomeing a problem
        if 4 <= self.terms <= 11:
            early_ageing_attributes = [self.strength, self.endurance, self.dexterity]
            for ea in early_ageing_attributes:
                if ea < 3:
                    self.reenlist_choice = False
                    self.reason_a += 1
        elif self.terms > 12:
            late_ageing_attributes = [self.strength, self.endurance, self.dexterity, self.intelligence]
            for la in late_ageing_attributes:
                if la < 3:
                    self.reenlist_choice = False
                    self.reason_a += 1

    def filterB(self):
        # re-enlistment chances poor
        if (self.career == 'Navy' and self.intelligence < 7):
            self.reenlist_choice = False
            self.reason_b += 1
        if (self.career == 'Marines' and self.endurance < 8):
            self.reenlist_choice = False
            self.reason_b += 1
        if (self.career == 'Army' and self.education < 6):
            self.reenlist_choice = False
            self.reason_b += 1
        if (self.career == 'Scouts' and self.endurance < 9):
            self.reenlist_choice = False
            self.reason_b += 1
        if (self.career == 'Merchants' and self.intelligence < 7):
            self.reenlist_choice = False
            self.reason_b += 1
        if (self.career == 'Others' and self.intelligence < 9):
            self.reenlist_choice = False
            self.reason_b += 1

#    def filterC(self):
#        if (self.career == 'Scouts' or self.commissioned == False):
#            if (self.terms >= 6):
#                self.reenlist_choice = False
#                self.set_attr('reason_c', 1)
#            elif (self.terms >= 10):
#                self.reenlist_choice = False
#                self.set_attr('reason_c', 1)

    def filterD(self):
       # Maximum term covered by ageing rules
        if (self.terms == 14):
            self.reenlist_choice = False
            self.set_attr('reason_d', 1)

    def reenlistment_decision(self):
        self.reenlist_choice = True
        self.filterA()
#        self.filterB()
#        self.filterC()
        self.filterD()
        if self.reason_a > 0 and self.reason_b > 0:
            self.retirement_request_reason = 'Ageing & Survival Chances'
        elif self.reason_b > 0 and self.reason_c > 0:
            self.retirement_request_reason = 'Survival Chances and Time Served'
        elif self.reason_a > 0 and self.reason_c > 0:
            self.retirement_request_reason = 'Ageing & Time Served'
        elif self.reason_a > 0 and self.reason_b > 0 and self.reason_c > 0:
            self.retirement_request_reason = 'Ageing, Survival Chances & Time Served'
        elif self.reason_a > 0:
            self.retirement_request_reason = 'Ageing'
        elif self.reason_b > 0:
            self.retirement_request_reason = 'Survival chances'
        elif self.reason_c > 0:
            self.retirement_request_reason = 'Time Served'
        elif self.reason_d > 0:
            self.retirement_request_reason = 'Maximum age'
        else:
            self.retirement_request_reason = 'None'

    def reenlistment(self):
        if self.alive == False:
            return
#       reenlistment_choice = input("Do you want to reenlist? ")
#       for auto generated characters we assume the character wants to re-enlist
        self.reenlistment_decision()
        # level 0 filter a character will not re-enlist if doing so runs the risk of taking any attribute below 2
        reenlistment_roll = two_d6()
        if (reenlistment_roll == 12 and self.reenlist_choice == False):
#       print("You have been pressed back into service in time of need")
            self.service = 'contract'
            self.term()
        elif (reenlistment_roll >= service_rolls[self.career]['Reenlistment'] and self.reenlist_choice == True):
#           print("You have reenlisted for another term")
            self.service = 'contract'
            self.term()
        elif (reenlistment_roll < service_rolls[self.career]['Reenlistment'] and self.reenlist_choice == True):
#           print("The service no longer has need of your service, and you are offered retirement")
            self.end_of_service_reason = "Services no longer required"
        elif (reenlistment_roll < 12 and self.reenlist_choice == False):
            self.end_of_service_reason = "Granted Retirement"

    def commission(self):
        skills = 0
        if (self.commissioned == False and self.career != 'Others' and self.career != 'Scouts' and self.service != 'draft') :
            commission_roll = two_d6()
            if (self.career == 'Navy' and self.social_standing >= 9): commission_roll += 1
            if (self.career == 'Marines' and self.education >= 7): commission_roll += 1
            if (self.career == 'Army' and self.endurance >= 7): commission_roll += 1
            if (self.career == 'Merchants' and self.intelligence >= 6): commission_roll += 1
            if (commission_roll >= service_rolls[self.career]['Commission']):
                self.commissioned = True
                self.rank = 1
                skills += 1
                self.notional_skills_cap += 1
                if self.career == 'Army':
                    self.gun += 1
                    self.notional_skills_cap += 1
                if self.career == 'Marines':
                    self.gun += 1
                    self.notional_skills_cap += 1
        return skills

    def promotion(self):
        skills = 0
        if self.commissioned == True:
            if (self.career != 'Merchants' and self.rank < 6) or (self.career == 'Merchants' and self.rank < 5) :
                promotion_roll = two_d6()
                if (self.career == 'Navy' and self.education >= 8): promotion_roll += 1
                if (self.career == 'Marines' and self.social_standing >= 8): promotion_roll += 1
                if (self.career == 'Army' and self.education >= 7): promotion_roll += 1
                if (self.career == 'Merchants' and self.intelligence >= 9): promotion_roll += 1
                if (promotion_roll >= service_rolls[self.career]['Promotion']):
#                   print('you have been promoted')
                    self.rank += 1
                    skills += 1
                    self.notional_skills_cap +=1
                    if (self.career == 'Navy' and self.rank == 5): self.social_standing += 1
                    if (self.career == 'Navy' and self.rank == 6): self.social_standing += 1
                    if (self.career == 'Merchants' and self.rank == 4):
                        self.pilot += 1
                        self.notional_skills_cap +=1
        return skills

    def ageing_process(self):
        if (self.terms > 3 and self.terms < 8 ):
            if (two_d6() < 8): self.strength -= 1
            if (two_d6() < 7): self.dexterity -= 1
            if (two_d6() < 8): self.endurance -= 1
        elif (self.terms > 8 and self.terms < 11 ):
            if (two_d6() < 9): self.strength -= 1
            if (two_d6() < 8): self.dexterity -= 1
            if (two_d6() < 9): self.endurance -= 1
        elif ( self.terms > 11 and self.terms < 15):
            if (two_d6() < 9): self.strength -= 2
            if (two_d6() < 8): self.dexterity -= 2
            if (two_d6() < 9): self.endurance -= 2
            if (two_d6() < 9): self.intelligence -= 1
        ageing_attributes = [self.strength, self.endurance, self.dexterity, self.intelligence]
        for aa in ageing_attributes:
            if aa < 1:
                self.alive = False
                self.end_of_service_reason = "You died in service owing to the effects of old age"

    def mustering_out(self):
        if(self.alive):
            mustering_out_rolls = self.terms
            if (self.commissioned == True and self.rank <3 ): mustering_out_rolls += 1
            elif(self.rank >=3 ): mustering_out_rolls += 2
            split = random.randint(0,1)
            self.cash_benefits_count = min(mustering_out_rolls * split, 3)
            material_benefits_count = mustering_out_rolls - self.cash_benefits_count
            self.material_benefits = []
            for i in range(material_benefits_count):
                muster_roll = one_d6()
                if (self.rank >= 5): muster_roll += 1
                self.material_benefits.append(mustering_out_benefits_table[self.career][muster_roll])
            for i in self.material_benefits:
                if i == "Social_Standing +2":
                    self.social_standing += 2
                    self.attribute_increase += 2
                if i == "Social_Standing +1":
                    self.social_standing += 1
                    self.attribute_increase += 1
                if i == "Intelligence +2":
                    self.intelligence += 2
                    self.attribute_increase += 2
                if i == "Intelligence +1":
                    self.intelligence += 1
                    self.attribute_increase += 1
                if i == "Education +2":
                    self.education += 2
                    self.attribute_increase += 2
                if i == "Education +1":
                    self.education += 1
                    self.attribute_increase += 1

    def print_character(self):
        print(int(self.strength) , int(self.endurance) , int(self.dexterity) , int(self.intelligence) , int(self.education)  ,  int(self.social_standing) , end=" ")
        print(self.career)

        print("Terms " + str(self.terms))
        print("Rank " + str(self.rank))

    def total_stats(self):
        return self.strength + self.endurance + self.dexterity + self.intelligence + self.education + self.social_standing

    def total_skills(self):
        return self.brawling + self.gun + self.blade + self.mechanic + self.engineering + self.electronic + self.computer + self.admin + self.medical + self.steward + self.atv + self.air_raft + self.ships_boat + self.pilot + self.navigation + self.gunnery + self.vacc_suit + self.leadership + self.tactics + self.forward_observer + self.streetwise + self.gambling + self.bribery + self.forgery + self.J_o_T

    def to_dict(self):
        return {
            'number': self.number,
            'first_choice' : self.first_choice,
            'career': self.career,
            'initial term': self.initial_service,
            'service type': self.service,
            'commissioned': self.commissioned,
            'total stats': self.total_stats(),
            'total skills': self.total_skills(),
            'attribute increase': self.attribute_increase,
            'skill opportunities': self.total_skills() + self.attribute_increase,
            'init_strength': self.initial_strength,
            'init_endurance': self.initial_endurance,
            'init_dexterity': self.initial_dexterity,
            'init_intelligence': self.initial_intelligence,
            'init_education': self.initial_education,
            'init_social_standing': self.initial_social_standing,
            'strength': self.strength,
            'endurance': self.endurance,
            'dexterity': self.dexterity,
            'intelligence': self.intelligence,
            'education': self.education,
            'social_standing': self.social_standing,
            'rank': self.rank,
            'terms': self.terms,
            'age': self.age,
            'alive': self.alive,
            'retirement reason': self.retirement_request_reason,
            'end_of_service': self.end_of_service_reason,
            'brawling': self.brawling,
            'gun': self.gun,
            'blade': self.blade,
            'mechanic': self.mechanic,
            'engineering': self.engineering,
            'electronic': self.electronic,
            'computer': self.computer,
            'admin': self.admin,
            'medical': self.medical,
            'steward': self.steward,
            'atv': self.atv,
            'air_raft': self.air_raft,
            'ships_boat': self.ships_boat,
            'pilot': self.pilot,
            'navigation': self.navigation,
            'gunnery': self.gunnery,
            'vacc_suit': self.vacc_suit,
            'leadership': self.leadership,
            'tactics': self.tactics,
            'forward_observer': self.forward_observer,
            'streetwise': self.streetwise,
            'gambling': self.gambling,
            'bribery': self.bribery,
            'forgery': self.forgery,
            'J_o_T' : self.J_o_T,
            'material benefits': self.material_benefits,
            'count of cash benefits': self.cash_benefits_count,
            'skills_cap_check': self.notional_skills_cap,
            'reasonA': self.reason_a,
            'reasonB': self.reason_b,
            'reasonC': self.reason_c,
            'mod': self.enlistment_roll_mod
        }

characters = []

run_size = 200000

for i in range(run_size):
    characters.append(Character(i))

for i in range(run_size):
    characters[i].career_arc()

df = pandas.DataFrame.from_records([s.to_dict() for s in characters])

# print(df.describe(include = 'all'))

df_is_alive = df['alive'] == True

#print(df_is_alive.describe(include = "all"))

df.to_excel(r"C:\Users\Mike\Desktop\Traveller_New.xlsx", index = False, header=True)















