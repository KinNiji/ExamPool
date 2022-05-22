import hashlib

from mysql import select, update, insert_record


class User:
    def __init__(self):
        pass

    @staticmethod
    def encrypt_sha1(password: str):
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

    def login_check(self, stu_id, password):
        if select('select count(*) from user where stu_id=%s and password=%s', stu_id, self.encrypt_sha1(password)):
            return stu_id
        return None

    def insert_user(self, stu_id, password):
        if not select('select * from user where stu_id=%s', stu_id):
            return insert_record('user', {'stu_id': stu_id, 'password': self.encrypt_sha1(password)})
        return False

    def update_password(self, stu_id, password):
        return update('update user set password=% where stu_id=%s', stu_id, self.encrypt_sha1(password))


if __name__ == '__main__':
    user = User()
    # print(user.insert_user('10000000', '1145141919810'))
    for stu_id in range(18250101, 18250131 + 1):
        print(user.insert_user(stu_id, '123456'))
