from crewai.flow.flow import Flow, start, listen  # type: ignore
from litellm import completion # type: ignore

API_KEY= 'AIzaSyBBNC4cKBQoer0611vHglETTpTN2Wq35x4'

class CityFunFact(Flow):

    @start()
    def random_city_name(self):
        result= completion(
            model='gemini/gemini-1.5-flash',
            api_key=API_KEY,
            messages=[{"content":"Return a random city name from Pakistan.",
                       "role":"user"}]
            ) 
        city = result['choices'][0]['message']['content']   
        print(city)
        return city
    
    @listen(random_city_name)
    def fun_fact(self, city_name):
         result= completion(
            model='gemini/gemini-2.0-flash-exp',
            api_key=API_KEY,
            messages= [{"content":f"Return a random fun fact about {city_name}",
                       "role":"user"}]
            )
         fun_fact= result['choices'][0]['message']['content']
         print(fun_fact)
         self.state['fun_fact']= fun_fact
         #return hai but better, as it helps to use the output in each and every function, 
         # not like return (it can be used in the next function only)

    @listen(fun_fact)
    def save_fun_fact(self):
         with open("fun_fact.md", "w") as file:
            # "w" is used to write in the file and if there is no file with the same name, it will create a new file
              file.write(self.state['fun_fact'])

              # To view the fun fact or basically the response in readme.md format use Ctrl+Shift+V

def kickoff():
        obj= CityFunFact()
        obj.kickoff()