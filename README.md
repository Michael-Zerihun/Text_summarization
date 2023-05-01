# Project Overview 

The project is a web-based application that takes long text input and summarizes it using Hugging Face's 🤗  Transformers library. The project uses the PyTorch framework to train and deploy the model and the Flask framework to create a web interface for users to interact with. The frontend is designed using the Bootstrap CSS framework.

## Requirements

The following are the requirements for running the project:

* Python 3.7 or higher
* PyTorch library
* Hugging Face Transformers library
* Flask library
* Bootstrap CSS framework

## Usage

Open a web browser and navigate to http://localhost:5000/ to access the web interface.
Enter the long text you want to summarize in the text area provided.
Click on the "Summarize" button to generate a summary of the text.
The summary will be displayed in the "Summary" section next to the text area.

## Installation
1. Clone the repository from GitHub:

```
git clone https://github.com/Michael-Zerihun/Text_summarization.git

```
2. Install the required Python libraries:
```
pip install torch transformers flask
```
## Project Structure
The project directory structure is as follows:
```
├── app.py
├── env
│   └── ...
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── script.js
│   └── img
├── templates
│   ├── base.html
│   └── index.html
└── README.md
```
## Conclusion
This project demonstrates how to use Hugging Face's Transformers library, PyTorch framework, Flask framework, and Bootstrap CSS framework to create a web-based application that summarizes long text. The project structure is well-organized, making it easy to understand and navigate. The model used in the project is a pre-trained summarization model provided by the Transformers library, which makes it easy to generate high-quality summaries.

Overall, this project serves as a great example of how to use various libraries and frameworks to create a useful web application. It can be used as a starting point for building more complex applications that require natural language processing capabilities.