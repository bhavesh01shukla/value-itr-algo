import numpy as np

u=np.zeros((5,4,3))
v=np.zeros((5,4,3))
dif=np.zeros((5,4,3))


gamma=0.99
delta=0.001
final=100000000000000
itr=0

while(final > delta):
    
    print('----------------------------------------------------------------------')
    print("ITERATION NO:",itr)
    for i in range(0,5):
        for j in range(0,4):
            for k in range(0,3):
                ## i=> enemy health , j=> num arrows , k=> stamina
                step_cost=5 

                shoot=-100000000
                if j>0 and k>0:
                    if (i-1==0):
                        reward=0.5*(10-step_cost) + 0.5*(-step_cost)
                    else:
                        reward=-step_cost
                    shoot=reward + gamma*(0.5*u[i-1,j-1,k-1] + 0.5*u[i,j-1,k-1])

                recharge=-100000000
                if k==2:
                    reward=-step_cost
                    recharge= reward + gamma*(1*u[i,j,k])
                elif k<2:
                    reward=-step_cost
                    recharge=reward + gamma*(0.8*u[i,j,k+1]+0.2*u[i,j,k])
                
                dodge=-100000000
                reward=-step_cost
                if k==1:
                    if j==3:
                        dodge=reward + gamma*(u[i,3,0])
                    elif j<3:
                        dodge=reward + gamma*(0.2*u[i,j,0] + 0.8*u[i,j+1,0])
                elif k==2:
                    if j==3:
                        dodge=reward + gamma*(0.2*u[i,3,0] + 0.8*u[i,3,1])
                    elif j<3:
                        dodge=reward + gamma*(0.2*0.2*u[i,j,0] + 0.2*0.8*u[i,j+1,0] + 0.8*0.2*u[i,j,1] + 0.8*0.8*u[i,j+1,1])
                
                temp=max(shoot,recharge,dodge)
                
                if i>0:
                    if temp==shoot:
                        print('(',i,j,k,')',v[i,j,k],'policy:shoot')
                    elif temp==recharge:
                        print('(',i,j,k,')',v[i,j,k],'policy:recharge')
                    else:
                        print('(',i,j,k,')',v[i,j,k],'policy:dodge')
                    v[i,j,k]=temp
                    
                elif i==0:
                    print('(',i,j,k,')',u[i,j,k],'policy:-1')
                    v[i,j,k]=0
                dif[i,j,k]=np.abs(v[i,j,k]-u[i,j,k])
    
    u=np.copy(v)
    final=np.max(dif)
    print(final)
    itr+=1
    

