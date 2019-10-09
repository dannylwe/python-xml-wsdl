from zeep import Client

client = Client(wsdl="http://www.dneonline.com/calculator.asmx?WSDL")
print(client.service.Add(29, 30), "addition")   #59
print(client.service.Divide(10, 5), "division") #2

####################################################################

# To get a schema of the available services:

# python -mzeep http://www.dneonline.com/calculator.asmx?WSDL

# Result:
#     .....
#     Service: Calculator
#      Port: CalculatorSoap (Soap11Binding: {http://tempuri.org/}CalculatorSoap)
#          Operations:
#             Add(intA: xsd:int, intB: xsd:int) -> AddResult: xsd:int
#             Divide(intA: xsd:int, intB: xsd:int) -> DivideResult: xsd:int
#             Multiply(intA: xsd:int, intB: xsd:int) -> MultiplyResult: xsd:int
#             Subtract(intA: xsd:int, intB: xsd:int) -> SubtractResult: xsd:int
#     ....
####################################################################
