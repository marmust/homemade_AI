# you: mom can we have AI?
# mom: no we have AI at home.
# AI at home:

ans = float(input("ans: "))
train = int(input("train: "))
agr = float(input("agression: "))

weightN1 = 1
weightN2 = 1
weightN3 = 1
weightN4 = 1
weightN5 = 1

for x in range (train):
    # SINGLE NEURONE 1
    inputN1I1 = 1
    inputN1I2 = 1

    avarage = (inputN1I1 + inputN1I2) / 2
    neuronOutN1 = avarage * weightN1

    if neuronOutN1 <= ans:
        weightN1 = weightN1 + agr
    if neuronOutN1 >= ans:
        weightN1 = weightN1 - agr
    # SINGLE NEURONE 1

    # SINGLE NEURONE 2
    inputN2I1 = 0
    inputN2I2 = 1

    avarage = (inputN2I1 + inputN2I2) / 2
    neuronOutN2 = avarage * weightN2

    if neuronOutN2 <= ans:
        weightN2 = weightN2 + agr
    if neuronOutN2 >= ans:
        weightN2 = weightN2 - agr
    # SINGLE NEURONE 2

    # SINGLE NEURONE 3
    inputN3I1 = 0
    inputN3I2 = 0

    avarage = (inputN3I1 + inputN3I2) / 2
    neuronOutN3 = avarage * weightN3

    if neuronOutN3 <= ans:
        weightN3 = weightN3 + agr
    if neuronOutN3 >= ans:
        weightN3 = weightN3 - agr
    # SINGLE NEURONE 3

    # L2

    # SINGLE NEURONE 4
    inputN4I1 = neuronOutN1
    inputN4I2 = neuronOutN2

    avarage = (inputN4I1 + inputN4I2) / 2
    neuronOutN4 = avarage * weightN4

    if neuronOutN4 <= ans:
        weightN4 = weightN4 + agr
    if neuronOutN4 >= ans:
        weightN4 = weightN4 - agr
    # SINGLE NEURONE 4

    # SINGLE NEURONE 5
    inputN5I1 = neuronOutN2
    inputN5I2 = neuronOutN3

    avarage = (inputN5I1 + inputN5I2) / 2
    neuronOutN5 = avarage * weightN5

    if neuronOutN5 <= ans:
        weightN5 = weightN5 + agr
    if neuronOutN5 >= ans:
        weightN5 = weightN5 - agr
    # SINGLE NEURONE 5

    # OUTPUT NEURONE ----------------------------------------------------------------------

    inputN6I1 = neuronOutN4
    inputN6I2 = neuronOutN5

    avarage = (inputN6I1 + inputN6I2) / 2
    neuronOutN6 = avarage

    # OUTPUT NEURONE ----------------------------------------------------------------------

# RESULTS

print("------------------------------------------------------")
print("RESULT:")
print(neuronOutN6)
print("------------------------------------------------------")
print("FOUND PARAMETERS:")
print("weight 1: " + str(weightN1))
print("weight 2: " + str(weightN2))
print("weight 3: " + str(weightN3))
print("weight 4: " + str(weightN4))
print("weight 5: " + str(weightN5))
print("------------------------------------------------------")

# RESULTS

# TRIAL

print("INSERT FOUND PARAMETERS TO TEST:")

# SINGLE NEURONE 1
inputN1I1 = 1
inputN1I2 = 1

avarage = (inputN1I1 + inputN1I2) / 2
neuronOutN1 = avarage * float(input("weight 1: "))
# SINGLE NEURONE 1

# SINGLE NEURONE 2
inputN2I1 = 0
inputN2I2 = 1

avarage = (inputN2I1 + inputN2I2) / 2
neuronOutN2 = avarage * float(input("weight 2: "))
# SINGLE NEURONE 2

# SINGLE NEURONE 3
inputN3I1 = 0
inputN3I2 = 0

avarage = (inputN3I1 + inputN3I2) / 2
neuronOutN3 = avarage * float(input("weight 3: "))
# SINGLE NEURONE 3

# L2

# SINGLE NEURONE 4
inputN4I1 = neuronOutN1
inputN4I2 = neuronOutN2

avarage = (inputN4I1 + inputN4I2) / 2
neuronOutN4 = avarage * float(input("weight 4: "))
# SINGLE NEURONE 4

# SINGLE NEURONE 5
inputN5I1 = neuronOutN2
inputN5I2 = neuronOutN3

avarage = (inputN5I1 + inputN5I2) / 2
neuronOutN5 = avarage * float(input("weight 5: "))
# SINGLE NEURONE 5

# OUTPUT NEURONE ----------------------------------------------------------------------

inputN6I1 = neuronOutN4
inputN6I2 = neuronOutN5

avarage = (inputN6I1 + inputN6I2) / 2
neuronOutN6 = avarage

# OUTPUT NEURONE ----------------------------------------------------------------------
print("------------------------------------------------------")
print("TEST RESULT:")
print(neuronOutN6)