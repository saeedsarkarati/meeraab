from members.models import User
from members.models import Agent
print (User.objects.all() )
print (Agent.objects.all() )
# ~ u = User(firstname='Emil', lastname='Refsnes')
# ~ u.save()
# ~ a = Agent(firstname='kargozar', lastname='nist')
# ~ a.save()
UList =[('1', '10'), ('2', '20'), ('3', '30'), ('4', '40'), ('5', '50'), ('6', '60')]
for i in UList:
	User ( firstname=i[0], lastname=i[1] ).save()
print(User.objects.all().values())

AList =[('a', 'a*'), ('b', 'b*'), ('c', 'c*')]
for i in AList:
	Agent ( firstname=i[0], lastname=i[1] ).save()	

print(Agent.objects.all().values())

# ~ python3 manage.py migrate members zero
# ~ python3 manage.py migrate members
# ~ python3 manage.py shell < ssaddtodb.py 

# ~ python3 manage.py flush
# ~ exec(open('ssadduser.py').read())  ..............  in python3 manage.py shell
# ~ python3 manage.py shell < ssaddtodb.py 
