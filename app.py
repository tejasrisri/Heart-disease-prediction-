from flask import Flask,render_template,request
import pickle
model=pickle.load(open('heartdisease.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def loadPage():
    return render_template('index.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    a=request.form["age"]
    b=request.form["gender"]
    c=request.form["chestpain"]
    d=request.form["bp"]
    e=request.form["cholestrol"]
    f=request.form["sugar"]
    g=request.form["restecg"]
    h=request.form["thalach"]
    i=request.form["exang"]
    j=request.form["oldpeak"]
    k=request.form["slope"]
    l=request.form["ca"]
    m=request.form["thal"]
    t=[[int(a),int(b),int(c),int(d),int(e),int(f),int(g),float(h),int(i),float(j),int(k),int(l),int(m)]]
    y=model.predict(t)
    print(y)
    ans=""
    if y==0:
        ans="Hurray! you Don't have Heart Disease"
    else:
        ans="Please Consult a Doctor you are having Heart Disease"
    return render_template('index.html',a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j,k=k,l=l,m=m,ans=ans)
if __name__=="__main__":
    app.run(debug=True)
