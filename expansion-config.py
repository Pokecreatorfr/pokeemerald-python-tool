def disasemble_definition(line):
    if line.find('#define') != -1 :
        previous_is_space = False
        a = 0
        variable = ''
        value = ''
        for i in range(len(line) - line.find('#define')):
            if line[line.find('#define') + i ] != ' ' and previous_is_space == True :
                a = line.find('#define') + i 
                if variable != '':
                    value = line[a :]
                    if line.endswith('\n'):
                        value = value[:len(value) - 1]
                    if value.find('//') != -1:
                        value = value[:value.find('//')]
                    return variable , value.replace(' ' , '')
                previous_is_space = False
            if line[line.find('#define') + i ] == ' ':
                if a != 0 and variable == '':
                        variable = line[a : line.find('#define') + i ]
                        a = 0
                previous_is_space = True
            if line.find('#define') + i == len(line) - 1:
                if a != 0 and variable =='':
                    variable = line[a :]
                if variable.endswith('\n'):
                        variable = variable[:len(variable) - 1]
                return variable , value
    else :
        print(line)
        return None

with open('include/constants/species.h') as f:
    filelist = [line for line in f]

species_list = []

for i in range(len(filelist)):
    if filelist[i].find('#define') != -1 :
        species_list.append(disasemble_definition(filelist[i]))

filelist = []

with open('src/data/text/species_names.h') as f:
    filelist = [line for line in f]

print(species_list[0])

names_list = []

for i in range(len(filelist)):
    for x in range(len(species_list)):
        if filelist[i][filelist[i].find('[') + 1 : filelist[i].find(']')] == species_list[x][0]:
            names_list.append( [species_list[x][0] , filelist[i][filelist[i].find('_("') + 3: filelist[i].find('"),')] ])

filelist = []

with open('src/data/pokemon/base_stats.h') as f:
    filelist = [line for line in f]

run = False
spe = False
spestep = 0
steps = ['.baseHP' , '.baseAttack' , '.baseDefense' , '.baseSpeed' , '.baseSpAttack' , '.baseSpDefense' , '.type1' , '.type2' , '.catchRate' , '.expYield' , '.evYield_SpAttack' , '.genderRatio' , '.eggCycles' , '.friendship' ,'.growthRate' , '.eggGroup1' , '.eggGroup2' , '.abilities' , '.bodyColor' , '.noFlip']
stats = []
basestats = []

for i in range(len(filelist)):
    if run == False and filelist[i].find('const struct BaseStats gBaseStats[]') != -1:
        run = True
    if run == True:
        if spe == False:
            stats = []
            if filelist[i].find('[SPECIES_') != -1 :
                stats.append(filelist[i][filelist[i].find('SPECIES_') : filelist[i].find('SPECIES_') + filelist[i][filelist[i].find('SPECIES_') : ].find("]")])
                spe = True
                spestep = 0
                if filelist[i].find('{0}') != -1 :
                    spe = False
                    basestats.append(stats)
        else:
            if filelist[i].find(steps[spestep]) != -1:
                spestep += 1
                stats.append(filelist[i][filelist[i].find('=') + 1 : len(filelist[i]) - 1]) 
                if spestep == 20:
                    spe = False
                    for x in range(len(stats)):
                        if stats[x].endswith(','):
                            stats[x] = stats[x][:len(stats[x]) - 1]
                        if stats[x].startswith(' '):
                            stats[x] = stats[x][1:]
                    basestats.append(stats)


filelist = []

with open('include/constants/moves.h') as f:
    filelist = [line for line in f]

moves_list = []

for i in range(len(filelist)):
    if filelist[i].find('#define') != -1 :
        moves_list.append(disasemble_definition(filelist[i]))



print(moves_list)