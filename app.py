from flask import Flask, request, render_template_string

app = Flask(__name__)


def load_codes():
    codes = {}
    with open('codes.txt', 'r') as f:
        for line in f:
            code, difficulty = line.strip().split(',')
            codes[code] = difficulty
    return codes


codes = load_codes()


@app.route('/access', methods=['GET', 'POST'])
def access():
    if request.method == 'POST':
        code = request.form['code'].lower()
        difficulty = codes.get(code)
        if difficulty:
            return render_template_string(open(f'templates/{difficulty}.html').read())
        else:
            return "Invalid code", 400
    return '''
    <!DOCTYPE html>
<html lang="en">

<head>
    <link rel="icon" type="image/x-icon"
        href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAA21BMVEXPFCsAJH3////OECgSM4bOCSP64+f86+7OABLTGjbRDC4AHXrg5fAWNogAGnm9xt0zQYlSXZjSJDr1zdLUQk7209fWSlUAJX3NAB8AAG8AFXbKAAD3+fwAIHvMABoAEHfv8vcABnLV2ef99vfTL0EkQ48AE3mPmb5tfbBNZKTmiZXolp+FkbzN0uM4SI+LlrtDT5B6h7QjPIvqoKfqqa9rfLH32t3nmaBMUYwAAHfidIHYVF9EXKDfZ3XRNUJabKfojZnutLm1vtgkLn3cTmDzwsjQNj7dW2vgfYYy7QtzAAAID0lEQVR4nO3daUPaWBQG4EtCWCs6IYGwBBVwallscYEpThHbMs3//0UTFjHLSXLvJWt73q9Tr3ka5D1Q50Bu8iGl+fJBsKYgytSpDG1fKpzfhXVV+RuS13PhpPaXQ1gSCW20skN4UQ3pqvQ8yYd01ElCKTJhDoUMQSEKUcgZFDIEhShEIWdQyBAUohCFnEEhQ1CIQhRyBoUMQSEKUcgZFDIEhShEIWf+BKGuN8M5Kp3Cao08tVrh/CtwGoXV1tcJEfpPzXYY56VOqFfbZ7MrgZjnTW/va6efmDKhXqveTbZXRPYnzi7atd9JqNdqXyb93Vl7odA9n91fnnZqioR67e+7j9PDWeTt0J3xlPuYFmFTb19+OfosQkG4Op+cXfOfnBZh7dK8f933s4j14KvprHnN2x3pENZa9x/7XetZxH50t3972eKbAdIgrLb0zx+69stwCM18+PSVawZIXlhtXd9e2Q8qjoZuoSD0X3hmgISFh363X4IhdcqQkG8GSFR47Pf3DArrckkiMiw0v8ct6wyQoNDS70fffCybPuItZJ8BEhPa+v3gUxfDnc9PyGxMRujs971vrPS0w9F+wv0MQG1MRujsdzPquiFpx6P9hUwzQBJCd78L85EiaZbvHCRkmAHiF0L9bqwkyfZ9g4UC7QwQtxDsd7knOb4rlZBuBohVCPb7SOxIrqMphTQzQIxCsN/H5ZLbJ0pl8lgY0BmDZoDYhGC/H/vP5tMkZUwqjcc5HTGgH2MSgv3+MCxprkNFTWus6wIxfzafH1iMXvcxDiHU74K6eO93S7SeMlbN/2z+JIqa+LygNPq8DxCHEOr3ccPWf28nllaL+e7nzxRu76fYWBcpjV4zQPRCsN8bIuirLN6eX3bC3c9kY0xp9JgBohYC/V509fubb1Q8Pn8ehNvnVW21oHxa3c4Al877GK0Q6ve1+RziPkssSYb1Xh2F2+/TkR9pjf1Pek2PTVhtN12+cQXod/PBWF4WbH/QKjSff0rKK+VjVTh/+WGbASITmv13cet4/iw+rsB+14ZL1XGddiEhvVLjtSBQpfvdNgNEJNz2+8zRf/NHBew/STHqrst0ConY6/1kmgFqEQqbUL/PH1be/e4OKbv/LNMMMLk4GMMXNnPtS6fP7PeGX78DQnieY5gBpocZIHxh7drV7/Pxs3+/A8L5qAIayTNtPx5mgLCFUL+vA/sdEJqPa0MELoZ1Brhuhypst/SJq98VuN9FS79Dwu3fzbIHGSVNeaCfAVr/hCj88dXZf4P10PX6fefTDP/7cHgFXFiSHnBBUqe8oO3H/iQ84XTiml/Afpd68ijo+o6v8efLoSa50+vID36PAe+cIrRn+/q90wMuTlsZwd1teRejbjQUKMOfm0SFg9fnldKAYtA839vep1HrYDZ1npsYnrBeV8HQ9RntO1HsCe9RelpQyB8UojCsoJA/KERhWEEhf1CYfWExLcJiVKmzCOXILqNIpFJE6VH7yPYfG6KKRGQxqrAISWRXIbve8/7dgsLsB4XZDwqzHxRmPyjMflCY/aAw+0Fh9oPC7AeF2Q8Ksx8UZj8ozH5QmP2gMPtBYfaDwuwHhdkPCrMfFGY/MqkA/z9ROGG6kMiuokLkSlRh+rWvyK6Cej8Ne5h+v1SO7DL+hN8vjezk3/93hFGIwrCCQv6gEIVhBYX8QSEKwwqVcADvNFB9ly1ELyxuNvASCNuyDBrhZglupVBWv16TFS5W/4GbPJ7XFmOwcPNN9lp64rsYNIZH6aBgaB3o4kRl9L5zL+AQ9RsB9hZtF9c4FxBNQ91PYz/LOwWP5UG94fhtb6Lflw/UX6WAr39L/9+Qdww9OXbweBsN2WN50P4e+AgH6rce8LWi7TGwS3f6dB39nijPzI2VBi5YGj4UfIRFFb7/GmmM7Yt9rqa3eiS7vs6cu748o8JGraQ8AJ9vsfdtjDLocy1yuzqf5SPb13bh3NfmmfpI0aBFdaVnUDjYGENocaamOZfxdc8n95Ht3DvsnKUjDupjaNmuWIGEr8ZQg3wl5dHps+xOjmQz5HZv4mdaozoGFggC75dull4+1/27vY9n9+WE1jhfi06jS1hfypDv8Lxku4qn+7j2l1YvZn1KY8GQ7EaHkKHfXXvoI9xBq1fb+RnnDGATMvW7ax901HuEGWaApWUGeBcO5t/g+Qfu9/h3Qet8M8CbsKgaGtx/Hv3uThz7vDlmgL2wWDdkj34fe/R7EkL2GUDaCxn6/fvsLNG9+uwzgGQKN9v7Cfigfvf2xfrZCPQzwHooEs/5Bep3v8/ViPfzLehnAFLh6/cEhYwzAPC7GEC/p/FzZmhnAKeQtt8TFuboZwC7kL7fkxfSzgBW4fb1+9rZ7yn/zK7gGeBd6PH6Pe2fuxY4AxyFjP2eFmHwDHAQMvd7eoRBM8BOqJVW7n6/YPws0qQ/w9LLaAp3/W5/Ap0G9nuqhL4zACl3Kjz9njKhzwxAVnz9njphzmsGIPb71+1T9nsahfAM4Pxc7lzmP5fbOQPYPlvd8/V7doTuGeAoZOz39AqdM8BByNzvaRbaZwCy9zH3e6qFthlgK+Tp95QLLTMA4ez31AuPMwB54ut3d1InzO1mgBnR+frdnTQKTWON5EM6KqXCXB6F9EEhClHIGRQyBIUoRCFnUMgQFKIQhZxBIUNQiEIUcgaFDEEhClHIGRQyBIUoRCFn/ghhOP8CfJpQcwlP+72Q9+h5cnMWUvIvDqEoU6cydAjv8mFd1s3/OTHn2xZxrA0AAAAASUVORK5CYII=">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Cairo:wght@200..1000&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
        rel="stylesheet">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Level Test</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">
        <h1>English Level Test</h1>
        <h5>Code authentication</h5>
        <p id="thing" style="text-align: center;">Please enter the code given to you by your test's adminstraitor.</p>
        <form method="POST">
            <div class="input-group mb-3">
                <input type="text" style="text-align: center;" name="code" class="form-control" placeholder="Enter Code" id="code">
            </div>
            <button id="submit-btn" class="btn btn-primary">Submit</button>
        </form>
        <p style="text-align: center;font-family: 'Roboto', sans-serif;font-weight: 300;font-style: normal;"><i>made
                by Mouad Coding For Teacher Ms.Messahel <br> (This is currently a Placeholder for now)</i></p>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.1/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script src="script.js"></script>
</body>

</html>

    '''


if __name__ == '__main__':
    app.run(debug=True)
