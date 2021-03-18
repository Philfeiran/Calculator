
FROM python:3
ADD calculatorTest.py /
RUN pip install pystrich
CMD [ "python", "./calculatorTest.py" ]
