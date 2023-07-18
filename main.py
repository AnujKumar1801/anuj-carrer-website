from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/')
def front_page():
    return render_template('index.html')

@app.route('/resume')
def resume_page():
    return render_template('resume.html')

@app.route('/download')
def download_resume():
    resume_path = 'resume.pdf'  # Specify the path to your resume.pdf file
    return send_file(resume_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
