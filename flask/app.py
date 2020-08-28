from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')
app.debug = True

def noop(input=None, *args, **kwargs):
    return input

def sink(input="", *args, **kwargs):
    return ""

@app.template_test("in_manifest")
def in_manifest(obj, *args, **kwargs):
    return False

@app.template_filter('to_json')
def to_json(s):
    return noop(s)

@app.template_filter('embedded_json_ld')
def embedded_json_ld(s):
    return noop(s)

@app.template_filter('placeholder')
def placeholder(s, *args, **kwargs):
    return noop(s)

@app.template_filter('mdstrip')
def mdstrip(s):
    return noop(s)

@app.template_filter('dateformat')
def dateformat(s):
    return noop(s)

@app.template_filter('url_del')
def url_del(s):
    return noop(s)

@app.template_filter('owner_avatar')
def owner_avatar(s, *args, **kwargs):
    return noop(s)

@app.template_filter('owner_name')
def owner_name(s):
    return noop(s)

@app.template_filter('avatar_url')
def avatar_url(s):
    return noop(s)

@app.template_filter('obfuscate')
def obfuscate(s):
    return noop(s)

@app.context_processor
def inject_Vars():
    return dict(_=noop, theme=noop, reuse="", hook=sink, theme_static=noop, current_site={'keywords': []}, static=noop, url_for=noop, i18n_alternate_links=sink, csrf_token=noop, current_user=None, config={'LINKCHECKING_ENABLED': False, 'LINKCHECKING_UNCHECKED_TYPES': False, 'MD_ALLOWED_TAGS': [], 'MD_ALLOWED_ATTRIBUTES': [], 'MD_ALLOWED_STYLES': [], 'TAG_MIN_LENGTH': 0, 'TAG_MAX_LENGTH': 0}, manifest=noop, current_theme=None, package_version=noop)

# Warning : this is a security hole, don't use this in prod !
@app.route('/static/<path:path>')
def static_file(path):
        return send_from_directory('../temp/', path)

@app.route('/<template>')
def templates(template=None):
    return render_template('home.html', template=template)