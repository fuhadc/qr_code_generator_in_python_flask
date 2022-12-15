from flask import Flask, request, redirect, url_for
import qrcode

app = Flask(__name__)

@app.route('/')
def display_form():
    if 'qr' in request.args:
        qr = request.args['qr']
        return '<img src="{}">'.format(qr)
    else:
        return '''
        <form action="/generate" method="POST">
            <input type="text" name="data">
            <input type="submit" value="Generate QR code">
        </form>
        '''

@app.route('/generate', methods=['POST'])
def generate_qr_code():
    data = request.form['data']
    qr = qrcode.make(data)
    return redirect(url_for('display_form', qr=qr))

if __name__ == '__main__':
    app.run(port=5100,debug=True)
