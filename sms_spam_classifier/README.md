
# SMS Spam Filtering

## Overview

SMS Spam Filtering is a machine learning-based system designed to detect and filter out unwanted and unsolicited text messages (SMS spam). It is a useful tool for mobile phone users who want to automatically filter out spam messages and keep their SMS inbox clean.

## Features

- **Data Preprocessing:** The system includes data preprocessing steps to clean and prepare the SMS messages for classification.

- **Machine Learning Models:** Various classification models, such as Naive Bayes, Support Vector Machine (SVM), and deep learning models, are employed to classify SMS messages as spam or not spam.

- **Custom Rules:** Users can define custom rules for filtering messages based on keywords, sender numbers, or other criteria.

- **Blocking and Whitelisting:** The system allows users to block specific senders or whitelist trusted contacts to personalize the filtering process.

- **Reporting:** Users can report incorrectly classified messages to improve the system's accuracy and performance.

- **User-friendly Interface:** The system provides an intuitive and user-friendly interface for configuring and managing filtering settings.

## Requirements

To use this project, you will need the following:

- Python 3.x
- Required Python libraries (specified in the `requirements.txt` file)
- A dataset of labeled SMS messages (spam and not spam) for training (you can use public datasets or create your own)

## Installation

1. Clone or download this repository to your local machine.

2. Navigate to the project directory.

cd SMS-Spam-Filtering


3. Create a virtual environment (optional but recommended).

python -m venv venv
source venv/bin/activate # On Windows, use 'venv\Scripts\activate'


4. Install the required Python libraries.

pip install -r requirements.txt


## Usage

1. Open the Jupyter Notebook or Python IDE.

2. Open the `SMS_Spam_Filtering.ipynb` notebook to start using the system.

3. Follow the instructions in the notebook to load and preprocess data, train machine learning models, and evaluate the performance.

4. You can also modify the notebook to suit your specific needs, add more data, or change the machine learning models.

## Data

The project requires a dataset of labeled SMS messages, with labels indicating whether each message is spam or not spam. You can find public datasets or create your own dataset for training and testing.


## Acknowledgments

- The project may use publicly available SMS spam datasets from sources like Kaggle or academic repositories.


