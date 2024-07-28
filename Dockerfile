FROM hrishi2861/terabox:latest
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash", "start.sh"]
