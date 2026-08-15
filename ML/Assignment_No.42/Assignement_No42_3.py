import math

Border = "-"*30

##################################################
#
#  Function : Euclidean Distance (StudyHours, Attendance)
#
##################################################

def MarvellousStudentEuc(P1,P2):
    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours'])**2 + (P1['Attendance'] - P2['Attendance'])**2)
    return Ans

##################################################
#
#  Function : Student Pass/Fail KNN Classifier
#
##################################################

def MarvellousStudentKNN():

    Data = [
        {'StudyHours':2, 'Attendance':60, 'Result':'Fail'},
        {'StudyHours':5, 'Attendance':80, 'Result':'Pass'},
        {'StudyHours':6, 'Attendance':85, 'Result':'Pass'},
        {'StudyHours':1, 'Attendance':50, 'Result':'Fail'}
    ]

    print(Border)
    print("Marvellous Student KNN Classifier")
    print(Border)

    for i in Data:
        print(i)

    print(Border)

    # Accept input from user
    sh = float(input("Enter Study Hours: "))
    att = float(input("Enter Attendance: "))

    new_point = {'StudyHours':sh,'Attendance':att}

    # Calculate Euclidean distance from all dataset points
    for d in Data:
        d['distance'] = MarvellousStudentEuc(d,new_point)

    # Sort the distances
    sorted_data = sorted(Data,key = lambda item : item['distance'])

    k = 3
    nearest = sorted_data[:k]

    # Majority Voting
    votes = {}
    for neighbors in nearest:
        label = neighbors['Result']
        votes[label] = votes.get(label,0) + 1

    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print(Border)
    print("Predicted Result:",Name)
    print(Border)

def main():
    MarvellousStudentKNN()

if __name__ == "__main__":
    main()
