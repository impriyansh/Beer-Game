#!/usr/bin/python
import random
from random import randint
import matplotlib.pyplot as plt

import numpy as np
from numpy import random

N=int(input("Enter the number of weeks: "))
array_lb=int(input("Please define the random Customer Demand between a certain interval(lower bound): "))
array_ub=int(input("Please define the random Customer Demand between a certain interval(upper bound): "))
ad=int(input("Please define the randon change in customer demand that causes bullwhip effect:"))
Weeks=[0]*(N+1)
for i in range(0,N+1):
    Weeks[i]=(i+1)

Orders_C = [0]*(N+1)
Orders_R = [0]*(N+1)
Orders_W = [0]*(N+1)
Orders_D = [0]*(N+1)
Orders_F = [0]*(N+1)

Total_cost_R_array = [0]*(N+1)
Total_cost_W_array = [0]*(N+1)
Total_cost_D_array = [0]*(N+1)
Total_cost_F_array = [0]*(N+1)

Total_stock_R = [0]*(N+1)
Total_stock_W = [0]*(N+1)
Total_stock_D = [0]*(N+1)
Total_stock_F = [0]*(N+1)

My_Order_R = [0]*(N+1)
My_Order_W = [0]*(N+1)
My_Order_D = [0]*(N+1)
My_Order_F = [0]*(N+1)

Outgoing_Deliv_W = [0]*(N+12)
Outgoing_Deliv_D = [0]*(N+12)
Outgoing_Deliv_F = [0]*(N+12) 

Backorder_R=0;
Stock_R=int(input("What is your initial stock Retailer?: "))
Incoming_Deliv_R=0;
Backorder_W=0;
Stock_W=int(input("What is your initial stock Wholesaler?: ")) 
Incoming_Deliv_W=0;
Backorder_D=0;
Stock_D=int(input("What is your initial stock Distributor?: "))
Incoming_Deliv_D=0;
Backorder_F=0;
Stock_F=int(input("What is your initial stock Factory?: "))
Incoming_Deliv_F=0;
Init_order=int(input("What is the initial quantity of orders in every department except the Retailer: "))

# The   bullwhip   simulator   
for i in range(0,N+1):
    print ("Number of Current Week: ");
    print (i+1)
    
    if i<=4:  #After 5 rounds the Customer Demand is going to increase according to the additive value ad
        Customer_Demand = randint(array_lb, array_ub)   #Random Customer Demand between the interval of 10   and   20
    else:
        Customer_Demand = randint(array_lb+ad,array_ub+ad);  #The random change in Customer Demand that causes the bullwhip effect.
    
    #Retailer
    print ("RETAILER: ")             
    if i<=1:
        Incoming_Deliv_R=0;
    else:
        Incoming_Deliv_R=Outgoing_Deliv_W[i-2];           

    Incoming_Order_R=Customer_Demand;   #Order from Customer
    c_R=(Stock_R + Incoming_Deliv_R) - (Incoming_Order_R + Backorder_R)          
    if c_R<0:
        Outgoing_Deliv_R=Stock_R+Incoming_Deliv_R;
        Backorder_R=abs(c_R);
        Stock_R=0;
    else:
        Outgoing_Deliv_R=Incoming_Order_R+Backorder_R;                       
        Stock_R=c_R;
        Backorder_R=0;
    
    Total_cost_R=Backorder_R*2+Stock_R*1;
    Total_cost_R_array[i]=Total_cost_R
    if Stock_R>0:
        Total_stock_R[i]=Stock_R;
    else:
        Total_stock_R[i]=-Backorder_R;
    
    Orders_C[i]=Incoming_Order_R;

    print("Incoming Delivery from provider: ");
    print(Incoming_Deliv_R);
    print("Incoming Order from client: ");
    print(Incoming_Order_R);
    print("Outgoing Delivery: ");
    print(Outgoing_Deliv_R);
    print("Backorder: ");
    print(Backorder_R);
    print("Stock: ");
    print(Stock_R);
    print("Total cost: ");
    print(Total_cost_R);
    My_Order_R[i]=int(input("Whats your order Retailer ?: "))
    Orders_R[i]=My_Order_R[i];
    
    # Wholesaler 
    print ("wholesaler:");
    if i<=2:
        Incoming_Deliv_W=0;
    else:
        Incoming_Deliv_W=Outgoing_Deliv_D[i-2];

    if i==1:
        Incoming_Order_W=Init_order;

    else:
        Incoming_Order_W= My_Order_R[i-1]; # Order from retailer

    c_W=(Stock_W+Incoming_Deliv_W)-(Incoming_Order_W+Backorder_W);
    if c_W<0:
        Outgoing_Deliv_W[i]=Stock_W+Incoming_Deliv_W;
        Backorder_W=abs(c_W);
        Stock_W=0;
    else:
        Outgoing_Deliv_W[i]=Incoming_Order_W+Backorder_W;
        Stock_W=c_W;
        Backorder_W=0;

    Total_cost_W = Backorder_W*2 + Stock_W*1;
    Total_cost_W_array[i]=Total_cost_W;
    if Stock_W>0:
        Total_stock_W[i]=Stock_W;
    else:
        Total_stock_W[i]=-Backorder_W;

    print("incoming Delivery from Provider:")
    print(Incoming_Deliv_W)
    print("Incoming Order from Client")
    print(Incoming_Order_W)
    print("Outgoing Delivery")
    print(Outgoing_Deliv_W[i])
    print("Backorder:")
    print(Backorder_W)
    print("Stock:")
    print(Stock_W)
    print("Total cost:")
    print(Total_cost_W)
    My_Order_W[i]=int(input("Whats your order wholesaler ?: "))
    Orders_W[i]=My_Order_W[i];
    
    print ("DISTRIBUTER: ")
    if i<=2:
        Incoming_Deliv_D = 0
    else:
        Incoming_Deliv_D = Outgoing_Deliv_F[i-2]

    if i==1:
        Incoming_Order_D = Init_order
    else:
        Incoming_Order_D = My_Order_W[i-1]

    c_D = (Stock_D + Incoming_Deliv_D) - (Incoming_Order_D + Backorder_D)
    if c_D<0:
        Outgoing_Deliv_D[i] = Stock_D + Incoming_Deliv_D
        Backorder_D=abs(c_D)
        Stock_D = 0 
    else: 
        Outgoing_Deliv_D[i]= Incoming_Order_D + Backorder_D
        Stock_D = c_D
        Backorder_D = 0

    Total_cost_D = Backorder_D*2 + Stock_D*1
    Total_cost_D_array[i]=Total_cost_D; 

    if Stock_D>0:
        Total_stock_D[i] = Stock_D
    else:
        Total_stock_D[i] =-Backorder_D;
    print ("Incoming​ Delivery from Provider:")
    print (Incoming_Deliv_D)
    print ("Incoming​ ​Order​ ​from​ ​client:​ ​")
    print (Incoming_Order_D)
    print ("Outgoing​ ​Delivery")
    print (Outgoing_Deliv_D[i])
    print ("Backorder:​ ​")
    print (Backorder_D)
    print ("Stock:​ ​")
    print (Stock_D)
    print ("Total​ ​cost:​ ​")
    print (Total_cost_D)
    My_Order_D[i] = int(input('Whats​ ​your​ ​order​ ​distributor​ ​?:​ ​​ '))
    Orders_D[i] = My_Order_D[i]

    print ("FACTORY")
    if i<=3:
        Incoming_Deliv_F = 0
    else:
        Incoming_Deliv_F = My_Order_F[i-3]

    if i==1:
        Incoming_Order_F = Init_order
    else:
        Incoming_Order_F = My_Order_D[i-1]

    c_F = (Stock_F + Incoming_Deliv_F) - (Incoming_Order_F + Backorder_F);
    if c_F<0:
        Outgoing_Deliv_F[i] = Stock_F + Incoming_Deliv_F;
        Backorder_F = abs(c_F);
        Stock_F = 0;
    else:
        Outgoing_Deliv_F[i] = Incoming_Order_F + Backorder_F;
        Stock_F = c_F;
        Backorder_F=0;

    Total_cost_F = Backorder_F*2+Stock_F*1;
    Total_cost_F_array[i] = Total_cost_F
    if Stock_F>0:
        Total_stock_F[i] = Stock_F;

    else:
        Total_stock_F[i]=-Backorder_F;

    print ("Incoming​ ​Delivery​ ​from​ ​provider:​ ​ ")
    print (Incoming_Deliv_F)
    print ("Incoming​ ​Order​ ​from​ ​client:​ ​")
    print (Incoming_Order_F)
    print ("Outgoing​ ​Delivery")
    print (Outgoing_Deliv_F[i])
    print ("Backorder:​ ​")
    print (Backorder_F)
    print ("Stock:​ ​")
    print (Stock_F)
    print ("Total​ ​cost:​ ​")
    print (Total_cost_F)
    My_Order_F[i] = int(input('Whats​ ​your​ ​order​ ​Factory​ ​?:​ ​​ '))
    Orders_F[i] = My_Order_F[i]

