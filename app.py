from flask import Flask, request, jsonify

app = Flask(__name__)


def calculate_max_draws(p1, p2, p3):
    total_points = p1 + p2 + p3
    if total_points&1:
        return -1
    else:
        if p1+p2 >= p3:
            return (total_points//2)
        elif p1+p2 < p3:
            return p1+p2
    return -1

@app.route('/<int:p1>/<int:p2>/<int:p3>', methods=['GET'])

def get_max_draws(p1, p2, p3):
    if p1 > p2 or p2 > p3:
        return jsonify({"error": "Scores must be in non-decreasing order"}), 400

    max_draws = calculate_max_draws(p1, p2, p3)
    return jsonify({"max_draws": max_draws})

if __name__ == '__main__':
    app.run(debug=True)

    
