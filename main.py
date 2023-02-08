from peewee import *

DATABASE = 'tweepee3.db'
database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    username = CharField(unique = True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

class post(BaseModel):
    post_id = CharField(unique = True)
    poster = ForeignKeyField(User, to_field='username')

class likes(BaseModel):
    liked = ForeignKeyField(post,to_field = 'post_id')
    liker = ForeignKeyField(User, to_field = 'username')
    likes1 = IntegerField()


def create_tables():
    with database:
        database.create_tables([User,post], safe=True)


# create_tables()

# user = User.create(username = 'shivang',password= 'hshshsh',email = 'sknbhdbv', join_date = '11-03-2001')
# User.create(username = 'shivang12',password= 'hshshsh',email = 'sknbhdbv', join_date = '11-03-2001')
# User.create(username = 'shivang123',password= 'hshshsh',email = 'sknbhdbv', join_date = '11-03-2001')
# User.create(username = 'shivang1234',password= 'hshshsh',email = 'sknbhdbv', join_date = '11-03-2001')
# User.create(username = 'shivang12345',password= 'hshshsh',email = 'sknbhdbv', join_date = '11-03-2001')

# post.create(post_id = '12345',poster = 'shivang')
# post.create(post_id = '123456',poster = 'shivang')
# post.create(post_id = '1234567',poster = 'shivang1234')

# user.save()
# post.save()
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def main():
    return FileResponse('index.html')

@app.get("/all_users")
def get_all_users():
    ans = []
    query = User.select()
    for i in query:
        ans.append(i)
    return ans

@app.get("/users/{name}")
def get_user(name):
    user = []
    user = User.select().where(User.username == name)
    return user

@app.get("posts")
def get_posts():
    ans = []
    query = post.select()
    for i in query:
        ans.append(i)
    return ans

@app.get("/posts/{poster}}")
def get_posts1(poster):
    posts = post.select().where(poster = User.username)
    ans = []
    for i in posts:
        ans.append(i)
    return ans

@app.get("/like/{post_id}")
def like_post(post_id,username):
    post_likes = likes.get(liked = post_id)
    post_likes.likes1 = post_likes.likes1 + 1
    post_likes.save()


@app.get("/delete/{post_Id}")
def delete_post(post_id):
    removal = post.select().where(post_Id = post.post_id)
    post.delete(removal)
    post.save()


from fastapi import File, UploadFile
from fastapi.responses import  HTMLResponse
        
@app.post("/uploadfiles/")
def create_upload_file(files: UploadFile):
    return {"filename": files.filename}

@app.get("/login")
async def login():
    return FileResponse('login.html')

@app.post("/register")
async def register(username : str, password : str):
    return {username, password}

