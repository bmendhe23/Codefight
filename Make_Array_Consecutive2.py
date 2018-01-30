def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1


# another way more logical to do

def makeArrayConsecutive2(statues):
    new_array = list(range(min(statue),max(statues)+1))
    return len(new_array)-len(statues)
