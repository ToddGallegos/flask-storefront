from app import app 

@app.route('/')
def homePage():
    return {
        "test": "hi"
    }

@app.route('/api', methods=["GET", "POST"])
def api():
    return {
        "response": "ok",
        "message": "Future API page"
    }