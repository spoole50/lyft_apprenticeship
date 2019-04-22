from flask import Flask, request, render_template, url_for, jsonify

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def endpoint():
    if request.method == 'POST':
        in_data = request.get_json(force=True)
        out_str = in_data['string_to_cut']
        res_str = ""
        xi = 0
        for c in out_str:
            if (xi == 2):
                res_str += c
                xi = -1
            xi += 1
        out_dict = {"return_string": res_str}
        return jsonify(out_dict)

if __name__ == '__main__':
    app.run(debug=True)
