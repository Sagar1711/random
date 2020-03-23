import connexion

if __name__ == "__main__":
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('api.yml')
    app.run(host="127.0.0.1", port=8080)
