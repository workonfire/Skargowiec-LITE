import requests, sys, warnings, re, shutil

class GC2:
	def __init__(self):
		if not sys.warnoptions:
			warnings.simplefilter("ignore")
		self.session = requests.Session()
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

	def login(self, username, password):
		login_data = {'url': 'https://gc2.pl/forum/index.php',
				  	'action': 'do_login',
				  	'submit': 'Login',
				  	'quick_login': '1',
				  	'quick_username': username,
				  	'quick_password': password
				  	}
		login_request = self.session.post("https://gc2.pl/forum/member.php", data = login_data, verify = False, headers = self.headers)
		if "Zalogowano" in login_request.content.decode(errors = 'ignore'):
			return True
		else:
			return False
	def post(self, forum_category, prefix, subject, icon, message):
		thread_data = {
			'my_post_key': re.search(r'var my_post_key = "(\w+)";', self.session.post('https://gc2.pl/forum/', verify = False).content.decode(errors = 'ignore')).group(1),
			'threadprefix': prefix,
			'subject': subject,
			'icon': icon,
			'message': message,
			'postoptions[subscriptionmethod]': '',
			'numpolloptions': '2',
			'submit': 'Napisz wątek',
			'action': 'do_newthread'
		}
		self.session.post("https://gc2.pl/forum/newthread.php?fid=" + str(forum_category) + "&processed=1", data = thread_data, headers = self.headers)

	def save_avatar(self):
		user_id = self.session.cookies.get_dict()['mybbuser'].split('_')[0]
		avatar_request = self.session.get("https://gc2.pl/forum/uploads/avatars/avatar_{}.png".format(user_id), stream = True)
		with open('../temp/avatar.png', 'wb') as avatar_file:
			avatar_request.raw.decode_content = True
			shutil.copyfileobj(avatar_request.raw, avatar_file)

	def give_reputation_point(self, uid, value, comment):
		reputation_data = {
			'my_post_key': re.search(r'var my_post_key = "(\w+)";', self.session.post('https://gc2.pl/forum/', verify  =False).content.decode(errors='ignore')).group(1),
			'action': 'do_add',
			'uid': uid,
			'pid': 0,
			'rid': '',
			'nomodal': 1,
			'reputation': value,
			'comments': comment
		}
		self.session.post("https://gc2.pl/forum/reputation.php?modal=1", data = reputation_data, headers = self.headers)