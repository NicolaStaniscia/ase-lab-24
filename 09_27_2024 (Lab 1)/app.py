from flask import Flask, request, make_response, jsonify, Response
import random as rnd
import ast
import os

app = Flask(__name__, instance_relative_config=True)

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        res = a + b

        with open("operations.txt", "a") as file:
            file.write(f"add({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200) #HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) #HTTP 400 BAD REQUEST

#Endpoint /sub for subtraction which takes a and b as query parameters.
@app.route('/sub')
def sub():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        res = a - b

        with open("operations.txt", "a") as file:
            file.write(f"sub({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response("Invalid input", 400)
    
#Endpoint /mul for multiplication which takes a and b as query parameters.
@app.route('/mul')
def mul():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        res = a * b

        with open("operations.txt", "a") as file:
            file.write(f"mul({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)

#Endpoint /div for division which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/div')
def div():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        res = a / b

        with open("operations.txt", "a") as file:
            file.write(f"div({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)

#Endpoint /mod for modulo which takes a and b as query parameters. Returns HTTP 400 BAD REQUEST also for division by zero.
@app.route('/mod')
def mod():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        res = a % b

        with open("operations.txt", "a") as file:
            file.write(f"mod({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)

#Endpoint /random which takes a and b as query parameters and returns a random number between a and b included. Returns HTTP 400 BAD REQUEST if a is greater than b.
@app.route('/random')
def random():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a <= b:
        res = rnd.randint(int(a), int(b))

        with open("operations.txt", "a") as file:
            file.write(f"random({a}, {b}) = {res}\n")
            file.close()
            
        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)

# ! BONUS

# /upper which given the string a it returns it in a JSON all in uppercase.
@app.route('/upper')
def upper():
    a = request.args.get('a', type=str)
    if a:
        res = str.upper(a)

        with open("operations.txt", "a") as file:
            file.write(f"upper({a}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)
    
# /lower which given the string a it returns it in a JSON all in lowercase.
@app.route('/lower')
def lower():
    a = request.args.get('a', type=str)
    if a:
        res = str.lower(a)

        with open("operations.txt", "a") as file:
            file.write(f"lower({a}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)
    
# /concat which given the strings a and b it returns in a JSON the concatenation of them.
@app.route('/concat')
def concat():
    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)
    if a and b:
        res = a + b

        with open("operations.txt", "a") as file:
            file.write(f"concat({a}, {b}) = {res}\n")
            file.close()

        return make_response(jsonify(result=res), 200)
    else:
        return make_response('Invalid input', 400)


# /reduce which takes the operator op (one of add, sub, mul, div, upper, lower, concat) and a lst string
#  representing a list and apply the operator to all the elements giving the result. For instance, 
# /reduce?op=add&lst=[2,1,3,4] return a JSON containing {result=10}, meaning 2+1+3+4.

@app.route('/reduce')
def reduce():
    op = request.args.get('op', type=str)
    lst = request.args.get('lst', type=str)
    if op and lst:
        lst = ast.literal_eval(lst)

        if op == 'add':
            res = sum(lst)
            with open("operations.txt", "a") as file:
                file.write(f"reduce('{op}', {lst}) = {res}\n")
                file.close()
            
            return make_response(jsonify(result=res), 200)
        
        elif op == 'sub':

            res = 0
            for x in lst:
                res -= x
            
            with open("operations.txt", "a") as file:
                file.write(f"reduce('{op}', {lst}) = {res}\n")
                file.close()

            return make_response(jsonify(result=res), 200)
        
        elif op == 'mul':
            res = 1
            for x in lst:
                res *= x

            with open("operations.txt", "a") as file:
                file.write(f"reduce('{op}', {lst}) = {res}\n")
                file.close()

            return make_response(jsonify(result=res), 200)

        elif op == 'div':
            res = 1
            for x in lst:
                res /= x

            with open("operations.txt", "a") as file:
                file.write(f"reduce('{op}', {lst}) = {res}\n")
                file.close()
            
            return make_response(jsonify(result=res), 200)

        elif op == 'concat':
            res = ""
            for x in lst:
                res += str(x)
            
            with open("operations.txt", "a") as file:
                file.write(f"reduce('{op}', {lst}) = {res}\n")
                file.close()

            return make_response(jsonify(result=res), 200)

        else:
            return make_response('Invalid input', 400)
        

    else:
        return make_response('Invalid input', 400)
    

# /crash which terminates the service execution after responding to the client with info about the host and 
# the port of the service

@app.route('/crash')
def crash():
    ip = request.remote_addr
    host = request.host
    if ":" in host: port = host.split(":")[-1]

    if ip and port: 
        response = make_response(jsonify(ip=ip, port=port), 200)
        response.call_on_close(lambda: os._exit(0))

        with open("operations.txt", "a") as file:
            file.write(f"crash() = {ip, port}\n")
            file.close()

        return response
    else: 
        return make_response('Invalid input', 400)


# /last which returns a string representing the last operation requested with success, in the format 
# op(args)=res, e.g. add(2.0,3.0)=5.0 or reduce(‘add’,[2,1,3,4])=10 or rand(1,3)=2. It answers with 
# HTTP code 404 if no operation was performed.
# Hint: to do this you have to modify the other endpoints and use a file

@app.route('/last')
def last():
    
    with open("operations.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1][:-1]
        else: return make_response("'File not found or empty")
    
    return make_response(jsonify(last_action=str(last_line)), 200)
    

if __name__ == '__main__':
    app.run(debug=True)
    