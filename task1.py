import numpy as np

u=np.zeros((5,4,3))
v=np.zeros((5,4,3))

# print(u)

gamma=0.99
delta=0.001
final=1000000000000
itr=0

while(final > delta):

    delta_list=[]
    for i in range(0,5):
        for j in range(0,4):
            for k in range(0,3):
                if i==0:
                    reward = -10
                else:
                    reward = -20

                elem=[]
                
                ## action == shoot
                if j > 0 and k > 0:      ## can only shoot if no of arrows and stamina > 0
                    t1=0.5 * u[i-1,j-1,k-1]
                    t2=0.5 * u[i,j-1,k-1]
                    elem.append(t1)
                    elem.append(t2)

                ## action == recharge
                if k==2: ##stamina is full
                    t1= 1 * u[i,j,k]
                    elem.append(t1)
                else:   ### stamina is not full
                    t1= 0.8 * u[i,j,k+1] ##recharged
                    t2= 0.2 * u[i,j,k]   ## not recharged
                    elem.append(t1)
                    elem.append(t2)
                    
                ## action == dodge
                if k==1:
                    if j==3:  ##arrows==3
                        t1= 1 * u[i,3,0]
                        elem.append(t1)

                    if j<3:  ##arrows<3
                        t1= 1 * u[i,j,0]
                        t2= 1 * u[i,j+1,0]
                        elem.append(t1)
                        elem.append(t2)
                
                elif k==2:
                    if j==3:
                        t1= 0.2 * u[i,3,0]
                        t2= 0.8 * u[i,3,1]
                        elem.append(t1)
                        elem.append(t2)

                    elif j<3:
                        t1= 0.2 * 0.2 * u[i,j,0]
                        t2= 0.2 * 0.8 * u[i,j+1,0]
                        t3= 0.8 * 0.2 * u[i,j,1]
                        t4= 0.8 * 0.8 * u[i,j+1,1]
                        elem.append(t1)
                        elem.append(t2)
                        elem.append(t3)
                        elem.append(t4)

                
                # print(i,j,k,elem)
                ans=max(elem)
                ans*=gamma
                ans+=reward
                # print(ans)
                temp=ans-u[i,j,k]
                if(temp<0):
                    temp*=-1
                delta_list.append(temp)

                v[i,j,k] = ans

    u=np.copy(v)
    itr+=1
    # print(max(delta_list))
    final=max(delta_list)
    print(itr,final)
    print(u)
    print('----------------------------------------------------------------------')









