#!/bin/bash

echo "🔨 Building the Docker image..."

docker build -t shopping-cart-service:latest .

docker run -d -p 8080:8080 -e FLASK_ENV=testing shopping-cart-service

echo "🚀 The shopping-cart-service Flask app is now running."
echo "🌐 You can access it by opening a web browser and entering:"
echo "   🌍 http://localhost:8080"
echo "   or"
echo "   🌐 http://YOUR_SERVER_IP:8080 (if accessing remotely)"