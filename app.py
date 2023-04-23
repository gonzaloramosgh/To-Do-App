from flask import Flask,render_template,redirect,request,url_for ,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required,current_user
from werkzeug.security import check_password_hash,generate_password_hash
from flask_wtf.csrf import CSRFProtect
import datetime


app = Flask(__name__)
db = MySQL(app)
loged_user_app = LoginManager(app)
csrf = CSRFProtect()

#DATABASE CONFIG
#SECRET KEY USED FOR SHOW THE FLASH MESSAGES
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PASSWORD'] = '' #To CONFIGURE
app.config['MYSQL_DB'] = '' #To CONFIGURE
app.config['SECRET_KEY'] = '' #To CONFIGURE

actual_date= datetime.datetime.now()

@loged_user_app.user_loader
def logged(id):
	return ModelUser.get_user_id(db,id)


@app.route('/')
def index():
	return render_template('login.html')


@app.route('/deletetask' , methods=['POST', 'GET'])
@login_required
def delete():
	if request.method == 'POST':
		post_id= int(request.form.get('postid'))
		cursor = db.connection.cursor()
		sqldel = """   delete from tasks where id = %s """%(post_id)
		cursor.execute(sqldel)
		db.connection.commit()
		data = cursor.fetchone()
		return redirect('home')
	else:
		pass


@app.route('/deleteuser' , methods=['GET','POST'])
@login_required
def deleteuser():
	if request.method == 'POST':
		try:
			user_id = current_user.id
			cursor = db.connection.cursor ()
			sqldel = """ delete from tasks where user_id = %s """ % (user_id)
			cursor.execute (sqldel)
			db.connection.commit()
			sqldel = """ delete from users where id = %s """ %(user_id)
			cursor.execute (sqldel)
			db.connection.commit()
			flash ('User Deleted')
			return redirect('login')
		except Exception as ex:
			raise Exception(ex)
	else:
		return redirect('home')


@app.route('/create', methods=['GET','POST'])
@login_required
def createTask():
	if request.method == 'POST':
		_date = actual_date.strftime("%Y-%m-%d")
		_title = request.form['title']
		_cont = request.form['cont']
		cursor = db.connection.cursor()
		sql = """INSERT INTO tasks (title,description,date,user_id)
		    VALUES ('%s', '%s', '%s', %s) """%(_title,_cont,_date,current_user.id)
		cursor.execute(sql)
		db.connection.commit()
		return redirect('home')


@app.route('/login' , methods=['GET','POST'])
def login():
	if request.method == 'POST':
		user = User(0, "None", request.form['email'], request.form['password'])
		loged_user = ModelUser.login(db,user)
		if loged_user != None:
			if loged_user.passwd:
				login_user(loged_user)
				posts = ModelUser.posts(db,loged_user)
				return redirect('home')
			else:
				flash('Wrong Password')
				return redirect(url_for('login'))
		else:
			flash('Unknown Email')
			return render_template('login.html')
	else:
		return render_template('login.html')


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))


@app.route('/register' , methods=['POST' , 'GET'])
def register():

	''' Register New User.'''

	if request.method == 'POST':
		_name = request.form['name']
		_email = request.form['email']
		_password = request.form['password']
		print(_email)
		hashed_pass = generate_password_hash(_password)
		new_user = User(0,_name,_email,_password)
		print(new_user.email)
		try:
			cursor = db.connection.cursor()
			sql = """ SELECT id,name,email from users WHERE email = '%s' """ %new_user.email
			cursor.execute(sql)
			email = cursor.fetchone()
			print(email)
			if email == None:
				sql = """ INSERT INTO users(name,email,password)
							VALUE ('%s','%s','%s')"""%(_name,_email,hashed_pass)
				cursor.execute(sql)
				db.connection.commit()
				flash('User successfully registered')
				return redirect('login')
			else:
				flash('The email already has an associated account')
				return redirect('register')
		except Exception as ex:
			return " <h1> {%s}  </h1>"%Exception(ex)
	else:
		return render_template ('register.html')


@app.route('/home')
@login_required
def home():
	posts=ModelUser.posts(db,current_user)
	return render_template('home.html',posts=posts)


class ModelUser():

	''' User modeling class	'''

	@classmethod
	def login(self,db,user):
		try:
			cursor= db.connection.cursor()
			sql = """   SELECT id,name,email,password FROM users WHERE email = '%s' """ %(user.email)
			cursor.execute(sql)
			data = cursor.fetchone()
			if data != None:
				_user = User(data[0],data[1],data[2],user.check_password(data[3],user.passwd))
				return _user
			else:
				return None
		except Exception as ex:
			raise Exception(ex)


	@classmethod
	def get_user_id(self,db,id):
		try:
			cursor = db.connection.cursor()
			sql = """ SELECT id,name,email,password FROM users WHERE id = %s """%(id)
			cursor.execute(sql)
			_user = cursor.fetchone()
			if _user != None:
				_user = User(_user[0] ,_user[1],_user[2], True)
				return _user
			else:
				return None
		except Exception as ex:
			raise Exception(ex)


	@classmethod
	def posts(self,db,user):
		try:
			cursor= db.connection.cursor()
			sql = """   SELECT id,title,description,date,user_id FROM tasks WHERE user_id = %s ORDER BY ID DESC """%(user.id)
			cursor.execute(sql)
			post = cursor.fetchall()
			if post != None:
				for i in post:
					posteo = [ (Posts(i[0],i[1],i[2],i[3], i[4])) for i in post ]
					return posteo
			else:
				pass
		except Exception as ex:
			raise Exception(ex)


class Posts():

	""" Users Posts Class """

	def __init__(self,id,title,text,date,user_id):
		self.id = id
		self.title = title
		self.text = text
		self.date = date
		self.user_id= user_id


class User(UserMixin):
	""" User Class """
	def __init__(self, id, name, email, password )  -> None:
		self.id = id
		self.name = name
		self.email = email
		self.passwd = password


	@classmethod
	def check_password(self,hashed_password,password):
		'''compares the user's password in the database with the one entered'''
		return check_password_hash(hashed_password,password)


if __name__ == '__main__':
	csrf.init_app(app)
	app.run(debug = True)