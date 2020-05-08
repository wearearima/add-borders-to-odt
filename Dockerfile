FROM pandoc/latex:2.6
RUN apk update && apk add python3
COPY ./addBorders.py /app/addBorders.py
COPY ./entrypoint.sh /app/entrypoint.sh
RUN chmod u+x /app/*
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]
