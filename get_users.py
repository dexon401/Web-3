from data.db_session import global_init, create_session
from data.users import User

db_name = input()

global_init(db_name)

db_sess = create_session()

for user in db_sess.query(User).filter(User.address == "module_1"):
    if "engineer" not in user.speciality and "engineer" not in user.position:
        print(user.id)
