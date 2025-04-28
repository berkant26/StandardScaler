📦 MyStandardScaler
A simple implementation of a standard scaler in Python, designed for educational purposes.
It includes basic fit, transform, and fit_transform functionalities, similar to Scikit-Learn's StandardScaler.

✨ Features
Compute mean and standard deviation of input data.

Standardize data to have zero mean and unit variance.

Custom implementation without using external libraries like scikit-learn.

Fully tested with unit tests.

📂 Project Structure

StandardScaler/
│
├── scaler/
│   └── standard_scaler.py   # Implementation of MyStandardScaler
│
├── tests/
│   └── test_scaler.py       # Unit tests for MyStandardScaler
│
└── README.md                # Project description


🚀 How to Use
1. Clone this repository:


git clone https://github.com/your-username/StandardScaler.git
cd StandardScaler

2.Run the unit tests:
python -m unittest discover


3 -Example usage:


from scaler.standard_scaler import MyStandardScaler
import numpy as np

X = np.array([[1], [2], [3]])
scaler = MyStandardScaler()
scaler.fit(X)
transformed = scaler.transform(X)
print(transformed)



🛠️ Requirements
Python 3.8+

Numpy