p1 = plt.subplot(321)
plt.plot(Weeks, Total_cost_R_array, color = 'Red', label = 'Retailer')
plt.xlabel('Weeks')
plt.ylabel('Total Cost')
#plt.show()

plt.plot(Weeks, Total_cost_W_array, color = 'Green', label = 'Wholesaler')
plt.xlabel('Weeks')
plt.ylabel('Total Cost')
#plt.show()

plt.plot(Weeks, Total_cost_D_array, color = 'Yellow', label = 'Distributor')
plt.xlabel('Weeks')
plt.ylabel('Total Cost')
#plt.show()

plt.plot(Weeks, Total_cost_F_array, color = 'Blue', label = 'Factory')
plt.xlabel('Weeks')
plt.ylabel('Total Cost')


p1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
p2 = plt.subplot(323)

plt.plot(Weeks, Total_stock_R, color = 'Red', label = 'Retailer')
plt.xlabel('Weeks')
plt.ylabel('Stocks')
#plt.show()

plt.plot(Weeks, Total_stock_W, color = 'Green', label = 'Wholesaler')
plt.xlabel('Weeks')
plt.ylabel('Stocks')
#plt.show()

plt.plot(Weeks, Total_stock_D, color = 'Yellow', label = 'Distributor')
plt.xlabel('Weeks')
plt.ylabel('Stocks')
#plt.show()

plt.plot(Weeks, Total_stock_F, color = 'Blue', label = 'Factory')
plt.xlabel('Weeks')
plt.ylabel('Stocks')

#p2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
p2.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

p3 = plt.subplot(325)
plt.plot(Weeks, My_Order_R, color = 'Red', label = 'Retailor')
plt.xlabel('Orders')
plt.ylabel('Weeks')
#plt.show()

plt.plot(Weeks, My_Order_W, color = 'Green', label = 'Wholesaler')
plt.xlabel('Orders')
plt.ylabel('Weeks')
#plt.show()

plt.plot(Weeks, My_Order_D, color = 'Yellow', label = 'Distributor')
plt.xlabel('Orders')
plt.ylabel('Weeks')
#plt.show()

plt.plot(Weeks, My_Order_F, color = 'Blue', label = 'Factory')
plt.xlabel('Orders')
plt.ylabel('Weeks')

p3.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()





