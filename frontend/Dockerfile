# 1. THE BASE (Node.js for JavaScript)
FROM node:20-alpine

# 2. THE SETUP
WORKDIR /app

# 3. THE DEPENDENCIES
# Copy just the shopping list first (caching trick)
COPY package.json .
RUN npm install

# 4. THE CODE
COPY . .

# 5. THE STARTUP
# We add "--host" so the website is visible outside the container
CMD ["npm", "run", "dev", "--", "--host"]