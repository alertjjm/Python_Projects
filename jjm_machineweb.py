import cgi, os.path
from sklearn.externals import joblib

pklfile=os.path.dirname(__file__)+"/freq.pkl"
clf=joblib.load(pklfile)

def show_form(text,msg=""):
    print("Content-Type: text/jtml; charset=utf-8")
    print("")
    print("""
    <html><body><form>
    <textarea name="text" rows="8" cols="40">{0}</textarea>
    <p><input type="submit" value="판정"></p>
    <p>{1}</p>
    </form></body></form>
    """.format(cgi.escape(text),msg))