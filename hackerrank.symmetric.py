if __name__ == "__main__":
    a=int(input().strip())
    s1=set(map(int,input().strip().split()))
    b = int(input().strip())
    s2=set(map(int,input().strip().split()))
    for j in sorted(s1^s2):
        
        print(j)
