from flask import Blueprint, request
from app.models import Teacher
from app.schemas import TeacherSchema
from app.utils import APIResponse, is_principal_request

bp = Blueprint('principal_teachers', __name__)

@bp.route('/principal/teachers', methods=['GET'])
def get_principal_teachers():
    if not is_principal_request():
        return {"error": "Unauthorized"}, 403
    
    teachers = Teacher.query.all()
    
    return APIResponse.respond(data=TeacherSchema(many=True).dump(teachers))
