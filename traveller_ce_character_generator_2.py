import random
# import timeit
import pandas as pd

personal_development = {'Navy': {1: 'str', 2: 'dex', 3: 'end', 4: 'soc', 5: 'int', 6: 'edu'},
                        'Marines': {1: 'str', 2: 'dex', 3: 'end', 4: 'gambling', 5: 'brawling', 6: 'blade'},
                        'Army': {1: 'str', 2: 'dex', 3: 'end', 4: 'gambling', 5: 'brawling', 6: 'edu'},
                        'Scouts': {1: 'str', 2: 'dex', 3: 'end', 4: 'gun', 5: 'int', 6: 'edu'},
                        'Merchants': {1: 'str', 2: 'dex', 3: 'end', 4: 'str', 5: 'blade', 6: 'bribery'},
                        'Others': {1: 'str', 2: 'dex', 3: 'end', 4: 'blade', 5: 'brawling', 6: 'soc'}}

service_skills = {'Navy': {1: 'ships_boat', 2: 'vacc_suit', 3: 'forward_observer', 4: 'blade', 5: 'gun', 6: 'gunnery'},
                  'Marines': {1: 'atv', 2: 'vacc_suit', 3: 'blade', 4: 'blade', 5: 'gun', 6: 'gun'},
                  'Army': {1: 'atv', 2: 'air_raft', 3: 'forward_observer', 4: 'blade', 5: 'gun', 6: 'gun'},
                  'Scouts': {1: 'air_raft', 2: 'vacc_suit', 3: 'navigation', 4: 'mechanic', 5: 'electronic',
                             6: 'J_o_T'},
                  'Merchants': {1: 'steward', 2: 'vacc_suit', 3: 'atv', 4: 'gun', 5: 'electronic', 6: 'J_o_T'},
                  'Others': {1: 'forgery', 2: 'gambling', 3: 'brawling', 4: 'blade', 5: 'gun', 6: 'bribery'}}

advanced_education = {
    'Navy': {1: 'vacc_suit', 2: 'mechanic', 3: 'electronic', 4: 'engineering', 5: 'gunnery', 6: 'J_o_T'},
    'Marines': {1: 'atv', 2: 'mechanic', 3: 'electronic', 4: 'tactics', 5: 'blade', 6: 'gun'},
    'Army': {1: 'atv', 2: 'mechanic', 3: 'electronic', 4: 'tactics', 5: 'blade', 6: 'gun'},
    'Scouts': {1: 'air_raft', 2: 'mechanic', 3: 'electronic', 4: 'J_o_T', 5: 'gunnery', 6: 'medical'},
    'Merchants': {1: 'streetwise', 2: 'mechanic', 3: 'electronic', 4: 'navigation', 5: 'gunnery', 6: 'medical'},
    'Others': {1: 'streetwise', 2: 'mechanic', 3: 'electronic', 4: 'gambling', 5: 'brawling', 6: 'forgery'}}

advanced_higher_education = {
    'Navy': {1: 'medical', 2: 'navigation', 3: 'engineering', 4: 'computer', 5: 'pilot', 6: 'admin'},
    'Marines': {1: 'medical', 2: 'tactics', 3: 'tactics', 4: 'computer', 5: 'leadership', 6: 'admin'},
    'Army': {1: 'medical', 2: 'tactics', 3: 'tactics', 4: 'computer', 5: 'leadership', 6: 'admin'},
    'Scouts': {1: 'medical', 2: 'navigation', 3: 'engineering', 4: 'computer', 5: 'pilot', 6: 'J_o_T'},
    'Merchants': {1: 'medical', 2: 'navigation', 3: 'engineering', 4: 'computer', 5: 'pilot', 6: 'admin'},
    'Others': {1: 'medical', 2: 'forgery', 3: 'electronic', 4: 'computer', 5: 'streetwise', 6: 'J_o_T'}}

skills_tables = [personal_development, service_skills, advanced_education, advanced_higher_education]

mustering_out_benefits_table = {
    'Navy': {1: 'Low_Psg', 2: 'Intelligence +1', 3: 'Education +2 ', 4: 'Blade', 5: 'Travellers', 6: 'High_Psg',
             7: 'Social_Standing +2'},
    'Marines': {1: 'Low_Psg', 2: 'Intelligence +2', 3: 'Education +1', 4: 'Blade', 5: 'Travellers', 6: 'High_Psg',
                7: 'Social_Standing +2'},
    'Army': {1: 'Low_Psg', 2: 'Intelligence +1', 3: 'Education +2', 4: 'Gun', 5: 'High_Psg', 6: 'Mid_Psg',
             7: 'Social_Standing +1'},
    'Scouts': {1: 'Low_Psg', 2: 'Intelligence +2', 3: 'Education +2', 4: 'Blade', 5: 'Gun', 6: 'Scout'},
    'Merchants': {1: 'Low_Psg', 2: 'Intelligence + 1', 3: 'Education +1', 4: 'Gun', 5: 'Blade', 6: 'Low_Psg',
                  7: 'Merchant'},
    'Others': {1: 'Low_Psg', 2: 'Intelligence +1', 3: 'Education +2', 4: 'Gun', 5: 'High_Psg', 6: '--'}}

