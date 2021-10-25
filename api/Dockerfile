FROM python

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install  --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY api.py /app
CMD python api.py
