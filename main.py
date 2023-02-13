from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator
import tasks

app=FastAPI() #initialize the fastapi
Languages=['English','French','German','Romanian']

#data validator to ensure that route get the valid langauge
class Translation(BaseModel):
    text:str
    base_lang:str
    final_lang:str
    #validating the input
    @validator('base_lang','final_lang')
    def valid_lang(cls, lang):
        if lang not in Languages:
            raise ValueError("Invalid langauge")
        return lang


#route 1 : index route
@app.get('/')
def get_root():
    return {'message':'OK'}
#route 2: /translate
# take a transaltion request and store in the database 
#return a translation

@app.post('/translate')
def post_translation(t:Translation, background_tasks:BackgroundTasks):
    #store the translation 
    t_id=tasks.store_translation(t)
    # run the translation in background
    background_tasks.add_task(tasks.run_translation, t_id)
    return {"task_id":t_id}

#route 3:/result
@app.get("/results")
def get_translation(t_id:int):
    return {'translation': tasks.find_translation(t_id)}
# take  in a transaltion id 
# return the translationt text