def two_d6():
    return random.randint(1, 6) + random.randint(1, 6)

def one_d6():
    return random.randint(1, 6)

def one_d4():
    return random.randint(1, 4)

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)


cgl = pd.read_excel(r"C:\Users\Mike\Desktop\traveller_character_generator_data.xlsx", sheet_name='Sheet1')
cgm = pd.read_excel(r"C:\Users\Mike\Desktop\traveller_character_generator_data.xlsx", sheet_name='Sheet2')

cgl['key1'] = cgl['career'] + "_" + cgl['context']
cgm['key2'] = cgm['career'] + "_" + cgm['context']

cgl.set_index('key1', inplace=True)
cgm.set_index('key2', inplace=True)

upp_pos = [0, 1, 2, 3, 4, 5]
upp_abbr = ["str", "dex", "end", "int", "edu", "soc"]

def level_table_lookup(career, context):
    match = career + "_" + context
    return cgl.loc[match].at['level']

class Character:
    def __init__(self, number):
        self.unwise_to_reenlist = False
        self.career_choice = None
        self.number = number
        self.alive = True
        self.enlistment = None
        self.service = None
        self.career = None
        self.term = 0
        self.age = 18
        self.rank = 0
        self.skills = 0
        self.end_of_service_reason = None
        self.attribute_increase = 0
        self.aged = False

        self.init_str = two_d6()
        self.init_dex = two_d6()
        self.init_end = two_d6()
        self.init_int = two_d6()
        self.init_edu = two_d6()
        self.init_soc = two_d6()

        self.str = self.init_str
        self.dex = self.init_dex
        self.end = self.init_end
        self.int = self.init_int
        self.edu = self.init_edu
        self.soc = self.init_soc

        self.total_attributes = self.str + self.dex + self.end + self.int + self.edu + self.soc

        self.material_benefits = []

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
        self.air_raft = 0
        self.atv = 0
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

        self.skills_table_history = [0,0,0,0]

        self.char_dict = {'str': self.str, 'dex': self.dex, 'end': self.end, 'int': self.int, 'edu': self.edu,
                          'soc': self.soc}

    def modifier_table_lookup(self, career, context):
        dm = 0
        temp_df = cgm[(cgm.career == career) & (cgm.context == context)]
        char_list = temp_df['characteristic'].to_list()
        level_list = temp_df['level'].to_list()
        dm_list = temp_df['dm'].to_list()
        j = 0
        for i in char_list:
            if self.char_dict[i] >= level_list[j]:
                dm += dm_list[j]
            j += 1
        return dm

    def roll_to_enlist(self):
        self.career_choice = random.choice(('Navy', 'Marines', 'Army', 'Scouts', 'Merchants', 'Others'))
        #        print('choice ' + self.career_choice)
        if (self.career_choice == 'Navy' and self.int < 7) : self.career_choice = 'Army'
        if (self.career_choice == 'Marines' and self.end < 8): self.career_choice = 'Army'
        if (self.career_choice == 'Scouts' and self.end < 9): self.career_choice = 'Army'
        if (self.career_choice == 'Merchants' and self.int < 7): self.career_choice = 'Army'
        if (self.career_choice == 'Others' and self.int < 9): self.career_choice = 'Army'
        if self.career_choice == 'Army' and self.edu < 6:
            if self.int == 7:
                if self.str >= 7:
                    self.career_choice = 'Merchants'
            elif self.int >= 8:
                    self.career_choice = 'Navy'

        roll_required = level_table_lookup(self.career_choice, 'enlistment')
        roll = two_d6()
        dm = self.modifier_table_lookup(self.career_choice, 'enlistment')
        #        print(str(roll_required) + " " + str(roll) + " " + str(dm) )
        roll += dm
        if (roll >= roll_required):
            self.career = self.career_choice
            self.enlistment = 'contract'
            self.service = 'contract'
        #            print('contract ' + self.career)
        else:
            self.career = random.choice(('Navy', 'Marines', 'Army', 'Scouts', 'Merchants', 'Others'))
            self.enlistment = 'draft'
            self.service = 'draft'
        #            print('draft ' + self.career)

        if self.career == 'Army': self.gun += 1
        if self.career == 'Marine': self.blade += 1
        if self.career == 'Scouts': self.pilot += 1
        self.skills += 1

    def roll_to_survive(self):
        career = self.career
        roll_required = level_table_lookup(career, 'survival')
        roll = two_d6()
        dm = self.modifier_table_lookup(career, 'survival')
        #        print('survival roll')
        #        print(str(roll_required) + " " + str(roll) + " " + str(dm) )
        roll += dm
        if dm == 0 : self.unwise_to_reenlist = True
        self.term += 1
        self.skills += 1
        if self.career == 'Scouts': self.skills += 1
        if (roll >= roll_required):
            self.alive = True
        #            print('will survive term ' + str(self.term))
        else:
            self.end_of_service_reason = 1
            #            print('Died in service during term ' + str(self.term))
            self.alive = False

    def roll_for_commission(self):
        career = self.career
        if career != 'Scouts' and career != 'Others':
            if self.rank == 0 and self.service != 'draft':
                roll_required = level_table_lookup(career, 'commission')
                roll = two_d6()
                dm = self.modifier_table_lookup(career, 'commission')
                #                print('commissions board')
                #                print(str(roll_required) + " " + str(roll) + " " + str(dm))
                roll += dm
                if (roll >= roll_required):
                    self.rank = 1
                    #  print('commissioned as an officer in the ' + self.career + ' during term ' + str(self.term))
                    if self.career == 'Army' or self.career == 'Marines':
                        self.skills += 1
                        self.gun += 1
                    else:
                        self.skills += 1

    #                else:
    #                    print('not commissioned')

    def roll_for_promotion(self):
        career = self.career
        if career == 'Merchants':
            max_rank = 5
        else:
            max_rank = 6
        if (self.rank >= 1 and self.rank < max_rank):  # grrr this still needs to be changed for merchants!
            roll_required = level_table_lookup(career, 'promotion')
            roll = two_d6()
            dm = self.modifier_table_lookup(career, 'promotion')
            #            print('promotion board')
            #            print(str(roll_required) + " " + str(roll) + " " + str(dm) )
            roll += dm
            if (roll >= roll_required):
                self.rank += 1
                #                print('promoted to rank ' + str(self.rank) + ' during term ' + str(self.term))
                if self.career == 'Merchants' and self.rank == 4:
                    #            print('do we get here?...................................................................................................')
                    self.skills += 1
                    self.pilot += 1
                elif self.career == 'Navy' and self.rank >= 5:
                    self.soc += 1
                else:
                    self.skills += 1

    #            else:
    #                print('passed over for promotion')

    def resolve_skills(self):
        for s in range(self.skills):
            choices = [0, 1, 2, 3]
            if self.edu < 8:
                choices = [0, 1 ,2]
                self.skills_table_history_used = self.skills_table_history[0:3]
            else: self.skills_table_history_used = self.skills_table_history[0:4]
            n = len(choices)
            difference = False
