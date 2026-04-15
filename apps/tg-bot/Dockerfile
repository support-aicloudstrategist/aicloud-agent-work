FROM python:3.13-alpine
WORKDIR /app
COPY bot.py /app/bot.py
RUN adduser -D -h /home/bot bot && mkdir -p /data && chown -R bot:bot /data /app
USER bot
ENV PYTHONUNBUFFERED=1
CMD ["python", "/app/bot.py"]
