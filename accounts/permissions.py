# from django.contrib.auth.models import Group
# from accounts.models import User
#
# # rollarni yaratdim
# admin, _ = Group.objects.get_or_create(name = 'admin')
# client, _ = Group.objects.get_or_create(name = 'client')
#
# # userni ovolish
# user = User.objects.get(id = 1)
# user2 = User.objects.get(id = 6)
#
# #userni guruhlash
# user.groups.add(client)
# user.groups.add(admin)
# user2.groups.add(client)
# user2.groups.add(client)