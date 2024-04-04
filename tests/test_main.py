from App import MainApp

def test_message():
    app = MainApp()
    assert app.get_greeting() == "This code is uploaded from to docker hub using GH actions"