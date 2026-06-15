from oops_proj import chatbook

user1=chatbook()
print(user1.id)

#Using static method directly from class rather than object
chatbook.set_id(10)

user2=chatbook()
print(user2.id)
user3=chatbook()
print(user3.id)
# user4=chatbook()
# print(user4.id)
# user5=chatbook()
# print(user5.id)
# user1.sendmsg()
# print(user1._chatbook__name)

# print(user1.get_name())
# user1.set_name("Ayush")
# print(user1.get_name())