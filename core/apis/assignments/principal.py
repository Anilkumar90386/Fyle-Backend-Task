@app.route('/principal/assignments', methods=['GET'])
def get_principal_assignments():
    if not is_principal_request():
        return {"error": "Unauthorized"}, 404
    
    assignments = Assignment.query.filter(
        Assignment.state.in_(['SUBMITTED', 'GRADED'])
    ).all()
    
    return APIResponse.respond(data=AssignmentSchema(many=True).dump(assignments))
