def test_principal_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        headers=h_principal,
        json={
            "id": 1,
            "grade": "B"
        }
    )
    
    assert response.status_code == 200
    data = response.json
    assert data['data']['grade'] == 'B'
