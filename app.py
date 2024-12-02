from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        target_time = request.form['target_time']
        late_by = int(request.form['late_by'])

        # Convert target time to datetime object
        target_time = datetime.strptime(target_time, "%H:%M")

        # Calculate reminder time (earlier by 'late_by' minutes)
        reminder_time = target_time - timedelta(minutes=late_by)

        # Format reminder time to show to the user
        reminder_time_str = reminder_time.strftime("%H:%M")

        return render_template('index.html', reminder_time=reminder_time_str)
    
    return render_template('index.html', reminder_time=None)

if __name__ == '__main__':
    app.run(debug=True)
