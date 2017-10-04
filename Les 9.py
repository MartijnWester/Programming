# try:
#     age = input("Enter your age here: ")
#     intage = int(age)
#     print("you're", intage, "years old".format(intage))
# except:
#     print("Enter your age using digits 0-9")
#
# def dict_manipuation(my_dictionary, string, number):
#     try:
#         my_dictionary[string] = 2 * number
#         print(type(my_dictionary[string]))
#     except(ValueError, KeyError):
#         print("Error")
#     else:
#         my_dictionary[number:] = 2 * string
#     finally:
#         print(my_dictionary)
# dict_manipuation({"first":1, "second":2}, "last", 8)
