FROM python:3.14-alpine

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D nonroot
RUN mkdir /home/app && chown -R nonroot:nonroot /home/app
WORKDIR /home/app
USER nonroot

COPY --chown=nonroot:nonroot ./src ./src

CMD ["fastapi", "dev", "src/main.py", "--host", "0.0.0.0", "--port", "8888"]
