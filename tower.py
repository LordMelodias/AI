def TowerOfHanoi(n , s_pole, d_pole, i_pole):           
    if n == 1:       # for 1 dis moving if 1 then it print 
        print("Move disc 1 from pole",s_pole,"to pole",d_pole)
        return
    TowerOfHanoi(n-1, s_pole, i_pole, d_pole)     #for 2 dis moving
    print("Move disc",n,"from pole",s_pole,"to pole",d_pole)
    TowerOfHanoi(n-1, i_pole, d_pole, s_pole)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of poles