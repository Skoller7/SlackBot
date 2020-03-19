import pandas as pd

class Predict:
  def predict(self, context):
    sentence = self.__preprocessing(context)
    df = pd.DataFrame({"Sentence":[sentence], "Negatief":[0], "Lichtjes negatief":[0], "Neutraal":[0], "Lichtjes positief":[0], "Positief":[0], "labels":[0], "text":[sentence]})
    df['labels'] = list(zip(df['Negatief'].tolist(), df['Lichtjes negatief'].tolist(), df['Neutraal'].tolist(), df['Lichtjes positief'].tolist(),  df['Positief'].tolist()))
    return df

  def __preprocessing(self, context):
    employees_names = {'Anissa'} #names need to be added later, please lowercase these!
    employees_names = [name.lower() for name in employees_names]  #don't trust that mistakes won't happen, think ahead ;)   
    clean_context = context.lower()
    
    if [word in clean_context.split(" ") for word in employees_names]:
      for name in employees_names:
       for word in clean_context.split(" "):
         if word  == name:
           clean_context = clean_context.replace(word, 'slack')
           break;
    return clean_context
  
