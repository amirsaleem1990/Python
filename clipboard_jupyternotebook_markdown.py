
import clipboard
def change(text):
    ok_list = ["- <font color='red'>"+i.strip().replace('&nbsp;', "")+"</font><br>" 
               for i in text.splitlines()]
    final = ''
    for i in ok_list:
        if i != "- <font color='red'></font><br>":
            final += i + '\n'
    clipboard.copy(final.strip())
change("""
Male
Age
[correct]Number of Cigarettes per day
Previously had a Stroke
Hypertensive
Total Cholesterol Level
Systolic Blood Pressure
Blood Glucose Level
""")