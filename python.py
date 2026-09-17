# # # while True:
# # #     num = int(input("Enter the number:  "))
# # #     if num==-1:

# # #         break
# # #     print("You entered no:",num)


    
# # while True:
# #     password = input("Enter the password:")
# #     if password!=("open4129"):
# #         break
# #     print("You Entered password",password)

# """ num = int(input("Show the table of:"))
# for i in range(1,11):
#      print(num, "x" , i, "=", num*i)\

#       """
# for a in range(1,11):
#         if a*a>50:
#             print("First number who exceds 50>",a)
#             break
# for number in range(1,11):
#     if number%2==0:
#       continue
#     print(number)

""" n = int(input("Find the first multiple of this number above 50: "))
for value in range(51, 200):
    if value % n == 0:
        print("First multiple above 50 is", value)
        break
        
 """
""" for i in range(3):
    for j in range(2):
        print(i, j) """

""" city = input("Trip destination: ")
days = int(input("Number of days: "))
companions = input("Travelling with how many friends: ")

trip = [city, days, companions]
print("Trip details:", trip)
print("First detail:", trip[0])
print("Last detail:", trip[-1]) """

""" playlist = []
for i in range(4):
    playlist.append(input("Add a song title: "))

print("Original order:", playlist)
print("Alphabetical:", sorted(playlist))

playlist.reverse()
print("Reversed:", playlist) """

""" team_a = ["Ravi", "Meena"]
team_b = team_a
team_b.append("Arjun")
print(team_a)

finish = [12.5,10.2,15.8,9.9]
finish.sort()
print(finish)
finish.reverse()
print(finish) """

marks =[2,3,4,5]
updatedmarks=[(5+mark) for mark in marks]
print(marks)