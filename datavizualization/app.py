from flask import Flask, render_template, request, Response
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd

app = Flask(__name__)

# Sample data
def get_data():
    data = {
        'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Sales': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600],
        'Expenses': [1200, 1300, 1250, 1400, 1350, 1500, 1450, 1600, 1550, 1700, 1650, 1800],
        'Profit': [300, 300, 450, 400, 550, 500, 650, 600, 750, 700, 850, 800]
    }
    return pd.DataFrame(data)

@app.route('/')
def index():
        df = pd.read_csv('sales_data.csv')
        months = df['Month'].unique()
        return render_template('index.html', months=months)

@app.route('/plot')
def plot():
    month = request.args.get('month', 'All')
    
    try:
        df = pd.read_csv('sales_data.csv')
        if month != 'All':
            df = df[df['Month'] == month]

        img_sales = plot_chart(df, 'Sales', 'Sales')
        img_expenses = plot_chart(df, 'Expenses', 'Expenses')
        img_profit = plot_chart(df, 'Profit', 'Profit')
        
        return render_template('dashboard.html',
                               sales_plot=img_sales,
                               expenses_plot=img_expenses,
                               profit_plot=img_profit)
    except Exception as e:
        return str(e)

def plot_chart(df, column, title):
    img = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df[column], marker='o')
    plt.title(title)
    plt.xlabel('Month')
    plt.ylabel(title)
    plt.grid(True)
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')

@app.route('/export')
def export():
    df = pd.read_csv('sales_data.csv')
    csv = df.to_csv(index=False)
    return Response(csv, mimetype='text/csv', headers={"Content-Disposition": "attachment;filename=sales_data.csv"})


@app.route('/dashboard')
def dashboard():
    data = get_data()
    
    # Sales Plot
    img_sales = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(data['Month'], data['Sales'], marker='+', color='blue')
    plt.title('Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(img_sales, format='png')
    img_sales.seek(0)
    sales_plot_url = base64.b64encode(img_sales.getvalue()).decode('utf8')

    # Expenses Plot
    img_expenses = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(data['Month'], data['Expenses'], marker='o', color='red')
    plt.title('Monthly Expenses')
    plt.xlabel('Month')
    plt.ylabel('Expenses')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(img_expenses, format='png')
    img_expenses.seek(0)
    expenses_plot_url = base64.b64encode(img_expenses.getvalue()).decode('utf8')

    # Profit Plot
    img_profit = io.BytesIO()
    plt.figure(figsize=(10, 6))
    plt.plot(data['Month'], data['Profit'], marker='x', color='green')
    plt.title('Monthly Profit')
    plt.xlabel('Month')
    plt.ylabel('Profit')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(img_profit, format='png')
    img_profit.seek(0)
    profit_plot_url = base64.b64encode(img_profit.getvalue()).decode('utf8')

    return render_template('dashboard.html', sales_plot_url=sales_plot_url, expenses_plot_url=expenses_plot_url, profit_plot_url=profit_plot_url)




if __name__ == "__main__":
    app.run(debug=True)
