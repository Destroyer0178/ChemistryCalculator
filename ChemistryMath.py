import mendeleev as M

#Calculates the molar mass of a molecule and the mass percentage of each element in it
def GetMolarMass(elements):
    mass = 0
    element_count = {}
    keys = []
    for i in range(len(elements)):
        try:
            temp = M.element(elements[i])
            mass += M.element(elements[i]).atomic_weight
            index = len(element_count)
            element_count = AddElementCount(temp,element_count)
            if index < len(element_count):
                keys.append(temp)
        except Exception:
            temp_elements = GetElements(elements[i])
            if len(temp_elements) > 0:
                for m in range(len(temp_elements)):
                    mass += temp_elements[m].atomic_weight
                    index = len(element_count)
                    elemen_count = AddElementCount(temp_elements[m],element_count)
                    if index < len(element_count):
                        keys.append(temp_elements[m])
    result = "Molar mass = " + str(round(mass,2)) + " g/mol" + GetMassPercentage(mass, element_count, keys)
    return result

#Adds either a new element to the dictionary or adds 1 to an existing element
#Used to find how much of each element is in the molecule
def AddElementCount(element, count):
    if element not in count:
        count.update({element:1})
    else:
        count[element] += 1
    return count

#Calculates how much of each element is in the molecule by percent mass
def GetMassPercentage(mass, count, keys):
    if len(count) == 0:
        return " "
    result = ""
    for i in range(len(count)):
        percent = round((((count[keys[i]] * keys[i].atomic_weight)/mass)*100),2)
        result += "\n" + str(percent) + "% " + keys[i].symbol
    return result

#Checks if a string is an element
def CheckElement(text):
    try:
        M.element(text)
        return True
    except Exception:
        return False

#checks if a string is or contains a number
def ContainsNumber(text):
    return any(i.isdigit() for i in text)

#checks if the inputted string actually contains real elements
#returns the elements that are contained * the numbers written after them
#currently only works with single digit numbers, will fix it later
def GetElements(text):
    elements = []
    for i in range(len(text)):
        if i < len(text)-1 and CheckElement(text[i]+text[i+1]):
            elements.append(M.element(text[i]+text[i+1]))
            if i < len(text)-3 and ContainsNumber(text[i+2]) and ContainsNumber(text[i+3]):
                for i in range(int(text[i+2]+text[i+3])-1):
                    elements.append(elements[len(elements)-1])
            else:
                skip = True
            if i < len(text)-2 and ContainsNumber(text[i+2]) and skip == True:
                    for i in range(int(text[i+2])-1):
                        elements.append(elements[len(elements)-1])
        else:
            try:
                elements.append(M.element(text[i]))
                if i < len(text)-2 and ContainsNumber(text[i+1]) and ContainsNumber(text[i+2]):
                    for e in range(int(text[i+1]+text[i+2])-1):
                        elements.append(elements[len(elements)-1])
                else:
                    skip = True
                if i < len(text)-1 and ContainsNumber(text[i+1]) and skip == True:
                    for e in range(int(text[i+1])-1):
                        elements.append(elements[len(elements)-1])
            except Exception:
                continue
    return elements
