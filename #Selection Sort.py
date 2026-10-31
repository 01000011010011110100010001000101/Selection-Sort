#Selection Sort
import random
def SelectionSort(List):
    
    for j in range(len(List)):
        Min = j
        for i in range(Min + 1 , len(List)):
            if List[Min] >= List[i]:
                Min = i

        List[j] , List[Min] = List[Min] , List[j]
       

    return List


List = []

for i in range(10):
    List.append(random.randint(1,10))
print(SelectionSort(List))