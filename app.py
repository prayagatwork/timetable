from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Define the upload directory
UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

# Create the upload directory if it doesn't exist
if not os.path.exists(UPLOADS_DIR):
    os.makedirs(UPLOADS_DIR)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['file']

        # Check if the file is an Excel file based on its filename
        if not file.filename.endswith(('.xls', '.xlsx')):
            return 'File is not an Excel file. Please upload a valid Excel file.'

        # Save the file to the upload directory
        file_path = os.path.join(UPLOADS_DIR, file.filename)
        file.save(file_path)

        try:
            # Process the uploaded file
            process_file(file_path)
            return 'File uploaded and processed successfully!'
        except Exception as e:
            return f'An error occurred while processing the file: {str(e)}'

    return render_template('index.html')

def process_file(file_path):
    import script
    script.process_file(file_path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



# from flask import Flask, request, render_template
# import os
# import base64
# import chardet

# app = Flask(__name__)

# # Define the upload directory
# UPLOADS_DIR = os.path.join(os.path.dirname(__file__), 'uploads')

# # Create the upload directory if it doesn't exist
# if not os.path.exists(UPLOADS_DIR):
#     os.makedirs(UPLOADS_DIR)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Get the uploaded file
#         file = request.files['file']

#         # Save the file to the upload directory
#         file_path = os.path.join(UPLOADS_DIR, file.filename)
#         file.save(file_path)

#         # Process the uploaded file
#         process_file(file_path)

#         return 'File uploaded and processed successfully!'
#     return render_template('index.html')

# def process_file(file_path):
#     # Read the file contents
#     with open(file_path, 'rb') as f:
#         file_bytes = f.read()

#     print(file_bytes)
#     # Encode the file contents as a base64 string
#     file_data = base64.b64encode(file_bytes).decode('utf-8')
#     # print(file_data)

#     # Process the file data using your script.py file
#     import script
#     script.process_file(file_data)

# if __name__ == '__main__':
#     app.run(debug=True)
