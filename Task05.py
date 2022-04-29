#5) İstifadəçinin daxil etdiyi cümlənin içində sait və samitlərin sayını tapan skript
str=input("Zəhmət olmasa istədiyiniz söz və ya cümlə daxil edin: ");
saitlər=0
samitlər=0
for i in str:
    if(i == 'A'or i == 'a'or i == 'I'or i == 'ı'or i == 'O' or
       i == 'o'or i=='U' or i=='u' or i == 'E'or i == 'e'or i == 'Ə'or i == 'ə' or 
       i == 'Ö' or i =="ö" or i =='Ü' or i =='ü' or i == 'İ' or i =='i'):
           saitlər=saitlər+1;
    else:
        samitlər=samitlər+1;

print("Saitlərin sayı:",saitlər);
print("\nSamitlərin sayı:",samitlər);