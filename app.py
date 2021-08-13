from flask import Flask
from flask import render_template
from flask import request


def binary_search(arr, item):
    steps = []
    n = len(arr)
    r = len(arr)-1
    l = 0
    flag = 0
    mid = 0
    while(l<=r):
        mid = (l+r)//2
        if arr[mid] == item:
            flag = 1
            step = ""
            for i in range(n):
                if i != mid:
                    step += "_ "
                else:
                    step += "||" + str(arr[mid]) + "|| "
            steps.append(step)
            break
        elif arr[mid] < item:
            step = ""
            i = 0
            while(i < n):
                for i in range(l):
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| " 
                    else:
                        step = step + "_ "
                for i in range(l, r+1):
                    if i == l:
                        step += "((" + str(arr[i]) + ")) "
                        continue
                    if i == r:
                        step += "((" + str(arr[i]) + ")) "
                        continue
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| "
                    else:
                        step = step + str(arr[i]) + " "
                for i in range(r+1, n):
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| "
                    else:
                        step = step + "_ "
                i += (n+1)
            steps.append(step)
            l = mid+1
        elif arr[mid] > item:
            step = ""
            i = 0
            while(i < n):
                for i in range(l):
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| "
                    else:
                        step = step + "_ "
                for i in range(l, r+1):
                    if i == l:
                        step += "((" + str(arr[i]) + ")) "
                        continue
                    if i == r:
                        step += "((" + str(arr[i]) + ")) "
                        continue
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| "
                    else:
                        step = step + str(arr[i]) + " "
                for i in range(r+1, n):
                    if i == mid:
                        step += "||" + str(arr[mid]) + "|| "
                    else:
                        step = step + "_ "
                i += (n+1)
            steps.append(step) 
            r = mid-1
    if flag == 0:
        step = ""
        for a in range(n):
            step += "_ "
        steps.append(step)
    return steps




app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        input_array = request.form['array']
        str_item = request.form['item']
        if str_item is not None:
            try:
                item = int(str_item)
                array = [int(x) for x in input_array.split()]
                ans_array = binary_search(array, item)
            except:
                ans_array = None
    else:
        ans_array=None
    return render_template("home.html", ans_array=ans_array)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)