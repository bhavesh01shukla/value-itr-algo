import numpy as np

u=np.zeros((5,4,3))
v=np.zeros((5,4,3))

gamma=0.99
delta=0.001
final=100000000000000
itr=0

while(final > delta):
    print('----------------------------------------------------------------------')
    print("ITERATION NO:",itr)
    delta_list=[]
    for i in range(0,5):
        for j in range(0,4):
            for k in range(0,3):
                
                
                ## i=> enemy health , j=> num arrows , k=> stamina

                elem=[]
                if i==0:
                    policy='-1'
                    reward= 0
                    v[i,j,k]=reward + 0*u[i,j,k]
                    print('(',i,j,k,'):',policy,v[i,j,k])

                else:    
                    ## action == shoot
                    if j > 0 and k > 0:      ## can only shoot if no of arrows and stamina > 0
                        t1=0.5 * u[i-1, j-1, k-1]
                        t2=0.5 * u[i,j-1, k-1]

                        if(i-1==0):
                            reward=0.5*(10-20) + 0.5*(-20) ## enemy health == 0
                        else:
                            reward = -20
                        elem.append([t1+t2,'SHOOT',reward])
                        # elem.append([t2,'SHOOT',reward])

                    ## action == recharge
                    if k==2: ##stamina is full
                        t1= 1 * u[i,j,k]
                        reward= -1*20
                        elem.append([t1,'RECHARGE',reward])                    
                        
                    else:   ### stamina is not full
                        t1= 0.8 * u[i,j,k+1] ##recharged
                        t2= 0.2 * u[i,j,k]   ## not recharged
                        reward= 0.8*(-20) + 0.2*(-20)
                        elem.append([t1+t2,'RECHARGE',reward])                    
                        # elem.append([t2,'RECHARGE',reward])                                        
                        
                    ## action == dodge
                    if k==1:
                        if j==3:  ##arrows==3
                            reward=-20
                            t1= 1 * u[i,3,0]
                            elem.append([t1,'DODGE',reward])                                           

                        if j<3:  ##arrows<3
                            t1= 0.2 * u[i,j,0]
                            t2= 0.8 * u[i,j+1,0]
                            reward= -20
                            elem.append([t1+t2,'DODGE',reward])                                           
                            # elem.append([t2,'DODGE',reward])                                           
                                            
                    elif k==2:
                        if j==3:
                            t1= 0.2 * u[i,3,0]
                            t2= 0.8 * u[i,3,1]
                            reward= -20
                            elem.append([t1+t2,'DODGE',reward])                                           
                            # elem.append([t2,'DODGE',reward])                                                                   

                        elif j<3:
                            t1= 0.2 * 0.2 * u[i,j,0]
                            t2= 0.2 * 0.8 * u[i,j+1,0]
                            t3= 0.8 * 0.2 * u[i,j,1]
                            t4= 0.8 * 0.8 * u[i,j+1,1]
                            reward= -20
                            elem.append([t1+t2+t3+t4,'DODGE',reward])                                           
                            # elem.append([t2,'DODGE',reward])                                           
                            # elem.append([t3,'DODGE',reward])                                           
                            # elem.append([t4,'DODGE',reward])                                           

                    # print(i,j,k,elem)
                    max=elem[0]

                    for jj in elem:
                        if jj[0]> max[0]:
                            max=jj
                    reward=max[2]
                    policy=max[1]

                    v[i,j,k]= max[0]
                    v[i,j,k]*=gamma
                    v[i,j,k]+=reward
                    # print(v[i,j,k])
                    temp=v[i,j,k]-u[i,j,k]
                    if(temp<0):
                        temp*=-1
                    delta_list.append(temp)
                    print('(',i,j,k,'):',policy,round(v[i,j,k],3))

    u=np.copy(v)
    itr+=1
    # print(delta_list)
    final=delta_list[0]
    for bb in delta_list:
        if bb > final:
            final=bb
    print('gamma',final)
    # print(u)









