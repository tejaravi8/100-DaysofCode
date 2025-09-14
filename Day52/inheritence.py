# # class nanna:
    
# #     def __init__(self,name,surname,age):
# #         self.surnamename=surname
# #         self.age=age
# #         self.name=name
        
# #     def strengths(self,game,body):
# #         self.game=game
# #         self.body=body

# # class teja(nanna):
    
# #     def strengths(self, body, game):
# #         self.body=body
# #         self.game=game
# #         super().
    
        
# # obj=teja('sankara rao','botsa',48)

# # print(obj.strengths('sixpack','chess'))


# class nanna:   # Parent class
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
        
#     def strengths(self, game, body):
#         self.game = game
#         self.body = body
#         return f"Nanna Strengths → Game: {self.game}, Body: {self.body}"

# # Child class
# class teja(nanna):
#     def strengths(self, body, game):
#         # Call parent method with super()
#         parent_strengths = super().strengths(game, body)
#         return f"{parent_strengths}\nTeja Strengths → Body: {body}, Game: {game}"

# # Object of child class
# obj = teja("Sankara Rao", "Botsa", 48)

# # Call method
# print(obj.strengths("Sixpack", "Chess"))


class animal():
    
    def sound(self,sound):
        # print(obj.bread())
        return f"parent:{sound}"
    
class dog(animal):
    
    def sound(self, sound):
        self.sound=sound
        print(self.sound)
        return super().sound('back back')
    
    def bread(self):
        self.rev='sec'
        

obj=animal()
print(dog(animal()))
print(obj.sound('haha'))
