# 設計簡單的認證與授權系統
# 建立一個 User 類別儲存使用者名稱與加密過的密碼
# 此類別也能檢查使用者提供的密碼是否有效

import hashlib

class User:
    def __init__(self, username, password) -> None:
        '''建構新的使用者物件，密碼儲存前要加密'''
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False
    
    def _encrypt_pw(self, password):
        '''密碼加密，回傳sha摘要'''
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()
    
    def check_password(self, password):
        '''如果密碼正確回傳True'''
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


# 自訂例外
# 使用者名稱重複 抱錯
# 密碼太短 抱錯

class AuthException(Exception):
    def __init__(self, username, user=None) -> None:
        super().__init__(username, user)
        self.username = username
        self.user = user

class UsernameAlreadyExist(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass


# 建構 Authenticator 類別
# 此類別為建構管理使用者的帳號密碼
# 建構時透過上方的兩個自訂例外處理看帳號密碼是否符合規範

# class Authenticator:
#     def __init__(self) -> None:
#         '''建構Authenticator管理使用者的帳號密碼'''
#         self.users = {}

#     def add_user(self, username, password):
#         if username in self.users:
#             raise UsernameAlreadyExist(username)
#         if len(password) < 6:
#             raise PasswordTooShort(username)
#         self.users[username] = User(username, password)


# 登入時，確認使用者帳號是否正確
# 登入時，確認使用者密碼是否正確

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

# 擴充 authenticator
# 增加 login方法
# 必要時拋出登入錯誤意外

class Authenticator:
    def __init__(self) -> None:
        '''建構Authenticator管理使用者的帳號密碼'''
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExist(username)
        if len(password) < 6:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        '''登入'''
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)
        
        if not user.check_password(password):
            raise InvalidPassword(username, user)
        
        user.is_logged_in = True
        return True
    
    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False
    
# 以上為使用者帳號、密碼、登入管理
# 接下來建構 使用者的權限 存取管理
# 確認帳號是否登入
# 確認該組帳號是否有某項功能存取權限

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

class Authorizor:
    def __init__(self, authenticator) -> None:
        self.authenticator = authenticator
        self.permissions = {}
    
    def add_permissions(self, perm_name):
        '''建構使用者能使用的權限'''
        try:
            perm_set = self.permissions[perm_name]
        except:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")
    
    def permit_user(self, perm_name, username):
        '''對使用者授予權限'''
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        '''確認使用者是否有perm_name的權限'''
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission is not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True

authenticator = Authenticator()
authorizor = Authorizor(authenticator)