#Program to Count Total numbers of notes in given amount

amt=int(input("Enter Amount\n"))
note500=note100=note50=note20=note10=note5=note2=note1=0
if amt>=500:
    note500=amt//500               
    amt=amt-note500*500
if amt>=100:
    note100=amt//100
    amt=amt-note100*100
if amt>=50:
    note50=amt//50
    amt=amt-note50*50
if amt>=20:
    note20=amt//20
    amt=amt-note20*20
if amt>=10:
    note10=amt//10
    amt=amt-note10*10
if amt>=5:
    note5=amt//5
    amt=amt-note5*5
if amt>=2:
    note2=amt//2
    amt=amt-note2*2
if amt>=1:
    note1=amt//1
    amt=amt-note1*1
print("500 \t=\t",note500,amt)
print("100 \t= \t",note100,amt)
print("50 \t= \t",note50)
print("20 \t= \t",note20)
print("10 \t= \t",note10)
print("5 \t= \t",note5)
print("2 \t= \t",note2)
print("1 \t= \t",note1)