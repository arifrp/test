from flask import Flask, render_template_string

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heartbreak Story</title>
    <style>
        body {
            font-family: 'Courier New', Courier, monospace;
            background-color: #2c3e50;
            color: #ecf0f1;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            overflow: hidden;
        }
        .container {
            text-align: center;
            max-width: 600px;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #e74c3c;
            animation: fadeIn 2s ease-in-out;
        }
        .message {
            font-size: 1.5em;
            margin: 20px 0;
            animation: fadeIn 3s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes blinkCursor {
            from { border-right-color: rgba(255, 255, 255, 0.75); }
            to { border-right-color: transparent; }
        }
        #message {
            border-right: 2px solid rgba(255, 255, 255, 0.75);
            white-space: nowrap;
            overflow: hidden;
            animation: blinkCursor 0.7s step-end infinite;
        }
    </style>
    <script>
        let messages = [
            "Once upon a time, everything was perfect...",
            "We laughed together, shared dreams...",
            "But then, it all came crashing down...",
            "Promises were broken, and tears were shed...",
            "Now, the heart aches with every beat...",
            "Trying to move on, but the memories linger...",
            "Healing takes time, but it will happen...",
            "One day, the heart will be whole again..."
        ];

        function typeWriter(text, i, fnCallback) {
            if (i < (text.length)) {
                document.getElementById("message").innerHTML = text.substring(0, i+1) +'<span aria-hidden="true"></span>';
                setTimeout(function() {
                    typeWriter(text, i + 1, fnCallback)
                }, 100);
            } else if (typeof fnCallback == 'function') {
                setTimeout(fnCallback, 2000);
            }
        }

        function StartTextAnimation(i) {
            if (typeof messages[i] == 'undefined') {
                setTimeout(() => { StartTextAnimation(0); }, 2000);
                return;
            }
            typeWriter(messages[i], 0, function(){
                StartTextAnimation(i + 1);
            });
        }

        document.addEventListener("DOMContentLoaded", function() {
            StartTextAnimation(0);
        });
    </script>
</head>
<body>
    <div class="container">
        <h1>Heartbreak Story</h1>
        <div id="message" class="message"></div>
    </div>
</body>
</html>
"""

@app.route('/')
def heartbreak():
    return render_template_string(html_template)

if __name__ == "__main__":
    app.run(debug=True)
