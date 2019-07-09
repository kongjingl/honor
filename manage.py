# -*- encoding=utf-8 -*-
import unittest

from honor import app,db
import random
from flask_script import Manager
from honor.models import User,Image,Comment
from sqlalchemy import or_,and_

manager =Manager(app)
def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'

@manager.command
def run_test():
    tests = unittest.TestLoader().discover("./")
    unittest.TextTestRunner().run(tests)



@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0,30):
        db.session.add(User('User'+ str(i),'a'+str(i)))
        for j in range(0,11):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,3):
                db.session.add(Comment('this is a comment'+str(k), 1+3*i+j,i+1))
    db.session.commit()

    for i in range(10,20,2):
        user = User.query.get(i)
        user.username='[old]'+user.username
    db.session.commit()
    User.query.filter_by(id=10).update({'username':'[new]'})
    db.session.commit()

    for i in range(10,20,2):
        comment = Comment.query.get(i)
        db.session.delete(comment)
        db.session.commit()


    #各种查询
    print 1,User.query.all()
    print 2, User.query.get(3)
    print 3, User.query.order_by(User.id.desc()).offset(1).limit(2).all()
    print 4, User.query.filter(User.username.endswith('1')).limit(3).all()
    print 5, User.query.filter(or_(User.id==2,User.id==4)).all()
    print 6, User.query.filter(and_(User.id > 1, User.id < 4)).first()
    print 7, User.query.order_by(User.id.desc()).paginate(page=1,per_page=5).items
    user = User.query.get(1)
    print 8,user.images
    image = Image.query.get(1)
    print 9,image,image.user
    user = User.query.get(10)
    print 10, user







if __name__ == "__main__":
    manager.run()
