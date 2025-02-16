from crewai.flow.flow import Flow, start, listen  # type: ignore
import time


class AuraFlow(Flow):
    @start()
    def function1(self):
        print("Pehle Main Chaloon Ga")
        time.sleep(3)

    @listen(function1)
    def function2(self):
        print("Ab main")
        time.sleep(3)
        
    @listen(function2)
    def function3(self):
        print("Aur Akhir Main Main")

def kickoff():
    obj= AuraFlow()
    obj.kickoff()