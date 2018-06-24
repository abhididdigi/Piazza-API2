from piazza import Piazza
import os

p = Piazza()
p.user_login(email=os.environ['piazza_user_name'], password=os.environ['piazza_password'])
p.get_user_profile()