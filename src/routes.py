from flask import Flask, send_file, redirect, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ainda não há nada aqui! v0.0.1"

@app.errorhandler(404)
def page_not_found():
    # Redirects to the app to download
    print('TESTANDO CARALHOOOOOO')
    ua = request.headers.get('User-Agent')
    apple = 'https://apps.apple.com/br/app/dreampuppy-galeria-de-filhotes/id6478811369?l=en-GB'
    google = 'https://play.google.com/store/apps/details?id=com.dreampuppy.gallery&hl=en_US'
    print(ua)
    return redirect(apple)


@app.route("/.well-known/apple-app-site-association")
def apple_deep_linking():
    return send_file(path_or_file=".well-known/apple-app-site-association")


# https://www.dreampuppy.com.br/suporte
@app.route("/suporte")
def suport_redirect():
    return redirect('https://wa.me/send?phone=5533997312898')


@app.route("/documents/terms")
def get_terms_of_use():
    return send_file(path_or_file='docs/terms.docx', as_attachment=True)

@app.route("/documents/cnpj.pdf")
def get_cnpj():
    return send_file(path_or_file='docs/cnpj.pdf')

@app.route("/documents/policy")
def get_policy():
    return send_file(path_or_file='docs/policy.docx', as_attachment=True)

@app.route("/documents/lgpd")
def get_lgpd():
    return send_file(path_or_file='docs/lgpd.docx', as_attachment=True)
