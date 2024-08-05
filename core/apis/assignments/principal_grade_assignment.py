from flask import Blueprint, request
from app.models import Assignment
from app.schemas import AssignmentSchema
from app.utils import APIResponse, is_principal_request

bp = Blueprint('principal_grade_assignment', __name__)

@bp.route('/principal/assignments/grade', methods=['POST'])
def grade_assignment_by_principal():
    if not is_principal_request():
        return {"error": "Unauthorized"}, 403
    
    payload = request.json
    assignment = Assignment.query.get(payload['id'])
    
    if not assignment:
        return {"error": "Not Found"}, 404
    
    assignment.grade = payload['grade']
    assignment.state = 'GRADED'
    db.session.commit()
    
    return APIResponse.respond(data=AssignmentSchema().dump(assignment))
