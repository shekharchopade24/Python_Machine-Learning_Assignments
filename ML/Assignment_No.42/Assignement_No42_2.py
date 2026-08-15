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
#  Function : KNN Prediction for Changing K
#
##################################################

def MarvellousKNNChangingK():

    Data = [
        {'point':'A','X':1, 'Y':2,'label':'Red'},
        {'point':'B','X':2, 'Y':3,'label':'Red'},
        {'point':'C','X':3, 'Y':1,'label':'Blue'},
        {'point':'D','X':6, 'Y':5,'label':'Blue'}
    ]

    new_point = {'X':2,'Y':2}

    # Calculate Euclidean distance from all dataset points
    for d in Data:
        d['distance'] = MarvellousEuc(d,new_point)

    # Sort the distances
    sorted_data = sorted(Data,key = lambda item : item['distance'])

    print(Border)
    print("Prediction Results")
    print(Border)

    k_values = [1,3,5]

    for k in k_values:

        nearest = sorted_data[:k]

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

        print("K =",k,"->",Name)

    print(Border)

    # Explanation :
    # As K increases, more neighbors (including farther points) are
    # considered for Majority Voting. With a small K, prediction depends
    # only on the closest 1 or 2 points, but as K grows, distant points
    # belonging to the other class can outnumber the near ones, which
    # changes the Predicted Class.

def main():
    MarvellousKNNChangingK()

if __name__ == "__main__":
    main()
