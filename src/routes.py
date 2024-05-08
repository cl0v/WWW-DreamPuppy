from flask import Flask, send_file, redirect, request, render_template

app = Flask(__name__)

UNDER_CONSTRUCTION_STR: str = "Site em construção, aguarde as próximas versões (v0.0.2)"

@app.route("/")
def hello():
    return UNDER_CONSTRUCTION_STR

# @app.errorhandler(404)
# def page_not_found():
#     # Redirects to the app to download
#     print('TESTANDO CARALHOOOOOO')
#     ua = request.headers.get('User-Agent')
#     apple = 'https://apps.apple.com/br/app/dreampuppy-galeria-de-filhotes/id6478811369?l=en-GB'
#     google = 'https://play.google.com/store/apps/details?id=com.dreampuppy.gallery&hl=en_US'
#     print(ua)
#     return redirect(apple)


@app.route("/filhotes/<pet_id>")
def get_puppy_details(pet_id):
    # return redirect('ipets://www.dreampuppy.com.br/filhotes/'+str(pet_id))
    # Template usado:
    # https://learning-zone.github.io/website-templates/portfolio-item/
    # https://github.com/learning-zone/website-templates/tree/master/portfolio-item
    import requests as rq
    url = 'https://api.dreampuppy.com.br/puppies/' + str(pet_id)
    res = rq.get(url)
    petjson = res.json()
    if petjson['gender'] == 1:
        gender = 'Macho'
    else:
        gender = 'Fêmea'
    pet = {'id': pet_id,
             'gender': gender,
             'pedigree': 'CBKC',
             'age' : 60,
             'breed': petjson['breed'],
             'price': petjson['price'], 
             'images': petjson['images']}
    return render_template("puppies.html", pet=pet)

@app.route("/.well-known/apple-app-site-association")
def apple_deep_linking():
    return send_file(path_or_file=".well-known/apple-app-site-association")

@app.route("/.well-known/assetlinks.json")
def google_deep_linking():
    return send_file(path_or_file=".well-known/assetlinks.json")


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
