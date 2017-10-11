# set1 = {1, 2, 3, 4}
# set2 = {2, 3}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.union(set2))
# print(set2.intersection(set1))
# print(set2.difference(set1))
#
#
# import random
#
#
# def game(rows, cols):
#
#     table = (rows*cols-1)*[''] + ['B']
#     random.shuffle(table)
#
#     while True:
#         pos = input("Enter next position (format: x, y): ")
#         position = pos.split()
#         if table[int(position[0])*cols + int(position[1])] == "B":
#             print("You found the bomb!")
#             break
#         else:
#             print("No bomb at position", pos)
# game(5, 5)
