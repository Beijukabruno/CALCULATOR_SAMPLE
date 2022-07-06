from flask import Flask, render_template, request
import os 

# this was created with the attached code in the motivation folder as the idea


# Creating our Flask Instance

Flask_App = Flask(__name__) 


@Flask_App.route('/', methods=['GET'])
def home():
    # Our home page will be redirected to the templates with the html code

    return render_template('home.html')

@Flask_App.route('/calculation_result/', methods=['POST'])
def calculation_result():
    # this is going to be ruturnimg the results of our operation

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name= "
    first_input = request.form['Input1']  
    second_input = request.form['Input2']
    operation = request.form['operation']

    try:
        input1 = float(first_input)
        input2 = float(second_input)

        # On default, the operand  on webpage is addition
        # one can make a selection of the different choices available

        if operation == "+":
            result = input1 + input2   # addition

        elif operation == "-":
            result = input1 - input2   # subtraction

        elif operation == "/":
            result = input1 / input2    # division

        elif operation == "*":
            result = input1 * input2    # multiplication

        else:
            operation = "%"
            result = input1 % input2     # modulus or the remainder



        # this is for the case when its successful and the result is printed
        return render_template('home.html',input1=input1,input2=input2,operation=operation,result=result,calculation_success=True)
        
        # this is to cater for the case when someone divides a number by zero which would be infinity
    except ZeroDivisionError:
        return render_template('home.html',input1=input1,input2=input2,operation=operation,result="Math ERROR!!",calculation_success=False,error="INVALID input")
        
        # this caters for running the calculator without inputs or operands
    except ValueError:
        return render_template('home.html',input1=first_input,input2=second_input,operation=operation,result="Syntax ERROR!!",calculation_success=False,error="INVALID input")
            

if __name__ == '__main__':
    # displaying the error on the webpage
    #Flask_App.debug = True
    port = int(os.environ.get("PORT", 5000))
    Flask_App.run(debug=True,host='0.0.0.0',port=port)

  