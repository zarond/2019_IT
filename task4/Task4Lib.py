import matplotlib.pyplot as plt
import numpy as np

def rotate(theta):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c,-s), (s, c)))
    return R
    
def DrawGrid(M, l=1):
    for i in range(M):
        V = np.array([1,0])
        a = rotate(np.radians(i*360/M)).dot(V)
        plt.text(l*a[0], l*a[1], 'x'+ str(i), dict(size=10))
        for j in range(1,int(l+1)):
            plt.text(j*a[0], j*a[1], str(j), dict(size=10))
            plt.scatter(j*a[0], j*a[1], marker = '.', color = 'k')
        plt.plot([0,l*a[0]],[0,l*a[1]],color = 'k',linewidth=0.6)
    
def DrawDot(X,M,col):
    T = np.empty([M,2])
    L = np.empty([M+1])
    R = np.empty([M+1])
    for i in range(M):
        #V = np.array([i/M,0])
        V = np.array([X[i],0])
        T[i] = rotate(np.radians(i*360/M)).dot(V)
        L[i] = T[i][0]
        R[i] = T[i][1]
    L[M] = T[0][0]
    R[M] = T[0][1]

    plt.plot(L,R,marker = '.',color = col,linewidth=1.0)
    #plt.show()
    
def ParetoFront(X):
    X = np.array(X)
    (N,M) = X.shape
    S = [i for i in range(N)]
    for i in range(N):
        for j in S:
            if (X[j]>X[i]).all():
                if (i in S): S.remove(i)
                break
                
    return S #выдаёт индексы
    
    
def Draw(X):
    #Y = np.array([0.5,0.2,0.3])
    #X = np.array([0.3,0.2,0.1])
    X = np.array(X)
    #plt.xlim(-1, 1), plt.ylim(-1, 1)
    #plt.figure.set_aspect('equal')
    (N,M) = X.shape
    l = np.max(X)
    DrawGrid(M,l+0.5)
    for i in range(N):
        DrawDot(X[i],M,'dodgerblue')
        
    S = ParetoFront(X)
    for i in S:
        DrawDot(X[i],M,'r')
        
    plt.show()
    
def ParetoTest():
    #plt.xlim(0, 2), plt.ylim(0, 2)
    X = np.random.randn(100)
    Y = np.random.randn(100)
    #plt.scatter(X,Y)
    Z = np.stack((X, Y), axis=1)
    #print(Z)
    #plt.show()
    #plt.xlim(0, 2), plt.ylim(0, 2)
    S = ParetoFront(Z)
    plt.scatter(X,Y)
    plt.scatter(X[S],Y[S],color = 'r')
    plt.show()
        
