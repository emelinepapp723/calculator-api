from fastapi import FastAPI, status, HTTPException


app = FastAPI()




@app.get("/", status_code=200)
def read_root():
   """Health check endpoint"""
   return {"status": "healthy"}




@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
   """
   Add two numbers together.
  
   Parameters:
   - a: First number
   - b: Second number
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   return {"operation": "add", "a": a, "b": b, "result": a + b}


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
   """
   Subtract two numbers together.
  
   Parameters:
   - a: First number
   - b: Second number
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   return {"operation": "subtract", "a": a, "b": b, "result": a - b}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
   """
   Multiply two numbers together.
  
   Parameters:
   - a: First number
   - b: Second number
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   return {"operation": "multiply", "a": a, "b": b, "result": a * b}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
   """
   Divide two numbers together.
  
   Parameters:
   - a: First number
   - b: Second number
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   if b == 0:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Division by zero is not allowed. Please provide a non-zero value for b.")
   return {"operation": "divide", "a": a, "b": b, "result": a / b}


@app.get("/average/{a}/{b}/{c}", status_code=200)
def average(a: str, b: str, c: str):
   """
   Average 3 numbers.
  
   Parameters:
   - a: First number
   - b: Second number
   - c: Third number
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
       c = float(c)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. All parameters must be valid numbers")
   return {"operation": "average", "a": a, "b": b, "c": c, "result": (a + b + c) / 3}


@app.get("/tip/{a}/{b}", status_code=200)
def tip(a: str, b: str):
   """
   Calculate the amount you want to tip.
  
   Parameters:
   - a: Bill total
   - b: Tip %
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   return {"operation": "tip", "bill": a, "tip %": b, "tip": a * (b/100)}


@app.get("/gas/{a}/{b}/{c}", status_code=200)
def gas(a: str, b: str, c: str):
   """
   Calculate the fuel cost of a road trip.
  
   Parameters:
   - a: Car mileage (miles per gallon)
   - b: Cost of gas ($)
   - c: Trip distance (miles)
  
   Returns:
   - JSON object with the result
   """
   try:
       a = float(a)
       b = float(b)
       c = float(c)
   except ValueError:
       raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Error status 422. Both 'a' and 'b' must be valid numbers")
   return {"operation": "gas", "mpg": a, "gas cost": b, "distance": c, "trip cost": (c/a)*b}
