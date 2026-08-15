import math

Border = "-"*30

##################################################
#
#  Function : Euclidean Distance
#
##################################################

def MarvellousEuc(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X'])**2 + (P1['Y'] - P2['Y'])**2)
    return Ans

##################################################
#
#  Function : Manual KNN Classifier (K = 3)
#
##################################################

def MarvellousKNNClassifier():

    Data = [
        {'point':'A','X':1, 'Y':2,'label':'Red'},
        {'point':'B','X':2, 'Y':3,'label':'Red'},
        {'point':'C','X':3, 'Y':1,'label':'Blue'},
        {'point':'D','X':6, 'Y':5,'label':'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    # Accept new point from user
    x = int(input("Enter X coordinate : "))
    y = int(input("Enter Y coordinate : "))

    new_point = {'X':x,'Y':y}

    # Calculate Euclidean distance from all dataset points
    for d in Data:
        d['distance'] = MarvellousEuc(d,new_point)

    # Sort the distances
    sorted_data = sorted(Data,key = lambda item : item['distance'])

    k = 3
    nearest = sorted_data[:k]

    print("Nearest Neighbors :")
    for d in nearest:
        print(d['point'],"- Distance:",round(d['distance'],2))

    print(Border)

    # Majority Voting
    votes = {}
    for neighbors in nearest:
        label = neighbors['label']
        votes[label] = votes.get(label,0) + 1

    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Predicted Class:",Name)
    print(Border)

def main():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()
