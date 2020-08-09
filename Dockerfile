
# $cd "/mnt/d/Dropbox/Python Projects/market_notification"
# $export DOCKER_CONTENT_TRUST=0
# $pip freeze > requirements.txt (remender to first activate the enviroment)
# $docker build --no-cache -t market-notification-app .
# $docker run --name market-notification-NASDAQ-100 --restart unless-stopped market-notification-app

FROM python:3-alpine
RUN apk update
# delete cache files
RUN rm -vrf /var/cache/apk/*

WORKDIR "/usr/src/app"

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -U setuptools pip

# Install dependencies:
#COPY requirements.txt .
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir yfinance
RUN pip install --no-cache-dir pytz
RUN pip install --no-cache-dir notify-run
#RUN pip install --no-cache-dir -r requirements.txt

# Run the application:
COPY app.py .
CMD ["python", "app.py"]