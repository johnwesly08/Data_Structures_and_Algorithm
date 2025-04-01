# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# def in_order_traversal(root):
#     if root:
#         # Traverse the left subtree
#         in_order_traversal(root.left)
#         # Visit the root node
#         print(root.val, end=" ")
#         # Traverse the right subtree
#         in_order_traversal(root.right)

# def pre_order_traversal(root):
#     if root:
#         # Visit the root node
#         print(root.val, end=" ")
#         # Traverse the left subtree
#         pre_order_traversal(root.left)
#         # Traverse the right subtree
#         pre_order_traversal(root.right)

# def post_order_traversal(root):
#     if root:
#         # Traverse the left subtree
#         post_order_traversal(root.left)
#         # Traverse the right subtree
#         post_order_traversal(root.right)
#         # Visit the root node
#         print(root.val, end=" ")

# # Example of creating a simple binary tree
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)

# print("In-order Traversal:")
# in_order_traversal(root)
# print("\n")

# print("Pre-order Traversal:")
# pre_order_traversal(root)
# print("\n")

# print("Post-order Traversal:")
# post_order_traversal(root)
# print("\n")

# # Encapsulation

# class Clock:
#     def __init__(self):
#         self.__hours = 0
#         self.__minutes = 0

#     def set_time(self, hours, minutes):
#         if 0 <= hours < 24 and 0 <= minutes < 60:
#             self.__hours = hours
#             self.__minutes = minutes
#         else:
#             print('Invalid Time Format')

#     def getTime(self):
#         return f"{str(self.__hours).zfill(2)}:{str(self.__minutes).zfill(2)}"
    
# my_clock = Clock()
# my_clock.set_time(10, 45)
# print(my_clock.getTime())

# Inheritance
# Single Inheritance
# class Animal:
#     def __init__(self):
#         self.__dogCount = 20 #This is private
#         self.dogCount = 10

#     def makeNoise(self):
#         return "Animal makes the sound"
    
#     def getDogCount(self):
#         return self.__dogCount
    
# class Dog(Animal):
#     def makeNoise(self):
#         return "Bark like Hell"

# animal = Animal() # calling the parent class
# dog = Dog() # calling the child class
# print(animal.makeNoise(),animal.dogCount,animal.getDogCount())


# Multiple Inheritance 
