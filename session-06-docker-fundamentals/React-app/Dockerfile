FROM node:22-alpine AS build
WORKDIR /app
COPY package.json index.html src.jsx ./
RUN npm install --no-audit --no-fund && npm run build

FROM nginx:1.27-alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
