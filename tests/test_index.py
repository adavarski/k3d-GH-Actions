def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

    expected = "<p>Test CI/CD</p>"
    assert expected == response.get_data(as_text=True)
