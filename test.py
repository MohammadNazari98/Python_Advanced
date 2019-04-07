import textwrap
import re
import string
from fractions import gcd
import functools
from collections import deque
import math
#------------------------------------------------------------>Python<---------------------------------------------------
class All_program_of_code_signal_site:
    def Test(self):
        s = [()]
        res = [False] * 2
        if s:
            res[0] = True
        if s[0]:
            res[1] = True
        #output: [True,False]
    def Test2(self,L,X,Y,R):
        if L < X ** Y <= R: # 1
            ...
        if X ** Y > L and X ** Y < R: # 2
            ...
        if X ** Y in range(L+1,R+1): # 3
            ...
        # Option 1 is the most optimal one.
    def Test3(self,a,b,c):
      #  c = (a == not b) # error because It isn't Parentheses.
        c = not a == b # It not error and it works.
        c = not(a == b) # It not error and it works.
        a == (not b) # It not error and it works.
    def division(self,x,y): #python
        return x // y
        # int division(int x,int y) # java
        #{
            # return x / y;
        #}
    #--------------------->option x = 15 , y = -14 <----------------------------------------
    def countBits(self,n):
        return n.bit_length()
    def modulus(self,n):
        if n is not float(n):
            return n % 2
        else:
            return -1
    def simpleSort(self,arr):
        n = len(arr)
        for i in range(n):
            j = 0
            stop = n - i
            while j < stop - 1:
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                j += 1
        return arr
    def baseConversion(self,n, x):
        return hex(int(str(n), x))[2:]
    def mexFunction(self,s, upperBound):
        found = -1
        for i in range(upperBound):
            if not i in s:
                found = i
                break
        else:
            found = upperBound
        return found
    def listBeautifier(self,a):
        res = a[:]
        while res and res[0] != res[-1]:
            first, *res, last = res
        return res
    def Test5(self,s):
        s = 'abacaba' # True
        s = "abacaba" # True
    #      s = ''abacaba'' # False because it doesn't accept two single or double.
    #     s = ""abacaba"" #false because it doesn't accept two single or double.
        s = """abacaba""" # True
        s = '''abacaba''' #True
    def fixMessage(self,message):
        return message.capitalize()
    def catWalk(self,code):
        return " ".join(code.split())
    def convertTabs(self,code, x):
        return code.replace('\t', ' ' * x)
    def feedbackReview(self,feedback, size):
        return [] if feedback == "" else textwrap.fill(feedback, width=size).split('\n')
    def isWordPalindrome(self,word):
        return word == word[::-1]
    def permutationCipher(self,password, key):
        table = password.maketrans("".join(chr(97 + i) for i in range(0, 26)), key)
        return password.translate(table)
    def competitiveEating(self,t, width, precision):
        return '{:^{}.{}f}'.format(t, width, precision)
    def newStyleFormatting(self,s):
        s = re.sub('%%', '{%}', s)
        s = re.sub('%[dfFgeEGnnxXodcbs]', '{}', s)
        return re.sub('{%}', '%', s)
    def getCommit(self,commit):
        return re.sub(r"[?+0!]", "", commit)
    def Test6(self):
        # 1.list a repeated b times
        # 2.list b repeated a times?
        #----------------------->Yes to both options <------------------------------------
        return "Yes to both options."
    def listsConcatenation(self,lst1, lst2):
        res = lst1
        res.append(lst2)
        return res
    def twoTeams(self,students):
        return sum(students[::2]) - sum(students[1::2])
    def removeTasks(self,k, toDo):
        del toDo[k - 1::k]
        return toDo
    def printList(self,lst):
        return "This is your list: {}".format(lst)
    def Test7(self):
        repeatChar = lambda x, n: x * n
        return repeatChar
    def getPoints(self,answers, p):
        questionPoints = lambda i, ans: i + 1 if ans == True else -p
        res = 0
        for i, ans in enumerate(answers):
            res += questionPoints(i, ans)
        return res
    def sortStudents(self,students):
        students.sort(key=lambda x: x.split()[-1:])
        return students
    def isTestSolvable(self,ids, k):
        digitSum = lambda s: sum(list(map(int, list(str(s)))))
        sm = 0
        for questionId in ids:
            sm += digitSum(questionId)
        return sm % k == 0
    def createSpiralMatrix(self,n):
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        curDir = 0
        curPos = (n - 1, n - 1)
        res = [[' '] * n]
        for i in range(1, n * n + 1):
            res[curPos[0]][curPos[1]] = i
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
            if not (0 <= nextPos[0] < n and  0 <= nextPos[1] < n and res[nextPos[0]][nextPos[1]] == 0):
                curDir = (curDir + 1) % 4
                nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
            curPos = nextPos
        return res
    def constructShell(self,n):
        return [[0] * x for x in range(n)][1::] + [[0] * x for x in range(n + 1)[:0:-1]]
    def wordPower(self,word):
        num = dict({k: string.ascii_lowercase.find(k) + 1 for k in word})
        return sum([num[ch] for ch in word])
    def coolPairs(self,a, b):
        uniqueSums = {x + y for x in a for y in b if (x * y) % (x + y) == 0}
        return len(uniqueSums)
    def multiplicationTable(self,n):
        return [[i * j for i in range(1, n + 1)] for j in range(1, n + 1)]
    def chessTeams(self,smarties, cleveries):
        return [[smarties[i], cleveries[j]] for i in range(len(smarties)) for j in range(len(cleveries)) if i == j]
    def fixResult(self,result):
        def fix(x):
            return x // 10
        return list(map(fix, result))
    def collegeCourses(self,x, courses):
        def shouldConsider(course):
            return len(course) != x
        return list(filter(shouldConsider, courses))
    def createHistogram(self,ch, assignments):
        return [ch * i for i in assignments]
    def leastCommonDenominator(self,denominators):
        return functools.reduce(lambda x, y: x * y // gcd(x, y), denominators)
    def Test8(self):
        #1.set
        #2.frozenset
        #3.tuple of mutable objects
        #4.tuple of immutable object
        #5.list of mutable objects
        #6.list of immutable objects
        #Which of them can be used as dictionary keys?
        print("Objects 2 and 4.")
    def uniqueCharacters(self,document):
        return sorted(set(list(chr(ord(document[i])) for i in range(len(document)))))
    def correctScholarships(self,bestStudents, scholarships, allStudents):
        return set(bestStudents) <= set(scholarships) < set(allStudents)
    def startupName(self,companies):
        cmp1 = set(companies[0])
        cmp2 = set(companies[1])
        cmp3 = set(companies[2])
        res = functools.reduce((lambda set1, set2: set1 | set2), [set(company) for company in companies]) - functools.reduce(
            (lambda set1, set2: set1 ^ set2), [set(company) for company in companies])
        return list(sorted(list(res)))
    def wordsRecognition(self,word1, word2):
        def getIdentifier(w1, w2):
            return ''.join(sorted(list(set(w1) - set(w2)), key=lambda x: ord(x)))
        return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
    def transposeDictionary(self,scriptByExtension):
        return sorted([(i[1], i[0]) for i in scriptByExtension.items()])
    def doodledPassword(self,digits):
        n = len(digits)
        res = [deque(digits) for _ in range(n)]
        deque(map(lambda i: res[i].rotate(n - i), range(n)), 0)
        return [list(d) for d in res]
    #================================================================================================================
    #------------------------------------------>Intro<---------------------------------------------------------------
    def add(self,param1, param2):
        resualt = param1 + param2
        return resualt
    def centuryFromYear(self,year):
        if year % 100 == 0:
            century = (year // 100)
            return century
        else:
            return (year // 100) + 1
    def checkPalindrome(self,inputString):
        x = len(inputString)
        if inputString == inputString[::-1]:
            return True
        else:
            return False
    def adjacentElementsProduct(self,inputArray):
        length = len(inputArray)
        sum = []
        for i in range(length - 1):
            sum.append(inputArray[i] * inputArray[i + 1])
        return max(sum)
    def shapeArea(self,n):
      return ((n*n)+((n-1)*(n-1)))
    def makeArrayConsecutive2(self,statues):
        return max(statues) - min(statues) - len(statues) + 1
    def almostIncreasingSequence(self,sequence):
        return 3> sum((i >= j) + (i >= k) for i, j, k in zip(sequence, sequence[1:], sequence[2:] + [10**6]))
    def matrixElementsSum(self,matrix):
        result = 0
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[j][i] == 0:
                    break
                result += matrix[j][i]
        return result
#=======================================================================================================================
# ------------------------------------------>The Core<------------------------------------------------------------------
    def addTwoDigits(self,n):
        if n >= 10 and n <= 99:
            answer = 0
            while n > 0:
               r = n % 10
               answer = answer + r
               n = int(n//10)
            return answer
    def largestNumber(self,n):
       return int(math.pow(10,n)-1)
    def candies(self,n, m):
        return m - m % n
    def seatsInTheater(self,nCols, nRows, col, row):
        return (nCols - col + 1) * (nRows - row)
    def maxMultiple(self,divisor, bound):
        return bound - bound % divisor
a = All_program_of_code_signal_site()

