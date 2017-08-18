from user import User
from privileges import Privileges

wang = User('wang','lihui',28,'male','Ture')

print(wang.describe_user())
wang = Privileges('can close guest account')
print(wang.show_privileges())
