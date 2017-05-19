__DEBUG__ = False


"""
We get two multisets and the task is to find optimal Range for the this sets.
As example, if R(S1) > R(S2), so the optimal Range is R(S1).
And we have k steps. Moving one number is -1 step. If we are out of steps, we can't do anything.
"""


### Range of set S
def R(S):
    return max(S) - min(S)


### Inserting data, checking if this is stress test
if __DEBUG__:
    from random import randint

    n1 = randint(1, 100000)
    S1 = sorted(list({randint(-1e9, 1e9) for i in range(n1)}))
    n2 = randint(1, 100000)
    S2 = sorted(list({randint(-1e9, 1e9) for i in range(n2)}))
    k = randint(1, 1e9)
else:
    n1 = int(input())
    S1 = sorted(list(map(int, input().split())))
    n2 = int(input())
    S2 = sorted(list(map(int, input().split())))
    k = int(input())

### I want S1 to have the biggest number
if max(S2) > max(S1):
    S1, S2 = S2, S1

"""
Now the logic is the next:
We have two sets of numbers. They are sorted (We sorted it). In this case, we can
say, that they are overlapping, because the minimum of set, which has the biggest number (S1),
is smaller, than maximum of another set (S2):
(_____S2____(~~overlapping~~)____S1____)
First of all, we send all the overlapping elements from S1 to S2. In case, if there is
the same element in both sets, we send them to S2.
After that we have two not overlapping sets. We check what set has bigger Range.
Then we use some indicator in set with bigger Range and try to find in which case the situation
with Range changes. Some picture:
     S2             S1
(X X X X X X)__(X X X X X X )       <-- two not overlapping sets
                  ^
                  |        <-- indicator in the case R(S1) > R(S2)
"""
element = 0
MAX_S2 = max(S2)
while k and S1[element] < MAX_S2:
    k -= 1
    element += 1

S2 += S1[:element]
S2.sort()
S1 = S1[element:]

element = 0
while k and S1[0] == S2[-element-1]:
    k -= 1
    element += 1
element += 1
S1 = S2[element:] + S1
S2 = S2[:element]


if __DEBUG__:
    assert(S1 == sorted(S1))
    assert(S2 == sorted(S2))
    assert(S1[0] > S2[-1])

### We can use the fact, that sets are sorted
if R(S1) > R(S2):
    element = 0
    while k and S1[element]-S2[0] < S1[-1]-S1[element]:
        k -= 1
        element += 1
    answer = min(max(S1[element]-S2[0], S1[-1]-S1[element]), max(S1[element-1]-S2[0], S1[-1]-S1[element-1]))
elif R(S2) > R(S1):
    element = -1
    while k and S2[element] - S2[0] > S1[-1] - S2[element]:
        k -= 1
        element -= 1
    answer = min(max(S2[element] - S2[0], S1[-1] - S2[element]), max(S2[element+1] - S2[0], S1[-1] - S2[element+1]))
else:
    answer = 0

if not __DEBUG__:
    print(answer)