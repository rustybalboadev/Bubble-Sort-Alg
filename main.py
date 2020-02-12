#Seperate each number by a ','
bubblesInput = input("Make the list of numbers: ")
bubbles = bubblesInput.split(',')
bubbles = list(map(int, bubbles))
last_num = 0
times = 0
while times != len(bubbles):
    for x in range(0, len(bubbles)):
        if last_num > bubbles[x] and x != 0:
            bubble1 = bubbles[x-1]
            bubble2 = bubbles[x]
            bubbles[x] = bubble1
            bubbles[x-1] = bubble2
            print("Switched! New List: {}".format(bubbles))
        else:
            last_num = bubbles[x]
    times += 1
