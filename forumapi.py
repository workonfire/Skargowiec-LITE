import requests
import sys
import warnings
import re
import shutil


class AlreadyLoggedInError(Exception):
    pass


class NotLoggedInError(Exception):
    pass


class GC2:
    def __init__(self, username: str):
        """
        Class constructor.
        :param username: forum username
        """
        if not sys.warnoptions:
            warnings.simplefilter('ignore')
        self.username = username
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.132 Safari/537.36'}
        self.authenticated = False

    def __get_post_key(self) -> str:
        """
        Retrieves MyBB post key.
        :return: post key
        """
        request = self.session.post('https://gc2.pl/forum/', verify=False)
        return re.search(r'var my_post_key = "(\w+)";', request.content.decode(errors='ignore')).group(1)

    def authenticate(self, password: str):
        """
        Method used for logging into the GC2 Forum account.
        :param password: forum password
        :return:
        """
        if not self.authenticated:
            login_data = {'url': 'https://gc2.pl/forum/index.php',
                          'action': 'do_login',
                          'submit': 'Login',
                          'quick_login': '1',
                          'quick_username': self.username,
                          'quick_password': password
                          }
            login_request = self.session.post("https://gc2.pl/forum/member.php", data=login_data, verify=False,
                                              headers=self.headers)
            self.authenticated = True if "Zalogowano" in login_request.content.decode(errors='ignore') else False
        else:
            raise AlreadyLoggedInError

    def create_thread(self, forum_category: str, prefix: int, subject: str, icon: int, message: str):
        """
        Creates a new forum thread.
        :param forum_category: forum category ID, e.g. 294, which points to LavaBlock
        :param prefix: thread prefix, e.g. 25, which points to "[SKARGA]"
        :param subject: thread subject, usually a player's nickname
        :param icon: thread icon, e.g. 2, which points to an exclamation mark
        :param message: thread message
        :return:
        """
        if self.authenticated:
            thread_data = {
                'my_post_key': self.__get_post_key(),
                'threadprefix': prefix,
                'subject': subject,
                'icon': icon,
                'message': message,
                'postoptions[subscriptionmethod]': '',
                'numpolloptions': '2',
                'submit': 'Napisz wątek',
                'action': 'do_newthread'
            }
            self.session.post(f"https://gc2.pl/forum/newthread.php?fid={forum_category}&processed=1",
                              data=thread_data, headers=self.headers)
        else:
            raise NotLoggedInError

    def save_avatar(self, file_location: str):
        """
        Downloads the current user profile picture.
        Never used by Skargowiec LITE.
        :param file_location: file location
        :return:
        """
        if self.authenticated:
            user_id = self.session.cookies.get_dict()['mybbuser'].split('_')[0]
            avatar_request = self.session.get(f"https://gc2.pl/forum/uploads/avatars/avatar_{user_id}.png",
                                              stream=True)
            with open(file_location, 'wb') as avatar_file:
                avatar_request.raw.decode_content = True
                shutil.copyfileobj(avatar_request.raw, avatar_file)
        else:
            raise NotLoggedInError

    def give_reputation_point(self, user_id: int, value: int, comment: str = ''):
        """
        Gives a reputation point for the selected user.
        Never used by Skargowiec LITE.
        :param user_id: user id
        :param value: reputation value, e.g. 1
        :param comment: comment
        :return:
        """
        if self.authenticated:
            reputation_data = {
                'my_post_key': self.__get_post_key(),
                'action': 'do_add',
                'uid': user_id,
                'pid': 0,
                'rid': '',
                'nomodal': 1,
                'reputation': value,
                'comments': comment
            }
            self.session.post("https://gc2.pl/forum/reputation.php?modal=1", data=reputation_data, headers=self.headers)
        else:
            raise NotLoggedInError
