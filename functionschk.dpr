program FunctionsExample;

{$APPTYPE CONSOLE}

uses
  SysUtils;

// Function to add two numbers
function AddNumbers(A, B: Integer): Integer;
begin
  Result := A + B;
end;

// Function to subtract two numbers
function SubtractNumbers(A, B: Integer): Integer;
begin
  Result := A - B;
end;

// Function to multiply two numbers
function MultiplyNumbers(A, B: Integer): Integer;
begin
  Result := A * B;
end;

// Function to divide two numbers
// It includes error handling for division by zero
function DivideNumbers(A, B: Integer): Double;
begin
  if B = 0 then
    raise Exception.Create('Error: Division by zero!')
  else
    Result := A / B;
end;

var
  num1, num2: Integer;
  sum, difference, product: Integer;
  quotient: Double;
begin
  // Input two numbers
  Write('Enter the first number: ');
  ReadLn(num1);
  Write('Enter the second number: ');
  ReadLn(num2);

  // Perform calculations using the functions
  sum := AddNumbers(num1, num2);
  difference := SubtractNumbers(num1, num2);
  product := MultiplyNumbers(num1, num2);

  try
    quotient := DivideNumbers(num1, num2);
    WriteLn('Quotient: ', quotient:0:2);
  except
    on E: Exception do
      WriteLn(E.Message);
  end;

  // Display the results
  WriteLn('Sum: ', sum);
  WriteLn('Difference: ', difference);
  WriteLn('Product: ', product);

  // Wait for the user to press Enter before exiting
  ReadLn;
end.
