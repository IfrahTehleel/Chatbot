import aiml

# create kernel files and learn aiml files
global sentence
global nounList, verbList


def getSentenceFromBot():
    kernel = aiml.Kernel()
    kernel.learn("udc.aiml")
    kernel.learn("clothee.aiml")

    while True:
        sentence = input("HUMAN:  ")
        print(kernel.respond(sentence))


getSentenceFromBot()