#           x.count(x[0]) == len(x)
            if (n == 4 and self.skills_table_history_used.count(self.skills_table_history_used[0]) != 4):
                difference = True
            if (n == 3 and self.skills_table_history_used.count(self.skills_table_history_used[0]) != 3):
                difference = True
            if (difference == True):
                print(choices)
                max_val = max(self.skills_table_history_used)
                print(self.edu)
                print(self.skills_table_history)
                print(self.skills_table_history_used)
                print(max_val)
                indices_of_max_val = [i for i in range(len(self.skills_table_history_used)) if self.skills_table_history_used[i] == max_val ]
                print(indices_of_max_val)
                choices = [x for x in choices if x not in indices_of_max_val]
                print(choices)
                print("\n")
            choice = random.choice(choices)
            skill_table = skills_tables[choice]
            # find the skill table or tables most rolled on so far and take them out of consideration
            skill_roll = one_d6()
            attr = skill_table[self.career][skill_roll]
            self.set_attr(attr, 1)
            self.skills -= 1
            self.skills_table_history[choice] += 1

    def set_attr(self, attr, buff):
            new_val = getattr(self, attr) + buff
            setattr(self, attr, new_val)

    def ageing_process(self):
        if self.alive == True:
            if (self.term > 3 and self.term < 8):
                if (two_d6() < 8):
                    self.str -= 1
                    self.aged = True
                if (two_d6() < 7):
                    self.dex -= 1
                    self.aged = True
                if (two_d6() < 8):
                    self.end -= 1
                    self.aged = True
            elif (self.term > 8 and self.term < 11):
                if (two_d6() < 9):
                    self.str -= 1
                    self.aged = True
                if (two_d6() < 8):
                    self.dex -= 1
                    self.aged = True
                if (two_d6() < 9):
                    self.end -= 1
                    self.aged = True
            elif (self.term > 11 and self.term < 15):
                if (two_d6() < 9):
                    self.str -= 2
                    self.aged = True
                if (two_d6() < 8):
                    self.dex -= 2
                    self.aged = True
                if (two_d6() < 9):
                    self.end -= 2
                    self.aged = True
                if (two_d6() < 9):
                    self.int -= 1
                    self.aged = True
            else:
                self.end_of_service_reason = 3
            ageing_attributes = [self.str, self.end, self.dex, self.int]
            for a in ageing_attributes:
                if a < 1:
                    #                    print("Died in service owing to the effects of old age")
                    self.end_of_service_reason = 2
                    self.alive = False

    def roll_to_re_enlist(self):
        if self.alive == True:
            career = self.career
            roll_required = level_table_lookup(career, 're-enlistment')
            roll = two_d6()
            #            print(str(roll_required) + " " + str(roll))
            if (roll == 12):
                #                print('compulsory re-enlistment')
                self.service = 'contract'
                self.serve_term()
            elif (roll >= roll_required and (self.aged == False or self.unwise_to_reenlist)):
                #                print('sucessful re-enlistment')
                self.service = 'contract'
                self.serve_term()

    #            else:
    #               print('services no longer required')
    #               print('mustered out with ' + str(self.skills) + ' skills')
    #               print("\n")

    def mustering_out(self):
        if self.alive:
            mustering_out_rolls = self.term
            if self.rank  > 0 and self.rank <3 : mustering_out_rolls += 1
            elif self.rank >=3 : mustering_out_rolls += 2
            split = random.randint(0, 1)
            self.cash_benefits_count = min(mustering_out_rolls * split, 3)
            material_benefits_count = mustering_out_rolls - self.cash_benefits_count
            self.material_benefits = []
            for i in range(material_benefits_count):
                muster_roll = one_d6()
                if (self.rank >= 5): muster_roll += 1
                self.material_benefits.append(mustering_out_benefits_table[self.career][muster_roll])
            for i in self.material_benefits:
                if i == "Social_Standing +2":
                    self.soc += 2
                    self.attribute_increase += 2
                if i == "Social_Standing +1":
                    self.soc += 1
                    self.attribute_increase += 1
                if i == "Intelligence +2":
                    self.int += 2
                    self.attribute_increase += 2
                if i == "Intelligence +1":
                    self.int += 1
                    self.attribute_increase += 1
                if i == "Education +2":
                    self.edu += 2
                    self.attribute_increase += 2
                if i == "Education +1":
                    self.edu += 1
                    self.attribute_increase += 1

    def serve_term(self):
        self.roll_to_survive()
        self.roll_for_commission()
        self.roll_for_promotion()
        self.resolve_skills()
        self.ageing_process()
        self.roll_to_re_enlist()  # handles characters who died in previous phases also

    def to_dict(self):
        return {
            'number': self.number,
            'str': self.str,
            'dex': self.dex,
            'end': self.end,
            'int': self.int,
            'edu': self.edu,
            'soc': self.soc,
            'total attributes': self.total_attributes,
            'init str': self.init_str,
            'init dex': self.init_dex,
            'init end': self.init_end,
            'init int': self.init_int,
            'init edu': self.init_edu,
            'init soc': self.init_soc,
            'first_choice': self.career_choice,
            'career': self.career,
            'initial enlistment': self.enlistment,
            'service type': self.service,
            'rank': self.rank,
            'terms': self.term,
            'alive': self.alive,
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
            'J_o_T': self.J_o_T,
            'material benefits': self.material_benefits,
            'skills_table_history': self.skills_table_history
        }

