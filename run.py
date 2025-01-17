from app import create_app, config

app = create_app(config)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
