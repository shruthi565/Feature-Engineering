# 📊 Sales Data Analysis and Visualization

This project analyzes customer sales data using **Python, Pandas, Matplotlib, and Seaborn**. It includes data cleaning, statistical analysis, outlier detection, and different visualizations.

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

## 📂 Project Structure

```text
Sales-Data-Analysis/
│
├── feature.py
├── sales_data.csv
└── README.md
```

## 🔍 Features

The project performs:

* Loading the sales dataset
* Checking the dataset shape and contents
* Displaying basic statistics
* Checking and handling missing values
* Filling missing Age values using the median
* Creating a Spending distribution histogram
* Creating a Spending boxplot
* Detecting Age outliers using the IQR method
* Creating an Age vs Spending scatter plot
* Creating a correlation heatmap

## 📈 Visualizations

The project generates the following graphs:

1. **Spending Distribution Histogram**
2. **Spending Boxplot**
3. **Age vs Spending Scatter Plot**
4. **Correlation Heatmap**

## 📊 Outlier Detection

The project uses the **IQR (Interquartile Range)** method to identify possible outliers in the Age column.

```python
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

## ▶️ How to Run

### 1. Install the required libraries

```bash
pip install pandas matplotlib seaborn
```

### 2. Keep the files in the same folder

Make sure:

```text
feature.py
sales_data.csv
```

are in the same folder.

### 3. Run the program

```bash
python feature.py
```

The program will display the analysis results and graphs.

## 🎯 Objective

The main objective of this project is to understand customer sales data through **data cleaning, exploratory data analysis (EDA), visualization, correlation analysis, and outlier detection**.

