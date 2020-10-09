import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim


# install matplotlib using (pip install matplotlib)
# if you are using linux run this 
# sudo apt-get install --reinstall libxcb-xinerama0


def swap(A, i, j):
    a = A[j]
    A[j] = A[i]
    A[i] = a

# this is buble sort algo 
def sort_buble(arr):
    if (len(arr) == 1):
        return
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if (arr[j] > arr[j + 1]):
                swap(arr, j, j + 1)
            yield arr
def insertion_sort(arr):
    if(len(arr)==1):
        return
    for i in range(1,len(arr)):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            swap(arr,j,j-1)
            j-=1
            yield arr

def quick_Sort(arr,p,q):
    if(p>=q):
        return
    piv = arr[q]
    pivindx = p
    for i in range(p,q):
        if(arr[i]<piv):
            swap(arr,i,pivindx)
            pivindx+=1
        yield arr
    swap(arr,q,pivindx)
    yield arr

    yield from quick_Sort(arr,p,pivindx-1)
    yield from quick_Sort(arr,pivindx+1,q)

def selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[min]):
                min=j
            yield arr
        if(min!=i):
            swap(arr,i,min)
            yield arr

def merge_sort(arr,lb,ub):
    if(ub<=lb):
        return
    elif(lb<ub):
        mid =(lb+ub)//2
        yield from merge_sort(arr,lb,mid)
        yield from merge_sort(arr,mid+1,ub)
        yield from merge(arr,lb,mid,ub)
        yield arr

def merge(arr,lb,mid,ub):
    new = []
    i = lb
    j = mid+1
    while(i<=mid and j<=ub):
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    if(i>mid):
        while(j<=ub):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[lb+i] = val
        yield arr

def heapify(arr,n,i):
    largest = i
    l = i*2+1
    r = i*2+2
    while(l<n and arr[l]>arr[largest]):
        largest = l
    while(r<n and arr[r]>arr[largest]):
        largest = r
    if(largest!=i):
        swap(arr,i,largest)
        yield arr
        yield from heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n,-1,-1):
        yield from heapify(arr,n,i)
    for i in range(n-1,0,-1):
        swap(arr,0,i)
        yield  arr
        yield from heapify(arr,i,0)

def shell_sort(arr):
    sublistcount = len(arr) // 2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        yield  from gap_InsertionSort(arr, start_position, sublistcount)
      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap
            yield nlist

        nlist[position]=current_value
        yield nlist

def count_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m

    for a in arr:
        count[a] += 1
        yield arr
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
            yield arr
        yield  arr



n = int(input("Enter the number of elements:"))
print("\n 1.Bubble \n 2.Insertion \n 3.Quick \n 4.Selection \n 5.Merge Sort \n 6.Heapify \n 7.Shell \n 8.Count sort \n")
al = int(input("Choose algorithm: "))
array = [i + 1 for i in range(n)]
random.shuffle(array)

if(al==1):
    title = "Bubble Sort"
    algo = sort_buble(array)
elif(al==2):
    title = "Insertion Sort"
    algo = insertion_sort(array)
elif(al==3):
    title = "Quick Sort"
    algo = quick_Sort(array,0,n-1)
elif(al==4):
    title="Selection Sort"
    algo = selection_sort(array)
elif (al == 5):
    title = "Merge Sort"
    algo=merge_sort(array,0,n-1)
elif (al == 6):
    title = "Heap Sort"
    algo = heap_sort(array)
elif (al == 7):
    title = "Shell Sort"
    algo = shell_sort(array)
elif (al == 8):
    title = "Count Sort"
    algo = count_sort(array)
else:
    print("Please enter a number from list")
# Initialize fig
fig, ax = plt.subplots()
ax.set_title(title)

bar_rec = ax.bar(range(len(array)), array, align='edge')

ax.set_xlim(0, n)
ax.set_ylim(0, int(n * 1.1))

text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]


def update_plot(array, rec, epochs):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))


anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()
