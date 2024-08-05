def test_teacher_cannot_grade_as_principal(client, h_teacher):
    response = client.post(
        '/principal/assignments/grade',
        headers=h_teacher,
        json={
            "id": 1,
            "grade": "B"
        }
    )
    
    assert response.status_code == 403
    data = response.json
    assert data['error'] == 'Unauthorized'
