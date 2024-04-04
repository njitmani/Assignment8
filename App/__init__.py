class MainApp:
   def __init__(self) -> None:
       pass
   
   def get_greeting(self) -> str:
       return "This code is uploaded from to docker hub using GH actions"

   def start(self) -> None:
        print("Hello from inside a Docker container!")