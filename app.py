from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            current_amount = float(request.form['current_amount'])
            weeks_passed = int(request.form['weeks_passed'])
            
            fine = 0
            for _ in range(weeks_passed):
                new_fine = current_amount * 0.07
                current_amount += 10 + new_fine
                fine += new_fine

            return render_template_string('''
                <!DOCTYPE html>
                <html lang="th">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>ผลการคำนวณ</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f9;
                            margin: 0;
                            padding: 20px;
                        }
                        .container {
                            max-width: 600px;
                            margin: auto;
                            background: #fff;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }
                        h1 {
                            color: #333;
                        }
                        p {
                            font-size: 18px;
                            color: #555;
                        }
                        a {
                            text-decoration: none;
                            color: #007bff;
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>ผลการคำนวณ</h1>
                        <p>ดอกเบี้ยสะสม (บาท) : {{ fine }}</p>
                        <p>เงินสุดท้ายที่ต้องจ่าย (บาท) : {{ current_amount }}</p>
                        <a href="/">กลับไปที่หน้าแรก</a>
                    </div>
                </body>
                </html>
            ''', fine=fine, current_amount=current_amount)

        except ValueError:
            return render_template_string('''
                <!DOCTYPE html>
                <html lang="th">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>เกิดข้อผิดพลาด</title>
                    <style>
                        body {
                            font-family: Arial, sans-serif;
                            background-color: #f4f4f9;
                            margin: 0;
                            padding: 20px;
                        }
                        .container {
                            max-width: 600px;
                            margin: auto;
                            background: #fff;
                            padding: 20px;
                            border-radius: 8px;
                            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        }
                        h1 {
                            color: #333;
                        }
                        p {
                            font-size: 18px;
                            color: #555;
                        }
                        a {
                            text-decoration: none;
                            color: #007bff;
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>เกิดข้อผิดพลาด</h1>
                        <p>โปรดป้อนข้อมูลที่ถูกต้อง</p>
                        <a href="/">กลับไปที่หน้าแรก</a>
                    </div>
                </body>
                </html>
            ''')

    return '''
        <!DOCTYPE html>
        <html lang="th">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>คำนวณค่าปรับ</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    margin: 0;
                    padding: 20px;
                }
                .container {
                    max-width: 600px;
                    margin: auto;
                    background: #fff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #333;
                }
                form {
                    display: flex;
                    flex-direction: column;
                }
                label {
                    margin-bottom: 8px;
                    font-weight: bold;
                }
                input[type="text"] {
                    padding: 8px;
                    margin-bottom: 12px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                }
                input[type="submit"] {
                    padding: 10px;
                    border: none;
                    border-radius: 4px;
                    background-color: #007bff;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }
                input[type="submit"]:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>คำนวณค่าปรับ</h1>
                <form method="post">
                    <label for="current_amount">โปรดป้อนเงิน ณ ปัจจุบัน (บาท):</label>
                    <input type="text" id="current_amount" name="current_amount" required>
                    
                    <label for="weeks_passed">จำนวนเงินเมื่อผ่านไป (สัปดาห์):</label>
                    <input type="text" id="weeks_passed" name="weeks_passed" required>
                    
                    <input type="submit" value="คำนวณ">
                </form>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
