def TowerOfHanoi(n , source, destination, inter):
    if n==1:
        print("Move disk 1 from ",source,"to ",destination)
        return
    TowerOfHanoi(n-1, source, inter, destination)
    print("Move disk",n,"from ",source,"to ",destination)
    TowerOfHanoi(n-1, inter, destination, source)

TowerOfHanoi(4, 'A', 'C', 'B')