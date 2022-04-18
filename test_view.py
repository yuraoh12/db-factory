from flask import Blueprint

#라우팅 해주는 객체
bp = Blueprint('test', __name__, url_prefix="")

@bp.route('/hello')
def hello() :
    return "hello"

@bp.route('/by')
def by() :
    return "bye"

@bp.route('/instroduction')
def instroduction() :
    return "my name is yuraoh"
