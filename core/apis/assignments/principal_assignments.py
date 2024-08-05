from flask import Blueprint, request
from app.models import Assignment
from app.schemas import AssignmentSchema
from app.utils import APIResponse, is_principal_request

bp = Blueprint('principal_assignments', __name__)

@bp.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    if not is_principal_request():
        return {"error": "Unauthorized"}, 403
    
    assignments = Assignment.query.filter(
        Assignment.state.in_(['SUBMITTED', 'GRADED'])
    ).all()
    
    return APIResponse.respond(data=AssignmentSchema(many=True).dump(assignments))
