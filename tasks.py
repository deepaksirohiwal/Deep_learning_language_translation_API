from models import TranslationModel
from transformers import T5Tokenizer, T5ForConditionalGeneration,T5Model

#initializing the tokenizer
tokenizer=T5Tokenizer.from_pretrained("t5-base",model_max_length=512) #maximum length of the input 
translator= T5ForConditionalGeneration.from_pretrained("t5-base")

#tasks need to run in the backend 
# store the translation task
# store the request in the database
def store_translation(t):
    model= TranslationModel(text=t.text, base_lang=t.base_lang, final_lang=t.final_lang)
    model.save()
    return model.id

#run a pretrain deep learning model
def run_translation(t_id:int):#takes the database id of the model we want to translate
    model=TranslationModel.get_by_id(t_id) #look up using id

   #t5-small takes input as f"translate English to Frenc:Hello world!"
    prefix=f"translate {model.base_lang} to {model.final_lang}:{model.text}"
    #tokenizing 
    input_ids=tokenizer(prefix, return_tensors="pt").input_ids
    outputs= translator.generate(input_ids, max_new_tokens=512)
    #converting the number into text
    translation=tokenizer.decode(outputs[0], skip_special_tokens=True)
    model.translation=translation
    model.save()

# find the translation 
# retrieve the translation from the database
def find_translation(t_id:int):
    model=TranslationModel.get_by_id(t_id)
    translation= model.translation
    if translation is None:
        translation="Processing, check back later."
    return translation