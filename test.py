import preprocessor as preproc
import pickle
import numpy as np
pp = preproc.preprocessor()
text = pp.forward('my daughter having irragular periods')
model = pickle.load(open('model.pkl','rb'))
# print(model.predict(text))
# convert the out put to string
st = model.predict(text)
str = np.array2string(st)
print(type(str))