characters = []

run_size = 100

for i in range(run_size):
    characters.append(Character(i))

for i in range(run_size):
    #    print(characters[i].char_dict)
    characters[i].roll_to_enlist()
    characters[i].serve_term()
    characters[i].mustering_out()
#    print('\n')

df_out = pd.DataFrame.from_records([s.to_dict() for s in characters])
df_out.to_excel(r"C:\Users\Mike\Desktop\Traveller_New14.xlsx", index=False, header=True)

#   characters[i].muster_out()

#   generate blank character data sheet
#   generate characteristics
#   enlistment
#   first_term
#       specifics to first term
#           extra skill for first term,
#           service specific skills,
#           ineligibility for commission if drafted
#       each term thereafter
#           check survival,
#           commission
#           promotion
#           skill up
#           ageing effects
#   mustering out

#   data
#       enlistment rolls        # service / attributes / levels / dms
#       survival rolls          # service / attribute / level
#       commissioning rolls     # service / attribute / level
#       promotion rolls         # service / attribute / level
#       re-enlistment rolls     # service / attribute / level

# data structures

# 'the roll' takes the following parameters:
# Context / Table (e.g. 'enlistment', 'survival', etc. )
# Career('Navy', 'Marines', etc.)
# Characteristic ('str', 'dex', etc.)

# 'the DM' takes the following parameters
# 'the roll' - there can be one or more DMs applicable to each roll
#  dms can be accessed through a look-up of their 'roll' or through a composite key of 'context' and 'career'
