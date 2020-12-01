

def deal_into_new_stack(old):
    size = len(old)
    new = [None]*size
    for i in range(size):
        new[i] = old[size-i-1]
    # print(new)
    return new

def deal_into_new_stack_index(size, index):
    new = size - index - 1
    return new

def cut(n, old):
    new = old[n:] + old[:n]
    # print(new)
    return new

def cut_index(n, size, index):
    while n < 0:
        n += size
    if index < n:
        new = index + size - n
    else:
        new = index - n
    return new

def deal_with_increment(n, old):
    size = len(old)
    new = [None]*size
    for i in range(size):
        new[(i*n)%size] = old[i]
    # print(new)
    return new

def deal_with_increment_index(n, size, index):
    new = (index * n) % size
    return new

def shuffle(techniques, old):
    new = old
    for technique in techniques:
        if technique.startswith('deal into new stack'):
            print('deal into new stack')
            new = deal_into_new_stack(new)

        elif technique.startswith('cut'):
            n = int(technique[4:])
            print('cut', n)
            new = cut(n, new)

        elif technique.startswith('deal with increment'):
            n = int(technique[20:])
            print('deal with increment', n)
            new = deal_with_increment(n, new)

    return new

def shuffle_index(techniques, size, index):
    new = index
    for technique in techniques:
        if technique.startswith('deal into new stack'):
            # print('deal into new stack')
            new = deal_into_new_stack_index(size, new)

        elif technique.startswith('cut'):
            n = int(technique[4:])
            # print('cut', n)
            new = cut_index(n, size, new)

        elif technique.startswith('deal with increment'):
            n = int(technique[20:])
            # print('deal with increment', n)
            new = deal_with_increment_index(n, size, new)
    return new


test1 = '''deal with increment 7
deal into new stack
deal into new stack
'''

test2 = '''cut 6
deal with increment 7
deal into new stack
'''

test3 = '''deal with increment 7
deal with increment 9
cut -2
'''

test4 = '''deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1
'''

# old = [0,1,2,3,4,5,6,7,8,9]
# techniques = test4.strip().split('\n')
# new = shuffle(techniques, old)
# print(new)




f = open("day22.txt", "r")
techniques = f.read().strip().split('\n')
f.close()

# Part1
# old = [x for x in range(10007)]
# new = shuffle(techniques, old)
# for i in range(len(new)):
#     if new[i] == 2019:
#         print(i)
#         break

# Part2
index = 2010
#      119315717514047
size = 20
times = 101741582076661
count = 0
new = index
while count < times:
    count += 1
    old = new
    new = shuffle_index(techniques, size, old)
    print("count:", count, new)
    if new == index:
        break
print(new)

# 1e11 * 1       21216765755.0
# 1e11 * 2      121216765755.0
# 1e11 * 3       21216765755.0
# 1e11 * 4      321216765755.0
# 1e11 * 5      221216765755.0
# 1e11 * 6      321216765755.0
# 1e11 * 7      421216765755.0
# 1e11 * 8      321216765755.0
# 1e11 * 9       21216765755.0

# 9
# 1e12 * 1      721216765755
# 1e12 * 2      721216765755
# 1e12 * 3     2721216765755
# 1e12 * 4     2721216765755
# 1e12 * 5     2721216765755
# 1e12 * 6     2721216765755
# 1e12 * 7     6721216765755
# 1e12 * 8     2721216765755
# 1e12 * 9     2721216765755

# 1e12+1e13    9721216765755

# 1
# 1e13 * 1     2721216765755.0
# 1e13 * 2     2721216765755.0
# 1e13 * 3     2721216765755.0
# 1e13 * 4     2721216765755.0
# 1e13 * 5    32721216765755.0
# 1e13 * 6     2721216765755.0
# 1e13 * 7    62721216765755.0
# 1e13 * 8     2721216765755.0
# 1e13 * 9     2721216765755.0

# 1e13+1e14   42721216765755

# 1
# 1e14 * 1    82721216765755.0
# 1e14 * 2    82721216765755.0


